# Results

Model: gpt-5.6-sol · effort: default · 261 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 22% (19/87) | 83% | 80% (67/84) |
| B · human docs | 71% (62/87) | 90% | 0% (0/84) |
| C · machine rules | 92% (80/87) | 93% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 20% | 100% | 100% |
| Context | 14% | 71% | 90% |
| Traps | 0% | 33% | 58% |
| Conflicts | 58% | 100% | 100% |
| Interaction & tools | 33% | 33% | 100% |
| Matched pairs | 17% | 72% | 100% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | A | 0 | 0 | 1 | 2 |
| #20 → #25 | A | 0 | 1 | 1 | 1 |
| #15 → #26 | A | 0 | 0 | 0 | 3 |
| #11 → #27 | A | 0 | 0 | 0 | 3 |
| #10 → #28 | A | 0 | 0 | 0 | 3 |
| #13 → #29 | A | 0 | 0 | 1 | 2 |
| #16 → #24 | B | 1 | 0 | 2 | 0 |
| #20 → #25 | B | 3 | 0 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 2 | 1 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #10 → #28 | B | 2 | 1 | 0 | 0 |
| #13 → #29 | B | 0 | 0 | 3 | 0 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 3 | 0 | 0 | 0 |
| #13 → #29 | C | 1 | 0 | 2 | 0 |

## Hardest scenarios per level

**A · names only**

- #28 "Not now": wrong 3×, expected `ghost`, got `none`
- #27 "Dismiss": wrong 3×, expected `secondary`, got `none`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `destructive`, `none`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `none`
- #22 "Add file": wrong 3×, expected `ghost`, got `none`
- #19 "Request changes": wrong 3×, expected `secondary`, got `none`

**B · human docs**

- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #22 "Add file": wrong 3×, expected `ghost`, got `secondary`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`
- #13 "Log out": wrong 3×, expected `secondary`, got `ghost`
- #11 "Close": wrong 3×, expected `secondary`, got `primary`

**C · machine rules**

- #14 "Archive project": wrong 3×, expected `secondary`, got `ghost`
- #13 "Log out": wrong 2×, expected `secondary`, got `ghost`
- #8 "Export CSV": wrong 2×, expected `secondary`, got `ghost`

## Tokens

Input 151,635 · output 19,400
