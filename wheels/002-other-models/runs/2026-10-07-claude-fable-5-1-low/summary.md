# Results

Model: claude-fable-5-1 · effort: low · 261 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 55% (48/87) | 72% | 33% (28/84) |
| B · human docs | 80% (70/87) | 97% | 0% (0/84) |
| C · machine rules | 100% (87/87) | 100% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 100% | 100% | 100% |
| Context | 29% | 71% | 100% |
| Traps | 33% | 58% | 100% |
| Conflicts | 92% | 100% | 100% |
| Interaction & tools | 44% | 67% | 100% |
| Matched pairs | 44% | 83% | 100% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | A | 0 | 0 | 3 | 0 |
| #20 → #25 | A | 3 | 0 | 0 | 0 |
| #15 → #26 | A | 0 | 0 | 0 | 3 |
| #11 → #27 | A | 0 | 0 | 0 | 3 |
| #10 → #28 | A | 0 | 0 | 0 | 3 |
| #13 → #29 | A | 1 | 1 | 1 | 0 |
| #16 → #24 | B | 3 | 0 | 0 | 0 |
| #20 → #25 | B | 3 | 0 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 3 | 0 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #10 → #28 | B | 3 | 0 | 0 | 0 |
| #13 → #29 | B | 1 | 0 | 2 | 0 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 3 | 0 | 0 | 0 |
| #13 → #29 | C | 3 | 0 | 0 | 0 |

## Hardest scenarios per level

**A · names only**

- #28 "Not now": wrong 3×, expected `ghost`, got `none`
- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`, `none`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `none`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `secondary`
- #16 "Try again": wrong 3×, expected `primary`, got `none`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`

**B · human docs**

- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`
- #11 "Close": wrong 3×, expected `secondary`, got `primary`
- #8 "Export CSV": wrong 3×, expected `secondary`, got `ghost`
- #13 "Log out": wrong 2×, expected `secondary`, got `ghost`

**C · machine rules**

- all correct

## Tokens

Input 265,767 · output 18,117
