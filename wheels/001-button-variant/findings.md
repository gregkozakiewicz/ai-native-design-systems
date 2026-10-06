# Findings

## Summary

Yes. Given machine-readable rules, Claude Opus 5.5 chose the correct button variant in 76 of 81 answers, against 64 of 81 with typical human documentation and 53 of 81 with variant names alone. All 5 misses with rules trace to one gap in the rules, not to the agent.

## Evidence

All figures come from `runs/2026-10-07-opus-5-5-medium/`, summarised in its `summary.md`.

| Level | Correct answers | Scenarios where all 3 runs agreed | 'None' where a variant was expected |
| --- | --- | --- | --- |
| A, names only | 53 of 81 | 26 of 27 | 0 of 78 |
| B, human docs | 64 of 81 | 22 of 27 | 0 of 78 |
| C, machine rules | 76 of 81 | 26 of 27 | 0 of 78 |

The 5 easy scenarios were right in all 15 answers at every level. The whole gap between levels comes from the hard ones.

| Category | A, names only | B, human docs | C, machine rules |
| --- | --- | --- | --- |
| Context | 12 of 21 | 18 of 21 | 19 of 21 |
| Traps | 9 of 12 | 9 of 12 | 9 of 12 |
| Conflicts | 11 of 12 | 11 of 12 | 12 of 12 |
| Interaction and tools | 0 of 9 | 4 of 9 | 9 of 9 |
| Matched pairs | 6 of 12 | 7 of 12 | 12 of 12 |

### Rules beat human documentation by 15 points

Rules scored 94% (76 of 81), human documentation 79% (64 of 81), and names alone 65% (53 of 81). The success criterion was 90% and a 10-point lead, so the wheel is answered "yes".

### Human documentation raised accuracy but lowered consistency compared with names only

Consistency measures whether the 3 separate answers to a scenario were identical, right or wrong. With names only, the agent fell back on convention and gave the same answer each time: 26 of 27 scenarios agreed across runs, though only 53 of 81 answers were right. With prose, accuracy rose to 64 of 81 but agreement fell to 22 of 27. On scenario 11 ('Close' as the only button in a read-only dialog) one run wrote "one could argue for Secondary", then chose primary anyway. Prose gave the agent room to reason towards different answers in different runs.

### The agent applied the rules rather than matching their words

Four scenarios reword a rule that another scenario tests directly, with none of the rule's words in common. With rules, all 4 pairs were right in all 3 runs: 12 of 12. No run got the original right and the reworded pair wrong, at any level. The failure we expected did not appear.

### 'None' was used only where it belonged

Scenario 21, a press-and-hold recording control, is the only scenario where 'none' is correct. With rules it was flagged in 3 of 3 runs. With names only it was forced into primary in 3 of 3 runs. With human documentation it was forced into primary or secondary in 3 of 3 runs. Across all 234 answers where a variant was expected, 'none' was never chosen.

## Failure modes seen

The 5 misses with rules are one disagreement. On 'Log out' (3 of 3 runs) and 'Skip for now' (2 of 3 runs) the agent chose secondary where the key says ghost. Its reasoning was the same each time: a real choice the user must be able to find. Nothing in the rules says when a legitimate alternative is ghost rather than secondary, so the agent used the emphasis rule and reached a defensible answer. This is a gap in the rules, and one rule would close it.

On reflection the designer agreed with the agent on 'Log out': the key now says secondary, and the rules changed the agent's answer away from the convention it used at levels A and B (ghost in 6 of 6 runs). On 'Skip for now' the designer kept ghost, because the product wants users to finish onboarding. Rule H12 now records that line, and 2 scenarios were added to test it. Run 1 is scored against the original key; a second run tests the revised set.

With human documentation, the agent twice called 'Revert to original' destructive because redoing edits by hand "is not an undo". The documentation's one line on destructive ("delete data or can't be undone") does not say that reversible means recoverable, not instant.

Our own setup had one fault. Level B first contained a line saying variants are for click or tap actions, which gave away scenario 21. We removed it before the full run and did not keep the dry run.

## Open questions raised

These go to `../../QUESTIONS.md`.

- does the same rule set hold for other models, such as Sonnet 5.5, Codex and Gemini
- does the lead for rules shrink at low reasoning effort, where the agent thinks less before answering
- where is the line between a secondary alternative and a ghost option, and can it be written as one rule
