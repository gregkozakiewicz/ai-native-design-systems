# Results

Model: claude-opus-5-5 · effort: medium · 243 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 65% (53/81) | 96% | 0% (0/78) |
| B · human docs | 79% (64/81) | 81% | 0% (0/78) |
| C · machine rules | 94% (76/81) | 96% | 0% (0/78) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 100% | 100% | 100% |
| Context | 57% | 86% | 90% |
| Traps | 75% | 75% | 75% |
| Conflicts | 92% | 92% | 100% |
| Interaction & tools | 0% | 44% | 100% |
| Matched pairs | 50% | 58% | 100% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | A | 3 | 0 | 0 | 0 |
| #20 → #25 | A | 2 | 0 | 1 | 0 |
| #15 → #26 | A | 0 | 0 | 0 | 3 |
| #11 → #27 | A | 0 | 0 | 0 | 3 |
| #16 → #24 | B | 3 | 0 | 0 | 0 |
| #20 → #25 | B | 3 | 0 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 1 | 2 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |

## Hardest scenarios per level

**A · names only**

- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `secondary`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `secondary`
- #22 "Add file": wrong 3×, expected `ghost`, got `secondary`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`

**B · human docs**

- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`, `secondary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`
- #11 "Close": wrong 3×, expected `secondary`, got `primary`
- #26 "Revert to original": wrong 2×, expected `ghost`, got `destructive`
- #23 "Send feedback": wrong 1×, expected `ghost`, got `secondary`

**C · machine rules**

- #13 "Log out": wrong 3×, expected `ghost`, got `secondary`
- #10 "Skip for now": wrong 2×, expected `ghost`, got `secondary`

## Tokens

Input 240,759 · output 38,837
