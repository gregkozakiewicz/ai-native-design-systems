# Rewritten button rules got 948 of 960 answers right on 10 models

Without test buttons named as examples, rewritten button rules got 948 of 960 answers right on 10 models; the old rules partly matched labels.

**Wheel:** `wheels/004-new-button-rules/` · **Runs dated:** 8 and 9 October 2026 · **Status:** answered

| 98.8% | 5 of 10 | 69 of 783 | 27 of 27 |
| --- | --- | --- | --- |
| of answers matched the designer's, 948 of 960, with run 3's rewritten rules on 10 models | models gave the designer's answer every time in run 3, 96 of 96 | answers missed on 9 models by the old rules without their examples, up from 27 of 783 with them | answers wrong on 'Not now' on a notifications prompt without the example "not now" |

## The question

Do the rewritten button rules, with no examples that name test buttons, give the designer's answers on the same 10 models? Each answer is one button variant: primary, secondary, ghost, destructive, or none. In [wheel 003](../003-three-missing-rules/post.md), 3 amended rules raised the misses from 32 to 40 of 870. The old rules also gave test button labels as examples, such as "skip, not now, maybe later". A model could match a label instead of reading the situation.

**In scope:** the rewritten rules on wheel 002's 10 models in 3 runs, with fixes between runs, and a check of the old rules without examples. The scenarios are wheel 001's, with 6 described more fully and 3 added.
**Out of scope:** wheel 002's other 2 information levels, names only and human written documentation; other components; buttons the rules were not written for.

## The answer

Yes. In the last run, the rewritten rules got 948 of 960 answers right, which is 98.8%. The old rules got 838 of 870 in wheel 002. 5 of the 10 models were right every time. We count more than 95% of answers right as 'yes'. We set that bar after the runs, and run 3 did not meet the stricter one we set before them, which allowed 10 misses.

The check showed that the old rules partly relied on their examples. Without them, 9 models missed 69 of 783 answers, against 27 of 783 with them in wheel 002.

**Based on:** one component, 10 models, and 32 scenarios that the rules were developed against. It does not show that the rules work on buttons they were not written for.

## One example

'Learn more' on a promotional banner, as seen by every model. The answers are Claude Opus 5.5's. In the answers, HR1 to HR12 are the rules' hard rules, and P1 to P5 are the steps that decide which rule wins.

**The task**

```
Context: A promotional banner on a dashboard. The button opens a page with more information about a new feature.
Button label: "Learn more"

Which variant should this button use?
```

**With the old rules, without their examples**

```
primary

Under HR1 a banner is its own view, and 'Learn more' is the one forward-moving action that banner recommends (P4), so it is primary rather than a side task under HR11.
```

The old side-task rule, HR11, had listed "learn more" as an example. With the example, Opus chose ghost in 3 of 3 tries in wheel 001. Without it, Opus treated the banner as its own view and chose primary in 3 of 3 tries.

**With the rewritten rules**

```
ghost

HR11 (applied at P3, before P4's only-action rule): a button that leads to further information rather than completing the current task is ghost.
```

The rewritten HR11 covers a button that "leads to further information", so Opus chose ghost, the designer's answer, in 3 of 3 tries. All 10 models did the same, in 30 of 30 answers. Full output: `runs/2026-10-09-claude-opus-5-5-run3/`, and without the examples, `runs/2026-10-08-claude-opus-5-5-check/`.

## What we found

### The rewritten rules got 948 of 960 answers right in run 3

The rules are the design system text given to each model. Wheel 004 ran the rewritten rules 3 times, fixing the wording between runs. Run 3's rules are the ones the designer kept.

| Rules | Answers missed |
| --- | --- |
| Old rules, wheel 002, 10 models | 32 of 870 |
| Old rules without their examples, 9 models | 69 of 783 |
| Rewritten rules, run 1 | 13 of 930 |
| Rewritten rules, run 2 | 10 of 930 |
| Rewritten rules, run 3 | 12 of 960 |

| Model | Old rules, wheel 002 | Old rules without the test button names, 9 models | Rewritten rules, run 3 |
| --- | --- | --- | --- |
| Claude Fable 5.1 | 87 of 87 (100%) | 83 of 87 (95.4%) | 96 of 96 (100%) |
| Claude Opus 5.5 | 87 of 87 (100%) | 81 of 87 (93.1%) | 95 of 96 (99.0%) |
| Claude Sonnet 5.5 | 87 of 87 (100%) | 84 of 87 (96.6%) | 96 of 96 (100%) |
| Claude Haiku 4.5 | 84 of 87 (96.6%) | 80 of 87 (92.0%) | 90 of 96 (93.8%) |
| GPT-6 Astra | 84 of 87 (96.6%) | 84 of 87 (96.6%) | 96 of 96 (100%) |
| GPT-5.6 sol | 80 of 87 (92.0%) | 75 of 87 (86.2%) | 96 of 96 (100%) |
| Grok 4.7 | 83 of 87 (95.4%) | 77 of 87 (88.5%) | 95 of 96 (99.0%) |
| Grok 4.3 | 82 of 87 (94.3%) | 78 of 87 (89.7%) | 93 of 96 (96.9%) |
| Gemini 3.1 Pro | 82 of 87 (94.3%) | not run | 95 of 96 (99.0%) |
| Gemini 3.8 Flash | 82 of 87 (94.3%) | 72 of 87 (82.8%) | 96 of 96 (100%) |

5 of the 10 models scored 96 of 96 in run 3. The old rules named some of the test buttons in their wording, such as "log out", "archive" and "not now". Without those words, 9 models missed 69 of 783 answers instead of 27. Naming the test buttons is like writing a separate rule for each scenario, which we do not want. Run 3's rules name none of them.

Of the 3 gaps that [wheel 002](../002-other-models/post.md) found, one is closed, and the other 2 each still miss on one model:

| Question the old rules did not answer | Misses in wheel 002 | Misses in run 3 |
| --- | --- | --- |
| When is a reversible action optional? 'Archive project' on a settings page, 'Log out' in an account menu, 'Export CSV' above a data table | 22 of 90 | 3 of 90, all Grok 4.3 |
| Which rule wins when a button fits 2? 'Not now' on a notifications prompt, 'Stay on Free' on a pricing screen | 7 of 60 | 0 of 60 |
| Does retyping count as undoing? 'Discard changes' in a dialog about unsaved changes | 3 of 30 | 3 of 30, all Claude Haiku 4.5 |

Run 3 used 32 scenarios, so its total is not an exact comparison with wheel 002's 29. A model's reason is one line it writes with its answer, not a full record of what it weighed. Runs: `runs/`, one folder per model and run.

### The old rules missed 69 of 783 answers without their examples, against 27 with them

The check gave 9 models wheel 002's rules with the examples taken out and the rules renamed, on the same 29 scenarios. It ran without Gemini 3.1 Pro, to stay within that model's daily limit. 12 scenarios had button labels that appeared as examples in the old rules.

| Buttons | Misses in wheel 002, same 9 models | Misses without the examples |
| --- | --- | --- |
| 'Not now' on a notifications prompt | 3 of 27 | 27 of 27 |
| 'Log out' in an account menu | 6 of 27 | 10 of 27 |
| 'Learn more' on a promotional banner | 0 of 27 | 8 of 27 |
| 'Add file' next to 'Send' in a chat composer | 0 of 27 | 2 of 27 |
| The other 8 buttons named in examples | 10 of 216 | 10 of 216 |
| The 17 buttons not named in examples | 8 of 459 | 12 of 459 |
| All 29 scenarios | 27 of 783 | 69 of 783 |

On 'Not now' on a notifications prompt, every model used the rule for dismissing something or for backing out, and chose secondary. The old skip rule had listed "not now" as an example.

The models' reasons cite the new rule names, and we have not tested the names on their own. Runs: the folders ending in `-check`.

### Runs 2 and 3 each fixed one problem, and run 3's fix moved another button

| Run | What changed | What it fixed | What else changed |
| --- | --- | --- | --- |
| 2 | P5: Emphasis became one test instead of 2, and HR11, the side-task rule, narrowed | 'Log out' in an account menu, from 4 misses to 0 | GPT-6 Astra called 'Reset to defaults' on a settings page secondary in 2 of 3 tries, citing HR10, which run 2 did not change |
| 3 | A reset is destructive only when the user would lose a large configuration | both reset scenarios, right in 60 of 60 answers | 3 models each called 'Revert to original' in an image editor destructive once |

Run 3's change came from the designer. A reset loses the values the user chose, not the settings themselves. With a few settings, the user can set them again, but with 40 custom rules, they would have to rebuild them from memory. So the rules now ask how much would be lost.

The scenario for 'Revert to original' in an image editor says "several crops and filters", but not how many. So 3 models read it as a large loss, citing the new word "configuration" in HR2.

A scenario splits when the 10 models' most common answers differ. In run 3, no scenario that all 10 models agreed on in wheel 002 split. Run 2's split on 'Reset to defaults' on a settings page may not come from its change. GPT-6 Astra's reasons cite HR10, which run 2 did not touch.

### Where it failed

These went wrong, in the answers and in our setup:

- Haiku 4.5 missed the same 6 answers in every run, on 'Discard changes' in a dialog and 'Archive project' alone on a settings page
- Grok 4.3 called 'Export CSV' above a data table or 'Archive project' on a settings page ghost in 2 or 3 answers a run
- run 2 split 'Reset to defaults' on a settings page, which the criteria we set before the runs count as 'no'
- a trial of the 2 reset scenarios before run 3 saved no Gemini answers, because the Google account ran out of prepaid credit
- the Grok runs in run 3 stopped when the xAI account ran out of prepaid credit, and carried on after a top-up
- before run 1, Claude agents reviewed the rules against every scenario to find other ways a model could read them
- those reviews used Claude models only, and a risk they found for 'Export CSV' above a data table was left in

## What to do with this

1. Keep your test buttons' labels out of your rules' examples, so a good score cannot come from matching words.
2. If a button can be read 2 ways, put what the answer depends on into the rule, such as how much a reset loses.
3. Run every rule change against all your scenarios, because run 3's fix for the resets moved 'Revert to original' in an image editor.
4. Test your rules on a small model as well as large ones, because Claude Haiku 4.5 missed the same 6 answers in every run.

Run 3's rules now replace the 12 rules in [the system's button rules](../../system/button-variant.md), with the limits above written beside them.

## What this does not show

The runs have these limits:

- one component and 10 models
- the rules were developed against these 32 scenarios over 4 wheels, so we cannot say how they do on other buttons
- the correct answers are one designer's judgement
- the check changed the examples and the rule names together
- 6 scenarios gained more description than in wheel 002, so run 3 is not an exact rerun of wheel 002
- the reviews of the rules before run 1 used Claude models only

## Details

**How we tested**

| Setting | Value |
| --- | --- |
| Models | wheel 002's 10, from Anthropic, OpenAI, Google, and xAI, at the same settings, each through its own application programming interface (API) |
| Information levels | rules only: the rewritten rules in runs 1 to 3, and the old rules without their examples in the check |
| Scenarios | wheel 001's 29, with 6 described more fully; 2 added in run 1 and one more in run 3, making 32 |
| Repeats | 3 per scenario per model, each a fresh conversation |
| Scoring | wheel 001's script, against the designer's answers |
| Dates | the check on 8 October 2026, runs 1 to 3 on 9 October 2026 |
| Cost | about €11.73 in API credit, pay as you go, with no reruns. Run 1 cost €3.10, the check €2.31, run 2 €3.00, and run 3 €3.32, with its trial of the 2 reset scenarios. We worked it out from the tokens each model used and each company's published prices |

We wrote the question and the success criteria before run 1, and what we expected before each run. After the runs, we changed the bar for 'yes' to more than 95% of answers right. The bar before the runs allowed 10 misses of 930 and needed every model at 90 or more of 93.

**Reproduce it**

- wheel: `wheels/004-new-button-rules/`
- raw output: `wheels/004-new-button-rules/runs/`, one folder per model and run
- rules, scenarios, and runner: `wheels/004-new-button-rules/experiment/`

**Questions this raises**

- do the rules work on buttons they were never written for
- does HR11, the side-task rule, need a tighter limit for models that read it widely
- do the new rule names change answers on their own

**Changes to this post**

- 9 October 2026: first version
