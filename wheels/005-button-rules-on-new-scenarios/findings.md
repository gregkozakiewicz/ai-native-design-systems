# Findings

## Summary

By the success criteria written before the run, the answer is no: the 10 models gave the designer's answer in 381 of 720 answers, 52.9%. The bar for 'yes' was 685.

The rules themselves held. The models gave the answer the rules give in 711 of 720 answers, 98.8%, on 24 buttons the rules were never tuned on. That matches wheel 004's 948 of 960.

The gap is between the designer and the rules, not between the rules and the models. On the 11 scenarios where the designer's answer differs from what the rules give, every model followed the rules in every repeat: 330 of 330 answers.

## Evidence

Runs are in `runs/`, one folder per model, dated 13 October 2026, each with `C.jsonl` and `summary.md`. The Haiku 5.5 baseline is in the folder ending in `-baseline`.

### Claude Haiku 5.5 baseline on wheel 004's scenarios

Claude Haiku 5.5 gave the expected answer in 96 of 96 answers on wheel 004's 32 scenarios with run 3's rules. Claude Haiku 4.5 scored 90 of 96 on the same run. Its wheel 005 result is reported with the other 9.

### Each model against the designer and against the rules

| Model | Designer's answers | Answers the rules give |
| --- | --- | --- |
| Claude Fable 5.1, low effort | 39 of 72 | 72 of 72 |
| Claude Opus 5.5 | 39 of 72 | 72 of 72 |
| Claude Sonnet 5.5 | 39 of 72 | 72 of 72 |
| Claude Haiku 5.5 | 37 of 72 | 70 of 72 |
| GPT-6 Astra | 37 of 72 | 70 of 72 |
| GPT-5.6 sol | 39 of 72 | 72 of 72 |
| Gemini 3.1 Pro | 39 of 72 | 72 of 72 |
| Gemini 3.8 Flash | 38 of 72 | 71 of 72 |
| Grok 4.7 | 38 of 72 | 71 of 72 |
| Grok 4.3 | 36 of 72 | 69 of 72 |
| All 10 | 381 of 720 | 711 of 720 |

### Where the designer and the rules differ, the models followed the rules

| Button | Designer | Rules | Models |
| --- | --- | --- | --- |
| 'Delete' in an email inbox, emails restorable for 30 days | destructive | secondary | secondary, 30 of 30 |
| 'Keep subscription' in a cancel dialog | ghost | secondary | secondary, 30 of 30 |
| 'Done' on a read-only fitness summary | primary | secondary | secondary, 30 of 30 |
| 'Got it' on a traffic banner | ghost | secondary | secondary, 30 of 30 |
| 'Save job' on each of 20 job adverts | primary | ghost | ghost, 30 of 30 |
| 'Add to shopping list' on each of 30 recipe cards | secondary | ghost | ghost, 30 of 30 |
| 'Continue without insurance' next to 'Add insurance' | primary | secondary | secondary, 30 of 30 |
| 'Undo changes' in a calendar event form | secondary | ghost | ghost, 30 of 30 |
| 'Add notes' in a slide editor | secondary | ghost | ghost, 30 of 30 |
| 'Save for later' at a photo printing checkout | secondary | ghost | ghost, 30 of 30 |
| 'Copy link' in a share dialog | ghost | secondary | secondary, 30 of 30 |

### The 9 answers that missed the rules

| Button | Rules | Models' other answer |
| --- | --- | --- |
| 'Add to wishlist' on a product page | ghost | secondary in 4 of 30 |
| 'Assign to me' in a support ticket header | secondary | ghost in 3 of 30 |
| 'Send test email' on email settings | ghost | secondary in 2 of 30 |

All 3 are on the line between secondary and ghost. 2 of them are among the 4 scenarios the designer added for that reason.

## What the data does not show

- whether the designer's answers or the rules are the better design; that needs other designers' answers, which the designer judgement portal is collecting
- how the rules do on buttons that are not plain buttons; 4 such scenarios were removed before the run
- effort settings: Claude Haiku 5.5 ran at its default, which is medium, as Claude Opus 5.5 and Claude Sonnet 5.5 did

## Cost

About €2.24 of pay-as-you-go API credit for 816 answers, including the Haiku 5.5 baseline. See `SPENDING.md`.
