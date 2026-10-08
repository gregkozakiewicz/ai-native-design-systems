# Results

Model: claude-haiku-4-5 · effort: default · 93 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| C · machine rules | 94% (87/93) | 97% | 0% (0/90) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | C · machine rules |
|---|---|
| New in wheel 004 | 50% |
| Easy | 100% |
| Context | 100% |
| Traps | 100% |
| Conflicts | 75% |
| Interaction & tools | 100% |
| Matched pairs | 100% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 3 | 0 | 0 | 0 |
| #13 → #29 | C | 3 | 0 | 0 | 0 |

## Hardest scenarios per level

**C · machine rules**

- #30 "Archive project": wrong 3×, expected `primary`, got `destructive`, `secondary`
- #18 "Discard changes": wrong 3×, expected `destructive`, got `secondary`

## Tokens

Input 144,564 · output 4,316
