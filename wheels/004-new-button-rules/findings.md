# Findings

## Summary

Yes. In 3 runs, the rewritten rules missed 10 to 13 answers per run, of 930 to 960. The original rules missed 32 of 870 in wheel 002, and wheel 003's missed 40. The designer kept run 3's rules, which got 948 of 960 answers right, 98.8%. 5 of the 10 models scored 96 of 96 in run 3.

After the runs, the designer set the bar for "yes" at more than 95% of answers right. By the success criteria written before the runs, no run met every condition for "yes":

- Haiku 4.5 missed the same 6 answers in every run, and "yes" needed every model at 90 or more of 93
- in runs 1 and 3, 8 of 10 models got both 'Archive project' scenarios right, and "yes" needed 9
- run 2 split 'Reset to defaults', which the criteria count as "no"

The check run shows that the earlier wheels partly relied on matching words. Without the examples in the rules, 9 models missed 57 of 324 answers on the 12 scenarios whose labels had been examples. In wheel 002 they missed 19. Most of the rise was 'Not now', which every model got wrong every time.

## Evidence

Runs are in `runs/`, one folder per model, each with a `summary.md`. Run 1's folders are dated 9 October 2026. Runs 2 and 3 are dated the same day and end in `-run2` and `-run3`. The check run's folders are dated 8 October 2026 and end in `-check`. Wheel 002's and wheel 003's figures are their results with rules.

### Run 1: the rewritten rules cut the misses to 13 of 930

| Model | Wheel 002 | Wheel 003 | Wheel 004 |
| --- | --- | --- | --- |
| Claude Fable 5.1 | 87 of 87 | 85 of 87 | 90 of 93 |
| Claude Opus 5.5 | 87 of 87 | 81 of 87 | 93 of 93 |
| Claude Sonnet 5.5 | 87 of 87 | 87 of 87 | 92 of 93 |
| Claude Haiku 4.5 | 84 of 87 | 86 of 87 | 87 of 93 |
| GPT-6 Astra | 84 of 87 | 76 of 87 | 93 of 93 |
| GPT-5.6 sol | 80 of 87 | 83 of 87 | 93 of 93 |
| Grok 4.7 | 83 of 87 | 79 of 87 | 93 of 93 |
| Grok 4.3 | 82 of 87 | 85 of 87 | 90 of 93 |
| Gemini 3.1 Pro | 82 of 87 | 82 of 87 | 93 of 93 |
| Gemini 3.8 Flash | 82 of 87 | 86 of 87 | 93 of 93 |

Taking each model's most common answer, all 10 models agreed on 27 of 31 scenarios, up from 23 of 29 in wheel 002. No scenario on which all 10 agreed in wheel 002 split. A reworded pair is a second scenario that tests the same rule in different words. None of the 180 reworded pairs broke.

### 2 of wheel 002's 3 gaps closed, and the third misses only on Haiku 4.5

| Gap found in wheel 002 | Misses in wheel 002 | Misses in wheel 004 |
| --- | --- | --- |
| When a reversible action is optional: 'Archive project', 'Log out' and 'Export CSV' | 22 of 90 | 7 of 90 |
| Which rule wins: 'Not now' and 'Stay on Free' | 7 of 60 | 0 of 60 |
| Whether retyping counts as undoing: 'Discard changes' | 3 of 30 | 3 of 30, all Haiku 4.5 |

'Not now' on the notifications prompt missed 0 of 30, against 27 of 27 in the check run. Its new pair, 'No thanks', which declines for good, also missed 0 of 30. All 10 models told postponing apart from declining.

The 3 scenarios that split in wheel 003 were right on every model: 'New invoice', 'Reset to defaults' and 'Revert to original'. So were 'Stay on Free', 'Learn more' and 'Add file'.

### The 13 misses come from 4 models, each for its own reason

Haiku 4.5 missed 6:

- 'Discard changes' in a dialog about unsaved changes, secondary in 3 of 3: it said "all it removes are choices the user can make again"
- 'Archive project' alone, destructive in 2 and secondary in 1: its reasons argue both ways, such as "HR2 requires destructive ... but HR3 and NR2 override this"

Haiku 4.5 also missed 'Discard changes' in wheel 002, 3 of 3, and in wheel 003, 1 of 3.

Fable 5.1 missed 3 and Sonnet 5.5 missed one, all on 'Log out' in an account menu, answered ghost. They used only the first half of P5: "the user did not come to this view to log out, so ghost". P5 goes on "or may reasonably do it there". One of Fable's reasons ends "correcting: variant should be secondary", but its answer was ghost.

Grok 4.3 missed 3: 'Export CSV' ghost in 2 of 3, and 'Archive project' below 'Save changes' ghost in 1 of 3. Each cites HR11's new words: "adds something optional rather than completing the task". The check before the run flagged this risk for 'Export CSV', and the designer chose to leave it.

### Without examples, misses on the 12 matched scenarios rose from 19 to 57 of 324

The check run used wheel 002's rules with only the examples taken out, on wheel 001's 29 scenarios. It ran on 9 models, without Gemini 3.1 Pro. The 12 matched scenarios are the ones whose button labels had appeared as examples in the rules.

| Scenario | Misses in wheel 002, same 9 models | Misses in the check run |
| --- | --- | --- |
| 'Not now' on the notifications prompt | 3 of 27 | 27 of 27 |
| 'Log out' in an account menu | 6 of 27 | 10 of 27 |
| 'Learn more' on a promotional banner | 0 of 27 | 8 of 27 |
| 'Add file' next to 'Send' | 0 of 27 | 2 of 27 |
| The other 8 matched scenarios | 10 of 216 | 10 of 216 |

The rise of 38 is above the 20 that the README set for answering "the scores relied on matching words". On the other 17 scenarios, misses rose from 8 to 12 of 459, within the allowance of 6.

On 'Not now', the models used the dismiss and back-out rules instead. Gemini 3.8 Flash gave this reason: "HR5: a button that only dismisses something is secondary". In wheel 002, the skip rule listed "not now" as an example. On 'Learn more', they used HR1's view rule. Opus 5.5 gave this reason: "Under HR1 a banner is its own view, and 'Learn more' is the one forward-moving action that banner recommends".

8 of the 9 models scored lower than in wheel 002, and GPT-6 Astra did not change. Gemini 3.8 Flash lost 10 of 87, Opus 5.5 and Grok 4.7 lost 6 each, and GPT-5.6 sol lost 5. 30 of 162 reworded pairs broke, against 7 of 162 in wheel 002. 27 of the 30 were 'Skip for now' right and 'Not now' wrong.

### Run 2: 2 wording fixes cut the misses to 10 of 930, but split 'Reset to defaults'

Run 2 changed 2 rules after run 1. P5 became one test, and HR11's "adds something optional" became "adds an optional extra to the thing the user is creating".

| Model | Run 1 | Run 2 | Run 3 |
| --- | --- | --- | --- |
| Claude Fable 5.1 | 90 of 93 | 93 of 93 | 96 of 96 |
| Claude Opus 5.5 | 93 of 93 | 93 of 93 | 95 of 96 |
| Claude Sonnet 5.5 | 92 of 93 | 93 of 93 | 96 of 96 |
| Claude Haiku 4.5 | 87 of 93 | 87 of 93 | 90 of 96 |
| GPT-6 Astra | 93 of 93 | 91 of 93 | 96 of 96 |
| GPT-5.6 sol | 93 of 93 | 93 of 93 | 96 of 96 |
| Grok 4.7 | 93 of 93 | 93 of 93 | 95 of 96 |
| Grok 4.3 | 90 of 93 | 91 of 93 | 93 of 96 |
| Gemini 3.1 Pro | 93 of 93 | 93 of 93 | 95 of 96 |
| Gemini 3.8 Flash | 93 of 93 | 93 of 93 | 96 of 96 |

The P5 fix worked: 'Log out' in an account menu went from 4 misses to 0. The HR11 fix worked for 'Archive project' below 'Save changes', but Grok 4.3 still called 'Export CSV' ghost in 2 of 3 tries: "export adds an optional extra".

GPT-6 Astra called 'Reset to defaults' on a profile settings page secondary in 2 of 3 tries. In run 1 it had answered ghost 3 of 3. Its reason: "HR10's rarely-needed condition is not established". The scenario never said the reset is rarely needed. With its most common answer now secondary, the 10 models split 9 to 1 on a scenario they had all agreed on.

### Run 3: a reset is destructive only when much is lost, and both resets came right

After this miss, the designer decided that a reset is destructive when the user would lose a large configuration. It is not destructive when they lose a few settings. Run 3 rewrote HR2, HR3 and HR10 to say so, and section 1's meaning of destructive with them. It changed the reset scenario to a page with 4 settings that most people never reset. It also added a reset of 40 custom rules, answered destructive.

Run 3 missed 12 of 960. Both reset scenarios were right on every model, every time: 30 of 30 ghost for 4 settings, and 30 of 30 destructive for 40 custom rules. 'Not now' and 'No thanks' were right on all 10 models. No scenario on which all 10 agreed in wheel 002 split, and all 10 agreed on 29 of 32 scenarios.

The new wording moved one scenario it was not aimed at. Opus 5.5, Gemini 3.1 Pro and Grok 4.7 each called 'Revert to original' in an image editor destructive once in 3 tries. Grok 4.7 gave this reason: "reverting permanently discards the crop and filter configuration the user created, which would have to be recreated from memory". The scenario says "several crops and filters", but not how many. Each model still answered ghost in 2 of 3 tries, so no scenario split.

The other misses in run 3 were Haiku 4.5's 6 and Grok 4.3's 3. Grok 4.3 called 'Export CSV' ghost once and 'Archive project' ghost twice.

### What we expected and what happened

Before run 1 and the check run, the hypothesis expected these:

- 10 or fewer misses in the main run: there were 13
- 'Archive project', 'Log out' and 'Export CSV' to stay right: they missed 7 of 90
- 'Not now' and 'Stay on Free' to come right: they did, 0 of 60
- 'Discard changes' to come right: Haiku 4.5 still missed it 3 of 3
- 'Reset to defaults', 'Revert to original' and 'New invoice' to be right on every model: they were
- most remaining misses on the 2 new scenarios: 3 of the 13 were, all from Haiku 4.5, and 'No thanks' had none
- the check run to rise a little, to between 35 and 45 of 870: it rose from 27 to 69 of 783, on 9 models
- the check run's rise to fall on 'Not now', 'Skip for now', 'Add file', 'Send feedback' and 'Learn more': it fell on 'Not now', 'Learn more' and 'Add file', and 'Log out' rose too

Of run 1's 4 things that would surprise us, one happened in full and one in part:

- more than 20 extra misses on the matched scenarios in the check run: there were 38
- a rule moving a scenario it was not aimed at: HR11's new words moved 'Archive project' once, on Grok 4.3
- 'Archive project' alone called secondary by most models: one answer of 30
- 'Not now' and 'No thanks' getting the same answer: no model did this

Before run 2, we expected the misses to fall to about 6. They fell to 10. 'Log out' came right, as expected, and Haiku 4.5's 6 stayed. Grok 4.3's 'Export CSV' did not come right. The surprise we listed, a scenario right in run 1 missing in run 2, happened on 'Reset to defaults'.

Before run 3, we expected both reset scenarios to be right on almost every model, and they were right on every model. The surprise we listed, 'Revert to original' changing answer, happened on 3 models, once each.

## Failure modes seen

- one of Fable's answers disagrees with its own reason, which concludes secondary while the answer is ghost
- Haiku's reasons on 'Archive project' alone argue for 2 answers in one sentence
- the check run changed 2 things at once, the examples and the names; the reasons quote what the rules say, not their names, but we have not tested the names on their own
- 5 of the 29 scenarios have more description than in wheel 002, so the main run is not an exact rerun of wheel 002
- the 2 checks before the run used Claude models only, and the risk they left for 'Export CSV' caused 2 misses
- run 3's Gemini and Grok answers stopped twice when the Google and xAI accounts ran out of prepaid credit; after top-ups, the runs carried on where they stopped
- in run 3, the word "configuration" in HR2 moved 'Revert to original' on 3 models

## Cost

About €11.73 of pay-as-you-go API credit for the whole wheel. `tools/spending.py` works it out from the tokens in the raw runs and each company's published prices. Grok's costs are the charges xAI recorded.

| Run | Answers | Cost |
| --- | --- | --- |
| Run 1 | 930 | €3.10 |
| Check run | 783 | €2.31 |
| Run 2 | 930 | €3.00 |
| Run 3, probe of the 2 reset scenarios | 48 | €0.19 |
| Run 3 | 960 | €3.12 |

There were no reruns. The checks before runs 1 and 2 ran as Claude Code agents, not on API credit.

## Open questions raised

These go to `../../QUESTIONS.md`.

- why Haiku 4.5 reads a typed report as "choices the user can make again", and whether HR2 needs to say what content is
- whether P5's 2 halves should be one test, so a model cannot stop at "the user did not come to this view"
- whether HR11's "adds something optional" needs a limit, since it caught 'Export CSV' and 'Archive project' on Grok 4.3
- whether the new names HR, NR and P change answers on their own
