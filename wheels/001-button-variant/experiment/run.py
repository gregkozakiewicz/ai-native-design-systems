"""Run every scenario through Claude at each information level and save the answers.

Usage:
    python3 run.py                      # all levels, 3 runs each
    python3 run.py --levels A C         # only some levels
    python3 run.py --runs 5             # more repeats
    python3 run.py --model claude-sonnet-5-5

Answers go to ../runs/<date>-<model>-<effort>/<level>.jsonl, one line per
(scenario, run). Re-running with the same --out skips anything already saved,
so it is safe to stop and resume.
"""

import argparse
import datetime
import json
import re
import sys
import time
from pathlib import Path

import anthropic

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import env  # noqa: E402,F401  loads API keys from the repo's .env

HERE = Path(__file__).parent
SCENARIOS_MD = HERE / "scenarios.md"
LEVELS_DIR = HERE / "levels"
RUNS_DIR = HERE.parent / "runs"

LEVEL_FILES = {
    "A": "A-names-only.md",
    "B": "B-human-docs.md",
    "C": "C-machine-rules.md",
}

LETTER_TO_VARIANT = {
    "P": "primary",
    "S": "secondary",
    "G": "ghost",
    "D": "destructive",
    "none": "none",
}

ANSWER_SCHEMA = {
    "type": "object",
    "properties": {
        "variant": {
            "type": "string",
            "enum": ["primary", "secondary", "ghost", "destructive", "none"],
        },
        "reason": {
            "type": "string",
            "description": "One sentence. Name the rule or guideline you applied, if any.",
        },
    },
    "required": ["variant", "reason"],
    "additionalProperties": False,
}

SYSTEM_INTRO = (
    "You are a coding agent building a user interface with a design system. "
    "For each button you are shown, choose which variant to use. "
    "Base your choice only on the design system reference below; do not use "
    "outside conventions where the reference gives an answer."
)


def load_scenarios():
    """Parse the scenario tables out of scenarios.md.

    Rows look like `| 6 | A dialog ... | "Cancel" | S |`, optionally with a
    fifth `Pairs with` column. The current `###` heading is the category.
    """
    scenarios = []
    category = None
    for line in SCENARIOS_MD.read_text().splitlines():
        if line.startswith("### "):
            category = line[4:].split("(")[0].strip()
            continue
        m = re.match(r"^\|\s*(\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 3:
            continue
        text, button, answer = cells[0], cells[1].strip('"'), cells[2]
        pairs_with = None
        if len(cells) >= 4:
            pm = re.search(r"#(\d+)", cells[3])
            pairs_with = int(pm.group(1)) if pm else None
        if answer not in LETTER_TO_VARIANT:
            sys.exit(f"Scenario {m.group(1)} has an unexpected answer: {answer!r}")
        scenarios.append({
            "id": int(m.group(1)),
            "category": category,
            "scenario": text,
            "button": button,
            "expected": LETTER_TO_VARIANT[answer],
            "pairs_with": pairs_with,
        })
    if not scenarios:
        sys.exit("No scenarios found in scenarios.md")
    return scenarios


def load_done(path):
    done = set()
    if path.exists():
        for line in path.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                done.add((row["id"], row["run"]))
    return done


def ask(client, model, effort, level_text, scenario):
    user = (
        f"Context: {scenario['scenario']}\n"
        f"Button label: \"{scenario['button']}\"\n\n"
        "Which variant should this button use?"
    )
    response = client.messages.create(
        model=model,
        max_tokens=4000,
        output_config={
            "effort": effort,
            "format": {"type": "json_schema", "schema": ANSWER_SCHEMA},
        },
        system=[
            {"type": "text", "text": SYSTEM_INTRO},
            {
                "type": "text",
                "text": f"--- DESIGN SYSTEM REFERENCE ---\n\n{level_text}",
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[{"role": "user", "content": user}],
    )
    if response.stop_reason == "refusal":
        return {"variant": None, "reason": "refused", "usage": response.usage.model_dump()}
    text = next(b.text for b in response.content if b.type == "text")
    data = json.loads(text)
    data["usage"] = response.usage.model_dump()
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--levels", nargs="+", default=list(LEVEL_FILES), choices=list(LEVEL_FILES))
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--model", default="claude-opus-5-5")
    parser.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    parser.add_argument("--only", type=int, nargs="*", help="scenario ids to run (default: all)")
    parser.add_argument("--out", help="run folder (default: ../runs/<date>-<model>-<effort>)")
    args = parser.parse_args()

    scenarios = load_scenarios()
    if args.only:
        scenarios = [s for s in scenarios if s["id"] in args.only]
    if args.out:
        out_dir = Path(args.out)
    else:
        # A run folder is never reused: pick the next free name so a second
        # run on the same day does not append to the first.
        today = datetime.date.today().isoformat()
        model_slug = re.sub(r"^claude-", "", args.model)
        base = RUNS_DIR / f"{today}-{model_slug}-{args.effort}"
        out_dir, n = base, 2
        while out_dir.exists():
            out_dir = base.with_name(f"{base.name}-run{n}")
            n += 1
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Writing to {out_dir}")
    client = anthropic.Anthropic()

    total = len(args.levels) * len(scenarios) * args.runs
    done_count = 0
    for level in args.levels:
        level_text = (LEVELS_DIR / LEVEL_FILES[level]).read_text()
        out_path = out_dir / f"{level}.jsonl"
        done = load_done(out_path)
        with out_path.open("a") as out:
            for scenario in scenarios:
                for run in range(1, args.runs + 1):
                    done_count += 1
                    if (scenario["id"], run) in done:
                        continue
                    for attempt in range(3):
                        try:
                            answer = ask(client, args.model, args.effort, level_text, scenario)
                            break
                        except anthropic.RateLimitError as e:
                            wait = int(e.response.headers.get("retry-after", "30"))
                            print(f"  rate limited, waiting {wait}s", file=sys.stderr)
                            time.sleep(wait)
                        except (anthropic.APIConnectionError, anthropic.InternalServerError):
                            if attempt == 2:
                                raise
                            time.sleep(5 * (attempt + 1))
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
                        "effort": args.effort,
                        "usage": answer["usage"],
                    }
                    out.write(json.dumps(row) + "\n")
                    out.flush()
                    mark = "✓" if row["correct"] else "✗"
                    print(f"[{done_count}/{total}] {level} #{scenario['id']:>2} run {run}  {mark} {row['answer']:<12} (expected {row['expected']})")

    print(f"\nSaved to {out_dir}. Now run: python3 score.py {out_dir}")


if __name__ == "__main__":
    main()
