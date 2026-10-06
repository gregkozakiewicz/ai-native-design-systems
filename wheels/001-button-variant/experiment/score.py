"""Score a run folder and write summary.md inside it.

Usage:
    python3 score.py ../runs/2026-10-07-opus-5-5-medium
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
if len(sys.argv) != 2:
    raise SystemExit(__doc__)
RESULTS_DIR = Path(sys.argv[1])
SUMMARY = RESULTS_DIR / "summary.md"

LEVEL_NAMES = {"A": "A · names only", "B": "B · human docs", "C": "C · machine rules"}


def load():
    rows = []
    for path in sorted(RESULTS_DIR.glob("*.jsonl")):
        for line in path.read_text().splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


def pct(n, d):
    return f"{100 * n / d:.0f}%" if d else "–"


def by_level(rows):
    levels = defaultdict(list)
    for r in rows:
        levels[r["level"]].append(r)
    return dict(sorted(levels.items()))


def accuracy(rows):
    return sum(r["correct"] for r in rows), len(rows)


def consistency(rows):
    """Share of scenarios where every run gave the same answer."""
    answers = defaultdict(set)
    for r in rows:
        answers[r["id"]].add(r["answer"])
    stable = sum(1 for a in answers.values() if len(a) == 1)
    return stable, len(answers)


def over_flagging(rows):
    """Runs that answered `none` when a variant was expected."""
    eligible = [r for r in rows if r["expected"] != "none"]
    flagged = [r for r in eligible if r["answer"] == "none"]
    return len(flagged), len(eligible)


def per_category(rows):
    cats = defaultdict(list)
    for r in rows:
        cats[r["category"]].append(r)
    return {c: accuracy(rs) for c, rs in cats.items()}


def matched_pairs(rows, pairs):
    """For each (original, pair) return how many runs got both / only original / only pair / neither."""
    runs = defaultdict(dict)
    for r in rows:
        runs[r["run"]][r["id"]] = r["correct"]
    out = {}
    for original, pair in pairs:
        tally = {"both": 0, "original only": 0, "pair only": 0, "neither": 0}
        for run_results in runs.values():
            if original not in run_results or pair not in run_results:
                continue
            o, p = run_results[original], run_results[pair]
            key = "both" if o and p else "original only" if o else "pair only" if p else "neither"
            tally[key] += 1
        out[(original, pair)] = tally
    return out


def hardest(rows, n=6):
    """Scenarios most often wrong, with the wrong answers given."""
    by_id = defaultdict(list)
    for r in rows:
        by_id[r["id"]].append(r)
    scored = []
    for sid, rs in by_id.items():
        wrong = [r for r in rs if not r["correct"]]
        if wrong:
            given = sorted({r["answer"] for r in wrong})
            scored.append((len(wrong), sid, rs[0]["button"], rs[0]["expected"], given))
    scored.sort(reverse=True)
    return scored[:n]


def tokens(rows):
    inp = sum(r["usage"].get("input_tokens", 0) + r["usage"].get("cache_read_input_tokens", 0) + r["usage"].get("cache_creation_input_tokens", 0) for r in rows)
    out = sum(r["usage"].get("output_tokens", 0) for r in rows)
    return inp, out


def main():
    rows = load()
    if not rows:
        raise SystemExit(f"No results in {RESULTS_DIR}. Run: python3 run.py")
    levels = by_level(rows)

    pairs = []
    scenarios_md = (HERE / "scenarios.md").read_text()
    for line in scenarios_md.splitlines():
        if line.startswith("| ") and "#" in line.split("|")[-2]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            try:
                pairs.append((int(cells[4].lstrip("#").split()[0]), int(cells[0])))
            except (ValueError, IndexError):
                pass

    lines = ["# Results", ""]
    models = sorted({r["model"] for r in rows})
    efforts = sorted({r["effort"] for r in rows})
    lines.append(f"Model: {', '.join(models)} · effort: {', '.join(efforts)} · {len(rows)} answers")
    lines.append("")

    lines += ["## Headline", "", "| Level | Accuracy | Consistency | Over-flagging |", "|---|---|---|---|"]
    for level, rs in levels.items():
        a, an = accuracy(rs)
        c, cn = consistency(rs)
        f, fn = over_flagging(rs)
        lines.append(f"| {LEVEL_NAMES.get(level, level)} | {pct(a, an)} ({a}/{an}) | {pct(c, cn)} | {pct(f, fn)} ({f}/{fn}) |")
    lines += ["", "Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.", ""]

    categories = sorted({r["category"] for r in rows}, key=lambda c: scenarios_md.find(f"### {c}"))
    lines += ["## By category", "", "| Category | " + " | ".join(LEVEL_NAMES.get(l, l) for l in levels) + " |", "|---|" + "---|" * len(levels)]
    for cat in categories:
        cells = []
        for rs in levels.values():
            a, n = per_category(rs).get(cat, (0, 0))
            cells.append(pct(a, n))
        lines.append(f"| {cat} | " + " | ".join(cells) + " |")
    lines.append("")

    if pairs:
        lines += ["## Matched pairs", "", "Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.", ""]
        lines += ["| Pair | Level | Both | Original only | Pair only | Neither |", "|---|---|---|---|---|---|"]
        for level, rs in levels.items():
            for (o, p), t in matched_pairs(rs, pairs).items():
                lines.append(f"| #{o} → #{p} | {level} | {t['both']} | {t['original only']} | {t['pair only']} | {t['neither']} |")
        lines.append("")

    lines += ["## Hardest scenarios per level", ""]
    for level, rs in levels.items():
        lines.append(f"**{LEVEL_NAMES.get(level, level)}**")
        lines.append("")
        h = hardest(rs)
        if not h:
            lines.append("- all correct")
        for wrong, sid, button, expected, given in h:
            lines.append(f"- #{sid} \"{button}\": wrong {wrong}×, expected `{expected}`, got {', '.join(f'`{g}`' for g in given)}")
        lines.append("")

    inp, out = tokens(rows)
    lines += ["## Tokens", "", f"Input {inp:,} · output {out:,}", ""]

    text = "\n".join(lines)
    SUMMARY.write_text(text)
    print(text)
    print(f"\nWritten to {SUMMARY}")


if __name__ == "__main__":
    main()
