# Findings

## Summary

Yes. Given machine-readable rules, Claude Opus 5.5 chose the correct button variant in 84 of 87 answers in run 2, against 66 of 87 with typical human documentation and 58 of 87 with variant names alone. It gave the same answer in all 3 runs for all 29 scenarios. The 3 misses trace to one scenario that does not say whether the action can be undone.

Run 1, on 27 scenarios with 11 rules, scored 76 of 81 with rules. Its 5 misses were one gap in the rules. Closing that gap with rule H12 and 2 test scenarios gave run 2.

## Evidence

Run 1 is `runs/2026-10-07-opus-5-5-medium/` and run 2 is `runs/2026-10-07-opus-5-5-medium-run2/`. Each has a `summary.md`.

### Run 2: 29 scenarios, 12 rules

| Level | Correct answers | Scenarios where all 3 runs agreed | 'None' where a variant was expected |
| --- | --- | --- | --- |
| A, names only | 58 of 87 | 28 of 29 | 0 of 84 |
| B, human docs | 66 of 87 | 23 of 29 | 0 of 84 |
| C, machine rules | 84 of 87 | 29 of 29 | 0 of 84 |

| Category | A, names only | B, human docs | C, machine rules |
| --- | --- | --- | --- |
| Easy | 15 of 15 | 15 of 15 | 15 of 15 |
| Context | 12 of 21 | 17 of 21 | 21 of 21 |
| Traps | 6 of 12 | 6 of 12 | 12 of 12 |
| Conflicts | 12 of 12 | 11 of 12 | 9 of 12 |
| Interaction and tools | 1 of 9 | 4 of 9 | 9 of 9 |
| Matched pairs | 12 of 18 | 13 of 18 | 18 of 18 |

Rule H12 held. 'Skip for now' and its reworded pair 'Not now' were ghost in 6 of 6 answers with rules. 'Log out' and its pair 'Pay by bank transfer' were secondary in 6 of 6. Without rules, 'Log out' was ghost in 6 of 6 answers at levels A and B: the convention the agent falls back on disagrees with the designer, and only the rules moved it.

### Run 1: 27 scenarios, 11 rules

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

### Rules beat human documentation by 15 points in run 1 and 21 in run 2

In run 1 rules scored 94% (76 of 81), human documentation 79% (64 of 81), and names alone 65% (53 of 81). In run 2 the figures were 97% (84 of 87), 76% (66 of 87) and 67% (58 of 87). The success criterion was 90% and a 10-point lead, so the wheel is answered "yes" on both runs.

### Human documentation raised accuracy but lowered consistency compared with names only

Consistency measures whether the 3 separate answers to a scenario were identical, right or wrong. With names only, the agent fell back on convention and gave the same answer each time: 26 of 27 scenarios agreed in run 1, though only 53 of 81 answers were right. With prose, accuracy rose to 64 of 81 but agreement fell to 22 of 27. Run 2 repeated the pattern: 28 of 29, 23 of 29 and 29 of 29 for the 3 levels. On scenario 11 ('Close' as the only button in a read-only dialog) one run wrote "one could argue for Secondary", then chose primary anyway. Prose gave the agent room to reason towards different answers in different runs.

### The agent applied the rules rather than matching their words

Four scenarios in run 1, and 6 in run 2, reword a rule that another scenario tests directly, with none of the rule's words in common. With rules, every pair was right in every run: 12 of 12 in run 1 and 18 of 18 in run 2. No run got the original right and the reworded pair wrong, at any level. The failure we expected did not appear.

### 'None' was used only where it belonged

Scenario 21, a press-and-hold recording control, is the only scenario where 'none' is correct. With rules it was flagged in 3 of 3 runs. With names only it was forced into primary in 3 of 3 runs. With human documentation it was forced into primary or secondary in 3 of 3 runs. Across all 234 answers where a variant was expected, 'none' was never chosen.

## Failure modes seen

Run 2's 3 misses with rules are one scenario, 'Remove member' (17), chosen as primary in 3 of 3 runs where the key says destructive. In run 1 the same scenario was destructive in 3 of 3 runs. The rules did not change between runs on this point. The scenario does not say whether a removed member can be re-added, and the agent said so each time: run 1 assumed it cannot and chose destructive, run 2 assumed it can and chose primary. Both followed precedence step 1, reversibility, correctly. The fault is in the scenario, which should state whether the action can be undone. We have not changed it; the decision sits with the designer.

Run 1's 5 misses with rules were one disagreement. On 'Log out' (3 of 3 runs) and 'Skip for now' (2 of 3 runs) the agent chose secondary where the key says ghost. Its reasoning was the same each time: a real choice the user must be able to find. Nothing in the rules says when a legitimate alternative is ghost rather than secondary, so the agent used the emphasis rule and reached a defensible answer. This is a gap in the rules, and one rule would close it.

On reflection the designer agreed with the agent on 'Log out': the key now says secondary, and the rules changed the agent's answer away from the convention it used at levels A and B (ghost in 6 of 6 runs). On 'Skip for now' the designer kept ghost, because the product wants users to finish onboarding. Rule H12 now records that line, and 2 scenarios were added to test it. Run 1 is scored against the original key; a second run tests the revised set.

With human documentation, the agent twice called 'Revert to original' destructive because redoing edits by hand "is not an undo". The documentation's one line on destructive ("delete data or can't be undone") does not say that reversible means recoverable, not instant.

Our own setup had one fault. Level B first contained a line saying variants are for click or tap actions, which gave away scenario 21. We removed it before the full run and did not keep the dry run.

## Open questions raised

These go to `../../QUESTIONS.md`.

- does the same rule set hold for other models, such as Sonnet 5.5, Codex and Gemini
- does the lead for rules shrink at low reasoning effort, where the agent thinks less before answering
- where is the line between a secondary alternative and a ghost option, and can it be written as one rule
