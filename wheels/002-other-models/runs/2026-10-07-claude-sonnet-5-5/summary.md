# Results

Model: claude-sonnet-5-5 · effort: default · 261 answers

## Headline

| Level | Accuracy | Consistency | Over-flagging |
|---|---|---|---|
| A · names only | 31% (27/87) | 100% | 68% (57/84) |
| B · human docs | 76% (66/87) | 100% | 0% (0/84) |
| C · machine rules | 100% (87/87) | 100% | 0% (0/84) |

Accuracy: share of answers matching the key. Consistency: share of scenarios where all runs agreed. Over-flagging: answered `none` when a variant was expected.

## By category

| Category | A · names only | B · human docs | C · machine rules |
|---|---|---|---|
| Easy | 100% | 100% | 100% |
| Context | 14% | 86% | 100% |
| Traps | 0% | 25% | 100% |
| Conflicts | 50% | 100% | 100% |
| Interaction & tools | 33% | 67% | 100% |
| Matched pairs | 0% | 67% | 100% |

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
| #16 → #24 | B | 0 | 0 | 3 | 0 |
| #20 → #25 | B | 0 | 3 | 0 | 0 |
| #15 → #26 | B | 0 | 0 | 3 | 0 |
| #11 → #27 | B | 0 | 0 | 0 | 3 |
| #10 → #28 | B | 3 | 0 | 0 | 0 |
| #13 → #29 | B | 0 | 0 | 3 | 0 |
| #16 → #24 | C | 3 | 0 | 0 | 0 |
| #20 → #25 | C | 3 | 0 | 0 | 0 |
| #15 → #26 | C | 3 | 0 | 0 | 0 |
| #11 → #27 | C | 3 | 0 | 0 | 0 |
| #10 → #28 | C | 3 | 0 | 0 | 0 |
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
- #25 "Stay on Free": wrong 3×, expected `secondary`, got `ghost`
- #23 "Send feedback": wrong 3×, expected `ghost`, got `secondary`
- #16 "Try again": wrong 3×, expected `primary`, got `secondary`
- #15 "Reset to defaults": wrong 3×, expected `ghost`, got `secondary`
- #13 "Log out": wrong 3×, expected `secondary`, got `ghost`

**C · machine rules**

- all correct

## Tokens

Input 265,767 · output 18,179
