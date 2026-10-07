# Results

Model: gpt-6-astra · effort: default · 261 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 17% (15/87) | 100% | 86% (72/84) |
| B · human docs | 72% (63/87) | 86% | 0% (0/84) |
| C · machine rules | 97% (84/87) | 100% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 20% | 100% | 100% |
| Context | 14% | 71% | 100% |
| Traps | 0% | 67% | 100% |
| Conflicts | 50% | 83% | 100% |
| Interaction & tools | 33% | 44% | 100% |
| Matched pairs | 0% | 61% | 83% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | A | 0 | 0 | 0 | 3 |
| #20 → #25 | A | 0 | 0 | 0 | 3 |
| #15 → #26 | A | 0 | 0 | 0 | 3 |
| #11 → #27 | A | 0 | 0 | 0 | 3 |
| #10 → #28 | A | 0 | 0 | 0 | 3 |
| #13 → #29 | A | 0 | 0 | 0 | 3 |
| #16 → #24 | B | 3 | 0 | 0 | 0 |
| #20 → #25 | B | 3 | 0 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 0 | 3 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #10 → #28 | B | 2 | 1 | 0 | 0 |
| #13 → #29 | B | 2 | 0 | 1 | 0 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 0 | 3 | 0 | 0 |
| #13 → #29 | C | 3 | 0 | 0 | 0 |

## Hardest scenarios per level

**A · names only**

- #29 "Pay by bank transfer": wrong 3×, expected `secondary`, got `none`
- #28 "Not now": wrong 3×, expected `ghost`, got `none`
- #27 "Dismiss": wrong 3×, expected `secondary`, got `none`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `none`
- #25 "Stay on Free": wrong 3×, expected `secondary`, got `none`
- #24 "Update card": wrong 3×, expected `primary`, got `none`

**B · human docs**

- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `destructive`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`
- #11 "Close": wrong 3×, expected `secondary`, got `primary`
- #8 "Export CSV": wrong 3×, expected `secondary`, got `ghost`

**C · machine rules**

- #28 "Not now": wrong 3×, expected `ghost`, got `secondary`

## Tokens

Input 151,635 · output 18,871
