# Results

Model: grok-4.3 · effort: default · 87 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| C · machine rules | 90% (78/87) | 93% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | C · machine rules |
|---|---|
| Easy | 100% |
| Context | 90% |
| Traps | 67% |
| Conflicts | 100% |
| Interaction & tools | 100% |
| Matched pairs | 83% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 0 | 3 | 0 | 0 |
| #13 → #29 | C | 0 | 0 | 3 | 0 |

## Hardest scenarios per level

**C · machine rules**

- #28 "Not now": wrong 3×, expected `ghost`, got `secondary`
- #13 "Log out": wrong 3×, expected `secondary`, got `ghost`
- #8 "Export CSV": wrong 2×, expected `secondary`, got `ghost`
- #14 "Archive project": wrong 1×, expected `secondary`, got `ghost`

## Tokens

Input 0 · output 0
