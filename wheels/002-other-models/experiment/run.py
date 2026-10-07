"""Run wheel 001's scenarios and levels through models from other companies.

Usage:
    python3 run.py --model gpt-5.6-sol
    python3 run.py --model gemini-3.1-pro-preview
    python3 run.py --model claude-sonnet-5-5
    python3 run.py --model claude-haiku-4-5 --only 6 21 --runs 1   # dry run

The provider is read from the model name: claude-* goes to Anthropic,
gpt-*/o* to OpenAI, gemini-* to Google, grok-* to xAI. Everything else is wheel 001's:
scenarios, levels, system prompt, answer schema, row format. Answers go to
../runs/<date>-<model>/<level>.jsonl. Score with wheel 001's score.py.
"""

import argparse
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import env  # noqa: E402,F401  loads API keys from the repo's .env

sys.path.insert(0, str(HERE.parents[1] / "001-button-variant" / "experiment"))
import run as w1  # noqa: E402  wheel 001's runner: scenarios, levels, prompt, schema

RUNS_DIR = HERE.parent / "runs"


def provider_for(model):
    if model.startswith("claude-"):
        return "anthropic"
    if model.startswith(("gpt-", "o3", "o4")):
        return "openai"
    if model.startswith("gemini-"):
        return "google"
    if model.startswith("grok-"):
        return "xai"
    sys.exit(f"Cannot tell the provider from model name {model!r}")


def user_prompt(scenario):
    return (
        f"Context: {scenario['scenario']}\n"
        f"Button label: \"{scenario['button']}\"\n\n"
        "Which variant should this button use?"
    )


def post_json(url, headers, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={**headers, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def ask_openai(model, level_text, scenario):
    body = {
        "model": model,
        "instructions": f"{w1.SYSTEM_INTRO}\n\n--- DESIGN SYSTEM REFERENCE ---\n\n{level_text}",
        "input": user_prompt(scenario),
        "text": {"format": {"type": "json_schema", "name": "variant_answer", "schema": w1.ANSWER_SCHEMA, "strict": True}},
    }
    data = post_json("https://api.openai.com/v1/responses", {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]}, body)
    text = None
    for item in data.get("output", []):
        if item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    text = part["text"]
                elif part.get("type") == "refusal":
                    return {"variant": None, "reason": "refused: " + part.get("refusal", ""), "usage": data.get("usage", {})}
    if text is None:
        raise RuntimeError(f"no text in response: {json.dumps(data)[:300]}")
    answer = json.loads(text)
    answer["usage"] = data.get("usage", {})
    return answer


def ask_google(model, level_text, scenario):
    schema = {
        "type": "OBJECT",
        "properties": {
            "variant": {"type": "STRING", "enum": w1.ANSWER_SCHEMA["properties"]["variant"]["enum"]},
            "reason": {"type": "STRING"},
        },
        "required": ["variant", "reason"],
    }
    body = {
        "system_instruction": {"parts": [{"text": f"{w1.SYSTEM_INTRO}\n\n--- DESIGN SYSTEM REFERENCE ---\n\n{level_text}"}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt(scenario)}]}],
        "generationConfig": {"responseMimeType": "application/json", "responseSchema": schema},
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    data = post_json(url, {"x-goog-api-key": os.environ["GEMINI_API_KEY"]}, body)
    cand = data["candidates"][0]
    if cand.get("finishReason") not in (None, "STOP"):
        return {"variant": None, "reason": "stopped: " + cand.get("finishReason", ""), "usage": data.get("usageMetadata", {})}
    text = "".join(p.get("text", "") for p in cand["content"]["parts"])
    answer = json.loads(text)
    answer["usage"] = data.get("usageMetadata", {})
    return answer


def ask_xai(model, level_text, scenario):
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": f"{w1.SYSTEM_INTRO}\n\n--- DESIGN SYSTEM REFERENCE ---\n\n{level_text}"},
            {"role": "user", "content": user_prompt(scenario)},
        ],
        "response_format": {"type": "json_schema", "json_schema": {"name": "variant_answer", "schema": w1.ANSWER_SCHEMA, "strict": True}},
    }
    data = post_json("https://api.x.ai/v1/chat/completions", {"Authorization": "Bearer " + os.environ["XAI_API_KEY"]}, body)
    choice = data["choices"][0]
    if choice.get("finish_reason") not in (None, "stop"):
        return {"variant": None, "reason": "stopped: " + str(choice.get("finish_reason")), "usage": data.get("usage", {})}
    answer = json.loads(choice["message"]["content"])
    answer["usage"] = data.get("usage", {})
    return answer


EFFORT = None  # set from --effort; None means each Claude model's default (medium, or none for Haiku)


def ask_anthropic(model, level_text, scenario):
    import anthropic
    client = ask_anthropic.client = getattr(ask_anthropic, "client", None) or anthropic.Anthropic()
    effort = EFFORT or (None if model.startswith("claude-haiku") else "medium")
    return w1.ask(client, model, effort, level_text, scenario)


ASK = {"openai": ask_openai, "google": ask_google, "anthropic": ask_anthropic, "xai": ask_xai}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", required=True)
    parser.add_argument("--levels", nargs="+", default=list(w1.LEVEL_FILES), choices=list(w1.LEVEL_FILES))
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--only", type=int, nargs="*")
    parser.add_argument("--out", help="run folder (default: ../runs/<date>-<model>)")
    parser.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"], help="Claude models only; default is the model's own")
    args = parser.parse_args()
    global EFFORT
    EFFORT = args.effort

    provider = provider_for(args.model)
    ask = ASK[provider]
    scenarios = w1.load_scenarios()
    if args.only:
        scenarios = [s for s in scenarios if s["id"] in args.only]

    if args.out:
        out_dir = Path(args.out)
    else:
        label = f"{args.model}-{args.effort}" if args.effort else args.model
        base = RUNS_DIR / f"{datetime.date.today().isoformat()}-{label}"
        out_dir, n = base, 2
        while out_dir.exists():
            out_dir = base.with_name(f"{base.name}-run{n}")
            n += 1
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Writing to {out_dir}")

    total = len(args.levels) * len(scenarios) * args.runs
    count = 0
    for level in args.levels:
        level_text = (w1.LEVELS_DIR / w1.LEVEL_FILES[level]).read_text()
        out_path = out_dir / f"{level}.jsonl"
        done = w1.load_done(out_path)
        with out_path.open("a") as out:
            for scenario in scenarios:
                for run in range(1, args.runs + 1):
                    count += 1
                    if (scenario["id"], run) in done:
                        continue
                    answer = None
                    for attempt in range(4):
                        try:
                            answer = ask(args.model, level_text, scenario)
                            break
                        except urllib.error.HTTPError as e:
                            detail = e.read().decode(errors="ignore")
                            if e.code == 429 and "per_day" in detail:
                                print(f"\n{provider} daily request cap reached. Saved so far: {out_dir}. "
                                      f"Resume tomorrow with: python3 run.py --model {args.model} --out {out_dir}")
                                return
                            detail = detail[:300]
                            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                                wait = int(e.headers.get("retry-after", "20") or 20)
                                print(f"  {e.code} from {provider}, waiting {wait}s", file=sys.stderr)
                                time.sleep(wait)
                                continue
                            sys.exit(f"{provider} returned {e.code}: {detail}")
                        except Exception as e:  # SDK errors, network, bad JSON
                            if attempt < 3:
                                print(f"  {type(e).__name__}: {e}; retrying", file=sys.stderr)
                                time.sleep(10 * (attempt + 1))
                                continue
                            raise
                    row = {
                        "level": level,
                        "id": scenario["id"],
                        "run": run,
                        "category": scenario["category"],
                        "button": scenario["button"],
                        "expected": scenario["expected"],
                        "answer": answer["variant"],
                        "correct": answer["variant"] == scenario["expected"],
                        "reason": answer["reason"],
                        "model": args.model,
                        "provider": provider,
                        "effort": args.effort or "default",
                        "usage": answer["usage"],
                    }
                    out.write(json.dumps(row) + "\n")
                    out.flush()
                    mark = "✓" if row["correct"] else "✗"
                    print(f"[{count}/{total}] {level} #{scenario['id']:>2} run {run}  {mark} {str(row['answer']):<12} (expected {row['expected']})")

    print(f"\nSaved to {out_dir}. Score with: python3 ../../001-button-variant/experiment/score.py {out_dir}")


if __name__ == "__main__":
    main()
