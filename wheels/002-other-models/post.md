# The same 12 button rules work on 10 models from 4 companies

With rules, 10 models chose the correct button variant in 80 to 87 of 87 answers, against 60 to 73 with human written documentation.

**Wheel:** `wheels/002-other-models/` · **Runs dated:** 7 and 8 October 2026 · **Status:** answered

| 10 of 10 | 23 of 29 | 4 of 29 | 32 of 870 |
| --- | --- | --- | --- |
| models scored 80 or more of 87 with the rules | scenarios where all 10 models gave the same answer, with rules | scenarios where all 10 agreed with variant names only | answers with rules that missed, all from 3 gaps in the rules |

## The question

Does the button variant rule set from [wheel 001](../001-button-variant/post.md) guide models other than Claude Opus 5.5 as well as it guided Opus? Wheel 001 took Opus 5.5 from 54 of 87 to 87 of 87 with 12 written rules. If that holds only for Opus, the rules are a prompt tuned to one model. If it holds across companies, the rules belong to the design system.

**In scope:** the same 29 scenarios, 3 information levels, and correct answers as wheel 001, on 10 models.
**Out of scope:** changing the rules to suit a model; tuning per model; other components.

## The answer

Yes. The rules had the same impact. On every model, written rules beat human written documentation by 9 to 24 points. Every model scored at least 80 of 87 with them.

The rules also moved the models towards each other. With rules, all 10 gave the same answer on 23 of 29 scenarios; with names only, on 4 of 29. The 6 scenarios where they split are the 3 places the rules leave a reading open, and nothing else.

**Based on:** one component and 10 models. We do not go into details about reasoning settings for each model.

## One example

Scenario 13, as seen by every model. The answers are GPT-6 Astra's.

**The task**

```
Context: An account menu. The button signs the user out; they can sign in again at any time.
Button label: "Log out"

Which variant should this button use?
```

**Without rules** (level A, the 4 variant names and nothing else)

```
none

The design system reference provides no usage guidelines that assign a variant to a reversible sign-out action.
```

Given no guidance, GPT-6 Astra refused to guess, on 72 of 84 scenarios. Opus, given the same nothing, guessed from convention and called this ghost.

**With rules** (level C)

```
secondary

H3 rules out destructive because signing out is reversible, and the emphasis guideline makes this real choice secondary.
```

With rules, GPT-6 Astra reached the designer's answer in 3 of 3 repeats, citing the same rules Opus cites. Full output: `runs/2026-10-07-gpt-6-astra/`.

## What we found

### Rules beat human written documentation on all 10 models, by 9 to 24 points

Each model answered 29 scenarios, 3 times each, at 3 levels. Between levels, only the design system text given to the model changed: names only, human written documentation, or rules.

| Model | Tier | Rules | Human written documentation | Names only |
| --- | --- | --- | --- | --- |
| Claude Fable 5.1 | flagship | 87 of 87 | 70 of 87 | 48 of 87 |
| Claude Opus 5.5 | large | 87 of 87 | 63 of 87 | 54 of 87 |
| Claude Sonnet 5.5 | mid | 87 of 87 | 66 of 87 | 27 of 87 |
| Claude Haiku 4.5 | small | 84 of 87 | 68 of 87 | 54 of 87 |
| GPT-6 Astra | flagship | 84 of 87 | 63 of 87 | 15 of 87 |
| GPT-5.6 sol | previous flagship | 80 of 87 | 62 of 87 | 19 of 87 |
| Grok 4.7 | flagship | 83 of 87 | 71 of 87 | 16 of 87 |
| Grok 4.3 | older | 82 of 87 | 73 of 87 | 13 of 87 |
| Gemini 3.1 Pro | top Pro model our account can reach | 82 of 87 | 65 of 87 | 53 of 87 |
| Gemini 3.8 Flash | small | 82 of 87 | 60 of 87 | 54 of 87 |

Interesting note: the older Grok 4.3 did best on human written documentation, 9 points behind the rules. On every other model, including Grok 4.7, it was 16 to 24 points behind.

### Rules aligned the models with each other, as well as with the designer's answers

We counted the scenarios where all 10 models gave the same answer.

| Level | Scenarios where all 10 models agree |
| --- | --- |
| Names only | 4 of 29 |
| Human written documentation | 17 of 29 |
| Rules | 23 of 29 |

### All 32 misses come from 3 gaps in the rules

With rules, the models missed 32 of 870 answers. Every miss came from one of 3 questions the rules do not answer. In each case, the model's one-line reason shows which rule it followed.

| The question the rules do not answer | Buttons affected | Misses |
| --- | --- | --- |
| Is a reversible action a real choice (secondary) or an optional extra (ghost)? | 'Archive project' on a settings page, 'Log out' in an account menu, 'Export CSV' above a data table | 22 of 32 |
| When a button fits 2 rules, which one wins? | 'Not now' on a prompt to turn on notifications, 'Stay on Free' on a pricing screen | 7 of 32 |
| Does redoing the work by hand count as undoing it? | 'Discard changes' in a dialog about unsaved changes | 3 of 32 |

#### The rules do not say when a reversible action is optional

'Archive project' on a project settings page can be undone, so it is not destructive. No other rule fits it, so the last step in the order the rules are checked decides:

- a real choice the user may take is secondary
- an optional action that is rarely needed is ghost

The designer's answer is secondary. The models split 5 to 5: half read archiving as optional and rarely needed, and chose ghost. 'Log out' in an account menu and 'Export CSV' above a data table missed the same way.

#### 'Not now' and 'Stay on Free' each fit 2 rules

'Not now' on a prompt to turn on notifications fits 2 rules:

- the skip rule (H12) says a button that skips the task, such as 'Skip' or 'Not now', is ghost
- the close rule (H5) says a button that only closes something is secondary

Both rules are at the same step in the order the rules are checked, so nothing says which one wins. The designer's answer is ghost. GPT-6 Astra followed the close rule and chose secondary in 3 of 3 tries. Its reason was "this button only dismisses the prompt".

'Stay on Free' on a pricing screen also fits 2 rules:

- the skip rule (H12) says it is ghost, because it skips the upgrade
- the equal-alternative rule (H8) says an equal alternative to the option the product recommends is secondary, never ghost

Here the rules contradict each other. The order checks the skip rule first, but the equal-alternative rule says "never ghost". The designer's answer is secondary. Gemini 3.1 Pro and both Grok models followed the skip rule and chose ghost in 4 of their 9 answers.

A third answer is also possible: primary, because 'Stay on Free' confirms the plan the user already has, while 'Upgrade to Pro' changes it. No model chose primary in any of the 90 answers on this button, at any level.

#### The rules do not say whether retyping counts as undoing

'Discard changes' in a dialog about unsaved changes fits 2 rules:

- one rule (H2) says an action that cannot be undone is destructive
- another (H3) says an action that can be undone later is never destructive

The designer's answer is destructive, because the system cannot bring the changes back. Haiku 4.5 argued that "discarding changes can be undone by re-entering the data", so it is not destructive. It chose secondary in 3 of 3 tries. The rules do not say whether redoing the work by hand counts as undoing it.

### Models differ in what they do when the design system has no guidance

With names only, 5 models answered 'none' on most scenarios where a variant was expected. Grok 4.3 did so on 73 of 84, GPT-6 Astra on 72, Grok 4.7 on 71, GPT-5.6 on 67, and Sonnet on 57. They took the instruction "Base your choice only on the design system reference" literally. Opus, Haiku, and Gemini 3.8 Flash never answered 'none', and Gemini 3.1 Pro did so only 5 times. Fable 5.1 sat in between, with 28 of 84.

With rules, no model answered 'none' on any of the 84 scenarios where a variant was expected. When the design system has no guidance, it needs to tell the model whether to guess from training or answer 'none'. A 'none' is easier for the model to reason about than a wrong guess.

### Where it failed

- Haiku 4.5 rejects a reasoning setting the other Claude models accept; its first run failed on the first call and was rerun without it
- Gemini 3.1 Pro is capped at 250 requests a day on our tier, so the 261-call run stopped at 247
- the last 14 Gemini 3.1 Pro answers were filled the next day, a few at a time
- Gemini 2.5 Pro, our first fallback, is not available to new accounts; Gemini 3.8 Flash was used instead
- GPT-5.6 sol turned out to be a generation behind OpenAI's flagship, so GPT-6 Astra was added before findings were final
- xAI was added the same way, as a fourth company
- 7 of 162 reworded pairs broke with rules, all on the pairs that test rule H12
- in each break a model applied a different rule, and none broke by matching a rule's words

## What to do with this

1. Write button rules once, with IDs and a precedence order; they held on 10 models without tuning.
2. Run your rules on 3 or 4 models and list where they split. The splits are your gaps, and you can find them before deciding the correct answers.
3. Decide what the model should do when the design system has no guidance: guess from convention, or answer 'none'.
4. Write the 3 missing rules, then run again; a rule enters the system only when every model reads it the same way.

Nothing changes in the system yet. The 12 rules stay as they are, with a note of the 10 models they were tested on. The 3 missing rules are a candidate wheel 003.

## What this does not show

- one component; nothing here says rules work for layouts, patterns, or whole screens
- each model at one reasoning setting; we did not vary it
- Google's newest model, Gemini 4, is not available to our account
- the correct answers are one designer's judgement; on 'Archive project' half the models read the rule the other way
- we wrote the human written documentation ourselves, copying the style of a typical design system site rather than a real one

## Details

**How we tested**

| Setting | Value |
| --- | --- |
| Models | 10, from Anthropic, OpenAI, Google, and xAI, each through its own application programming interface (API) |
| Information levels | wheel 001's, unchanged: names, human written documentation, and rules |
| Scenarios | wheel 001's 29, unchanged, with the same correct answers |
| Repeats | 3 per scenario per level, each a fresh conversation |
| Scoring | wheel 001's script, against the same correct answers |
| Dates | 7 October 2026, with Gemini 3.1 Pro finishing on 8 October |
| Cost | about €7.62 in API credit, pay as you go, for the 9 runs, from €0.23 for Haiku 4.5 to €1.71 for Gemini 3.1 Pro. Opus 5.5's run is counted in wheel 001 |

**Reproduce it**

- wheel: `wheels/002-other-models/`
- raw output: `wheels/002-other-models/runs/`, one folder per model
- runner: `wheels/002-other-models/experiment/`, which reuses wheel 001's scenarios, levels, and scoring

**Questions this raises**

- can the 3 open readings be closed with 3 sentences, and do the same 10 models then agree
- should a design system tell models to answer 'none' when it has no guidance
- does the lead for rules shrink at low reasoning effort on the models that argued with themselves

**Changes to this post**

- 8 October 2026: first version
- 8 October 2026: [wheel 003](../003-three-missing-rules/post.md) tested the 3 missing rules, and misses rose from 32 to 40 of 870, so they did not enter the system
- 9 October 2026: the cost is now worked out from the tokens each model used and each company's published prices, about €7.62 instead of about €10
- 9 October 2026: part of this result relied on button labels; without the rules' examples, in [wheel 004](../004-new-button-rules/post.md), 9 models missed 69 of 783 answers, not 27
