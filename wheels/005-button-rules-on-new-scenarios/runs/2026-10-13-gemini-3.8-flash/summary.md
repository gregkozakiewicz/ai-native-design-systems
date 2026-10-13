# Results

Model: gemini-3.8-flash · effort: default · 72 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| C · machine rules | 53% (38/72) | 96% | 0% (0/72) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | C · machine rules |
|---|---|
| Wheel 005 | 53% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | C | 0 | 0 | 0 | 0 |
| #20 → #25 | C | 0 | 0 | 0 | 0 |
| #15 → #26 | C | 0 | 0 | 0 | 3 |
| #11 → #27 | C | 0 | 0 | 2 | 1 |
| #10 → #28 | C | 0 | 0 | 3 | 0 |
| #13 → #29 | C | 0 | 0 | 0 | 0 |

## Hardest scenarios per level

**C · machine rules**

- #26 "Copy link": wrong 3×, expected `ghost`, got `secondary`
- #25 "Save for later": wrong 3×, expected `secondary`, got `ghost`
- #21 "Add notes": wrong 3×, expected `secondary`, got `ghost`
- #18 "Undo changes": wrong 3×, expected `secondary`, got `ghost`
- #15 "Continue without insurance": wrong 3×, expected `primary`, got `secondary`
- #12 "Add to shopping list": wrong 3×, expected `secondary`, got `ghost`

## Tokens

Input 0 · output 0
