# The same 12 button rules work on 9 models from 4 companies

Nine models from Anthropic, OpenAI, Google and xAI all chose the correct button variant in 80 to 87 of 87 answers with the rules, against 60 to 73 with documentation.

**Wheel:** `wheels/002-other-models/` · **Runs dated:** 7 and 8 October 2026 · **Status:** answered

| 9 of 9 | 23 of 29 | 4 of 29 | 32 of 783 |
| --- | --- | --- | --- |
| models scored 80 or more of 87 with the rules | scenarios where all 9 models gave the same answer, with rules | scenarios where all 9 agreed with variant names only | answers with rules that missed, all from 3 unwritten sentences |

## The question

Does the button variant rule set from wheel 001 guide models other than Claude Opus 5.5 as well as it guided Opus? Wheel 001 took one model from 54 of 87 to 87 of 87 with 12 written rules. If that holds only for Opus, the rules are a prompt tuned to one model. If it holds across companies, the rules belong to the design system.

**In scope:** the same 29 scenarios, 3 information levels and answer key as wheel 001, on 9 models at their default reasoning settings.
**Out of scope:** changing the rules to suit a model; tuning per model; other components.

## The answer

Yes. The rules travel. On every model, written rules beat documentation written in the style of a typical design system site, by 9 to 24 points, and every model scored at least 80 of 87 with them. The rules also moved the models towards each other: with rules, all 9 gave the same answer on 23 of 29 scenarios; with names only, on 4. The 6 scenarios where they split are the 3 places the rules leave a reading open, and nothing else. The evidence covers one component and 9 models; it says nothing about Google's newest model, which our key cannot reach, or about reasoning settings other than each model's default.

## One example

Scenario 13, as every model saw it. The answers are GPT-6 Astra's.

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

### Rules beat documentation on all 9 models, by 9 to 24 points

Each model answered 29 scenarios, 3 times each, at 3 levels. Only the reference text changed.

| Model | Tier | Rules | Documentation | Names only |
| --- | --- | --- | --- | --- |
| Claude Opus 5.5 | flagship | 87 of 87 | 63 of 87 | 54 of 87 |
| Claude Sonnet 5.5 | mid | 87 of 87 | 66 of 87 | 27 of 87 |
| Claude Haiku 4.5 | small | 84 of 87 | 68 of 87 | 54 of 87 |
| GPT-6 Astra | flagship | 84 of 87 | 63 of 87 | 15 of 87 |
| GPT-5.6 sol | previous flagship | 80 of 87 | 62 of 87 | 19 of 87 |
| Gemini 3.1 Pro | top Pro reachable by API | 82 of 87 | 65 of 87 | 53 of 87 |
| Gemini 3.8 Flash | small | 82 of 87 | 60 of 87 | 54 of 87 |
| Grok 4.7 | flagship | 83 of 87 | 71 of 87 | 16 of 87 |
| Grok 4.3 | older | 82 of 87 | 73 of 87 | 13 of 87 |

Tiers are each company's own, checked against an independent public index. Grok 4.3 has the best documentation score, 73, so its gap to rules is the narrowest at 9 points, one short of the wheel's 10-point criterion. Claude Fable 5.1, run at low effort outside the boundary, also scored 87 of 87.

### Rules move models towards each other, not only towards the designer

For each scenario we asked whether all 9 models gave the same majority answer, without looking at the key.

| Level | Scenarios where all 9 models agree |
| --- | --- |
| Names only | 4 of 29 |
| Documentation | 17 of 29 |
| Rules | 23 of 29 |

This measure needs no answer key. Write the rules, run them on several models, and the scenarios where models split are the gaps in the rules. In this wheel the 6 splits were exactly the 3 open readings below.

### Every miss comes from 3 sentences nobody wrote

Across 783 answers with rules, 32 missed. All 32 trace to 3 places where the rules leave a reading open, and in every case the model named the rule it chose.

| Open reading | Scenarios | Misses |
| --- | --- | --- |
| Where "optional" ends: a reversible action like archive, log out or export, is it a real choice (secondary) or optional (ghost)? | 14, 13, 8 | 22 |
| Which rule wins when two in the same step fit: 'Not now' is both a dismiss and a bypass | 28, 25 | 7 |
| What "undone" means: does redoing work by hand count? | 18 | 3 |

On 'Archive project', 5 of 9 models chose ghost against the designer's secondary. It is the one scenario where the designer's reading is the minority one.

### Models differ in what they do when the system is silent

With names only, 5 models answered 'none' on most scenarios: Grok 4.3 on 73 of 84, GPT-6 Astra 72, Grok 4.7 71, GPT-5.6 67, Sonnet 57. They read "use only the reference" literally. Opus, Haiku and both Geminis guessed from convention instead. With rules, no model used 'none' once in 84 chances. A design system read by several models has to decide which behaviour it wants when it is silent; the refusers are easier to catch.

### Where it failed

- Haiku 4.5 rejects a reasoning setting the other Claude models accept; its first run failed on the first call and was rerun without it
- Gemini 3.1 Pro is capped at 250 requests a day on our tier; the 261-call run stopped at 247 and finished the next day as slots freed
- Gemini 2.5 Pro, our first fallback, is not available to new accounts; Gemini 3.8 Flash was used instead
- GPT-5.6 sol turned out to be a generation behind OpenAI's flagship, so GPT-6 Astra was added before findings were final; xAI was added the same way
- 7 of 162 reworded pairs broke with rules, all on the pairs that test rule H12, where a model applied a different rule; none broke by matching a rule's words

## What this does not show

- one component; nothing here says rules work for layouts, patterns or whole screens
- each model at its default reasoning setting; one Fable 5.1 run at low effort is the only other setting tried
- Google's newest model, Gemini 4, is not reachable with our key
- the answer key is one designer's judgement; on 'Archive project' most models read the rule the other way
- the documentation level was written by us in the style of a typical design system site, not taken from a real one

## What to do with this

1. Write button rules once, with IDs and a precedence order; they held on 9 models without tuning.
2. Run your rules on 3 or 4 models and list where they split; the splits are your gaps, and you do not need an answer key to find them.
3. Decide what the system wants when it is silent: a guess from convention, or 'none'.
4. Write the 3 missing sentences, then run again; a rule enters the system only when every model reads it the same way.

Nothing changes in the system yet. The 12 rules stay as they are, with a note of the 9 models they were tested on; the 3 sentences are a candidate wheel 003.

## Details

**How we tested**

| Setting | Value |
| --- | --- |
| Models | 9, from Anthropic, OpenAI, Google and xAI, each through its own API at its default reasoning setting |
| Information levels | wheel 001's, unchanged: names, documentation, rules |
| Scenarios | wheel 001's 29, unchanged, with the same answer key |
| Repeats | 3 per scenario per level, each a fresh conversation |
| Scoring | wheel 001's script, against the same key |
| Dates | 7 October 2026, with Gemini 3.1 Pro finishing on 8 October |
| Cost | about €1 per model in API credit, pay as you go, about €10 for all runs including the labelled Fable extra; the Fable run alone was €1.40 |

**Reproduce it**

- wheel: `wheels/002-other-models/`
- raw output: `wheels/002-other-models/runs/`, one folder per model
- runner: `wheels/002-other-models/experiment/`, which reuses wheel 001's scenarios, levels and scoring

**Questions this raises**

- can the 3 open readings be closed with 3 sentences, and do the same 9 models then agree
- is refusing to guess when the system is silent a property to design for
- does the lead for rules shrink at low reasoning effort on the models that argued with themselves

**Changes to this post**

- 8 October 2026: first version
