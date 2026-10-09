"""Count tokens and estimate API spend for every wheel, from the raw runs.

Usage:
    python3 tools/spending.py            # print the spending report
    python3 tools/spending.py --write    # also write SPENDING.md (git ignores it)

Tokens come from each saved answer's "usage" field, so they are exact. Costs are
estimates from each company's list prices in PRICES below, converted to euros at
EUR_USD. xAI records the real cost of each request ("cost_in_usd_ticks"), so Grok
costs use that instead of list prices. Newest wheel first, oldest last, and the
first line is always the total.
"""

import datetime
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Subscriptions used for the research, paid monthly from 1 October 2026.
# Each month that has started counts in full.
SUBSCRIPTIONS_EUR_PER_MONTH = 98
SUBSCRIPTIONS_START = datetime.date(2026, 10, 1)


def subscriptions_eur(today=None):
    today = today or datetime.date.today()
    months = (today.year - SUBSCRIPTIONS_START.year) * 12 + today.month - SUBSCRIPTIONS_START.month + 1
    return max(months, 0) * SUBSCRIPTIONS_EUR_PER_MONTH

# US dollars per million tokens, list prices, standard tier.
# input: uncached input; write: writing to the cache; read: reading from the cache.
PRICES = {
    # Anthropic, from Anthropic's model and prompt caching reference (cached 6 October 2026).
    # Cache writes are 1.25x input for the 5-minute cache, which the runs used.
    "claude-fable-5-1": {"input": 10.00, "write": 12.50, "read": 0.25, "output": 50.00},
    "claude-opus-5-5": {"input": 4.00, "write": 5.00, "read": 0.20, "output": 20.00},
    "claude-sonnet-5-5": {"input": 2.00, "write": 2.50, "read": 0.20, "output": 10.00},
    "claude-haiku-4-5": {"input": 1.00, "write": 1.25, "read": 0.10, "output": 5.00},
    # OpenAI, standard tier, prompts of 272,000 tokens or fewer. Reasoning tokens are billed as output.
    # GPT-5.6 sol's prices are promotional, "at least through November 21, 2026".
    "gpt-6-astra": {"input": 10.00, "write": 12.50, "read": 1.00, "output": 50.00},
    "gpt-5.6-sol": {"input": 4.00, "write": 5.00, "read": 0.40, "output": 20.00},
    # Google, paid standard tier, prompts of 200,000 tokens or fewer. Thinking tokens are billed as output.
    # Gemini 3.8 Flash's prices apply through 31 December 2026, then double.
    "gemini-3.1-pro-preview": {"input": 2.00, "read": 0.20, "output": 12.00},
    "gemini-3.8-flash": {"input": 0.75, "read": 0.075, "output": 3.75},
    # xAI, prompts under 200,000 tokens. Only used if a row has no recorded cost.
    "grok-4.7": {"input": 2.00, "read": 0.50, "output": 6.00},
    "grok-4.3": {"input": 1.25, "read": 0.20, "output": 2.50},
}
PRICE_SOURCES = {
    "Anthropic": "Anthropic's model and prompt caching reference, cached 6 October 2026",
    "OpenAI": "https://developers.openai.com/api/docs/pricing, checked 9 October 2026",
    "Google": "https://ai.google.dev/gemini-api/docs/pricing, checked 9 October 2026 (page last updated 7 October 2026)",
    "xAI": "the cost xAI records for each request, at 10,000,000,000 ticks to the US dollar (https://docs.x.ai/developers/cost-tracking); list prices from https://docs.x.ai/developers/models",
    "Euro rate": "European Central Bank reference rate, 1.1186 US dollars to the euro on 8 October 2026",
}
EUR_USD = 1.1186  # US dollars per euro
EUR_USD_DATE = "8 October 2026"
XAI_TICKS_PER_USD = 1e10

WHEEL_NAMES = {
    "001-button-variant": "Wheel 001, button variant",
    "002-other-models": "Wheel 002, other models",
    "003-three-missing-rules": "Wheel 003, 3 missing rules",
    "004-new-button-rules": "Wheel 004, new button rules",
}


def tokens(row):
    """Return (uncached input, cache write, cache read, output) for one answer."""
    u = row.get("usage") or {}
    p = row.get("provider") or "anthropic"
    if p == "anthropic":
        return (u.get("input_tokens", 0), u.get("cache_creation_input_tokens", 0) or 0,
                u.get("cache_read_input_tokens", 0) or 0, u.get("output_tokens", 0))
    if p == "openai":
        d = u.get("input_tokens_details") or {}
        cached = d.get("cached_tokens", 0) or 0
        write = d.get("cache_write_tokens", 0) or 0
        # input_tokens includes cached and written tokens; output_tokens includes reasoning
        return (u.get("input_tokens", 0) - cached - write, write, cached, u.get("output_tokens", 0))
    if p == "google":
        cached = u.get("cachedContentTokenCount", 0) or 0
        # thinking tokens are counted separately and billed as output
        out = (u.get("candidatesTokenCount", 0) or 0) + (u.get("thoughtsTokenCount", 0) or 0)
        return (u.get("promptTokenCount", 0) - cached, 0, cached, out)
    if p == "xai":
        d = u.get("prompt_tokens_details") or {}
        cached = d.get("cached_tokens", 0) or 0
        r = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0) or 0
        # reasoning tokens are counted separately from completion tokens
        return (u.get("prompt_tokens", 0) - cached, 0, cached, (u.get("completion_tokens", 0) or 0) + r)
    raise ValueError(f"unknown provider {p}")


def cost_usd(model, row, t):
    u = row.get("usage") or {}
    if "cost_in_usd_ticks" in u and XAI_TICKS_PER_USD:
        return u["cost_in_usd_ticks"] / XAI_TICKS_PER_USD
    pr = PRICES.get(model)
    if not pr:
        return None
    i, w, r, o = t
    return (i * pr["input"] + w * pr.get("write", pr["input"]) + r * pr.get("read", pr["input"]) + o * pr["output"]) / 1e6


def collect():
    data = defaultdict(lambda: defaultdict(lambda: {"answers": 0, "tok": [0, 0, 0, 0], "usd": 0.0, "unpriced": 0}))
    for wheel in sorted(WHEEL_NAMES):
        for f in sorted((ROOT / "wheels" / wheel / "runs").glob("*/*.jsonl")):
            for line in f.read_text().splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                model = row["model"]
                label = model + ("-low" if row.get("effort") == "low" else "")
                t = tokens(row)
                c = cost_usd(model, row, t)
                d = data[wheel][label]
                d["answers"] += 1
                d["tok"] = [a + b for a, b in zip(d["tok"], t)]
                if c is None:
                    d["unpriced"] += 1
                else:
                    d["usd"] += c
    return data


def eur(usd):
    return usd / EUR_USD if EUR_USD else None


def report(data):
    wheel_totals = {w: sum(m["usd"] for m in models.values()) for w, models in data.items()}
    total = sum(wheel_totals.values())
    answers = sum(m["answers"] for models in data.values() for m in models.values())
    subs = subscriptions_eur()
    lines = [f"Total so far: about €{eur(total) + subs:,.2f}: €{eur(total):,.2f} of pay-as-you-go API credit and €{subs:,} of subscriptions, for {answers:,} answers", ""]
    lines += ["# Spending", "",
              f"Costs are estimates from each company's list prices, converted at {EUR_USD} US dollars to the euro "
              f"(European Central Bank reference rate, {EUR_USD_DATE}). Grok costs are the real cost xAI records for each "
              "request. Tokens are exact, from the raw runs. Rebuild this file with `python3 tools/spending.py --write`.", ""]
    for wheel in sorted(data, reverse=True):
        models = data[wheel]
        lines += [f"## {WHEEL_NAMES[wheel]}: about €{eur(wheel_totals[wheel]):,.2f}", "",
                  "| Model | Answers | Input tokens | Cached input tokens | Output tokens | Cost |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for label in sorted(models):
            m = models[label]
            i, w, r, o = m["tok"]
            note = f", {m['unpriced']} answers not priced" if m["unpriced"] else ""
            lines.append(f"| {label} | {m['answers']:,} | {i + w:,} | {r:,} | {o:,} | €{eur(m['usd']):,.2f}{note} |")
        lines.append("")
    lines += ["## Price sources", ""] + [f"- {k}: {v}" for k, v in sorted(PRICE_SOURCES.items())] + [""]
    return "\n".join(lines)


if __name__ == "__main__":
    text = report(collect())
    print(text)
    if "--write" in sys.argv:
        (ROOT / "SPENDING.md").write_text(text)
        print(f"\nWrote {ROOT / 'SPENDING.md'}")
