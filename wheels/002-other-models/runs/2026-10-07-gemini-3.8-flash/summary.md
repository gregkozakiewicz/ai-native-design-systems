# Results

Model: gemini-3.8-flash · effort: default · 261 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 62% (54/87) | 100% | 0% (0/84) |
| B · human docs | 69% (60/87) | 93% | 0% (0/84) |
| C · machine rules | 94% (82/87) | 97% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 100% | 100% | 100% |
| Context | 57% | 76% | 100% |
| Traps | 50% | 42% | 58% |
| Conflicts | 100% | 100% | 100% |
| Interaction & tools | 0% | 0% | 100% |
| Matched pairs | 50% | 67% | 100% |

## Matched pairs

Original scenario vs. a rewording that tests the same rule. 'Original only' means the agent matched words, not the rule.

| Pair | Level | Both | Original only | Pair only | Neither |
|---|---|---|---|---|---|
| #16 → #24 | A | 3 | 0 | 0 | 0 |
| #20 → #25 | A | 3 | 0 | 0 | 0 |
| #15 → #26 | A | 0 | 0 | 0 | 3 |
| #11 → #27 | A | 0 | 0 | 0 | 3 |
| #10 → #28 | A | 0 | 3 | 0 | 0 |
| #13 → #29 | A | 0 | 0 | 3 | 0 |
| #16 → #24 | B | 0 | 0 | 3 | 0 |
| #20 → #25 | B | 3 | 0 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 3 | 0 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #10 → #28 | B | 0 | 3 | 0 | 0 |
| #13 → #29 | B | 2 | 0 | 1 | 0 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 3 | 0 | 0 | 0 |
| #13 → #29 | C | 0 | 0 | 3 | 0 |

## Hardest scenarios per level

**A · names only**

- #28 "Not now": wrong 3×, expected `ghost`, got `secondary`
- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #26 "Revert to original": wrong 3×, expected `ghost`, got `destructive`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `secondary`
- #22 "Add file": wrong 3×, expected `ghost`, got `secondary`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`

**B · human docs**

- #28 "Not now": wrong 3×, expected `ghost`, got `secondary`
- #27 "Dismiss": wrong 3×, expected `secondary`, got `ghost`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `secondary`
- #22 "Add file": wrong 3×, expected `ghost`, got `secondary`
- #21 "Hold to record": wrong 3×, expected `none`, got `primary`
- #16 "Try again": wrong 3×, expected `primary`, got `secondary`

**C · machine rules**

- #13 "Log out": wrong 3×, expected `secondary`, got `ghost`
- #14 "Archive project": wrong 2×, expected `secondary`, got `ghost`

## Tokens

Input 0 · output 0
