# Findings

## Summary

The rules travel. On 9 models from 4 companies, machine-readable rules scored higher than human documentation on every one, and higher than variant names alone. With rules, all 9 scored 80 of 87 or more: Opus 87, Sonnet 87, Haiku 84, GPT-6 Astra 84, Grok 4.7 83, Gemini 3.1 Pro 82, Gemini 3.8 Flash 82, Grok 4.3 82, GPT-5.6 80.

Every miss with rules, on every model, traces to 3 places where the rules leave a reading open. All 3 are named in the models' own reasons, and each is one sentence away from closed.

## Evidence

Runs are in `runs/`, one folder per model, each with a `summary.md`. Opus is wheel 001's run 3. Tiers are each company's own, confirmed against an independent public index on 7 October 2026.

| Model | Tier | Rules | Human docs | Names only |
| --- | --- | --- | --- | --- |
| Claude Opus 5.5 | flagship | 87 of 87 | 63 of 87 | 54 of 87 |
| Claude Sonnet 5.5 | mid | 87 of 87 | 66 of 87 | 27 of 87 |
| Claude Haiku 4.5 | small | 84 of 87 | 68 of 87 | 54 of 87 |
| GPT-6 Astra | flagship | 84 of 87 | 63 of 87 | 15 of 87 |
| GPT-5.6 sol | previous flagship | 80 of 87 | 62 of 87 | 19 of 87 |
| Gemini 3.1 Pro preview | top reachable Pro | 82 of 87 | 65 of 87 | 53 of 87 |
| Gemini 3.8 Flash | small | 82 of 87 | 60 of 87 | 54 of 87 |
| Grok 4.7 | flagship | 83 of 87 | 71 of 87 | 16 of 87 |
| Grok 4.3 | older | 82 of 87 | 73 of 87 | 13 of 87 |

One run sits outside the wheel's boundary and is reported separately: Claude Fable 5.1 at low reasoning effort, not its default. It scored 87 of 87 with rules, 70 of 87 with human documentation and 48 of 87 with names only, with all 29 scenarios consistent under rules. It cost about €1.40, the most of any run, and it is the only model that was partly a refuser at level A, answering 'none' on 28 of 84.

The same scores broken down by scenario, showing how many of the 3 repeats were right. A scenario at 0 of 3 is a firm different reading; one at 1 or 2 of 3 is a model that could not decide. The Fable row ran at low effort, outside the wheel's boundary.

| Model | Score | 3 of 3 right | 2 of 3 | 1 of 3 | 0 of 3 | Argued with itself |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 5.5 | 87 of 87 | 29 | 0 | 0 | 0 | 0 of 29 |
| Claude Fable 5.1 | 87 of 87 | 29 | 0 | 0 | 0 | 0 of 29 |
| Claude Sonnet 5.5 | 87 of 87 | 29 | 0 | 0 | 0 | 0 of 29 |
| Claude Haiku 4.5 | 84 of 87 | 28 | 0 | 0 | 1 | 0 of 29 |
| GPT-6 Astra | 84 of 87 | 28 | 0 | 0 | 1 | 0 of 29 |
| Grok 4.7 | 83 of 87 | 26 | 2 | 1 | 0 | 3 of 29 |
| Gemini 3.1 Pro | 82 of 87 | 27 | 0 | 1 | 1 | 1 of 29 |
| Gemini 3.8 Flash | 82 of 87 | 27 | 0 | 1 | 1 | 1 of 29 |
| Grok 4.3 | 82 of 87 | 26 | 2 | 0 | 1 | 2 of 29 |
| GPT-5.6 sol | 80 of 87 | 26 | 0 | 2 | 1 | 2 of 29 |

The 5 Claude and GPT-6 rows never argued with themselves; every miss they have is a firm reading, which one sentence can change. The Grok, Gemini and GPT-5.6 rows argue only on the secondary-or-ghost line, which is the vaguest of the 3 open readings.

### Rules beat human documentation on every model, by 9 to 24 points

The order rules, then documentation, then names held on all 9 runs. The gap ranged from 9 points (Grok 4.3, whose 73 of 87 is the best documentation score of any model) to 24 points (Opus and Gemini Flash). The wheel's criterion was 10 points on every model; Grok 4.3 falls one point short of it while still clearing 80 of 87 with rules.

### Five models refused to guess without guidance

With names only, 5 models answered 'none' on most scenarios where a variant was expected: Grok 4.3 on 73 of 84, GPT-6 Astra 72, Grok 4.7 71, GPT-5.6 67, Sonnet 57. They read the instruction to use only the reference literally: no guidance, so no answer. Opus, Haiku and both Geminis filled the gap with convention and scored 53 or 54 of 87. This is a difference in how models treat silence, not in how they read rules: with rules, no model used 'none' once in 84 chances.

### Reworded pairs held, with one exception that is a rule conflict, not word-matching

The 6 reworded pairs test whether a model gets the original right and the reworded pair wrong. With rules, that happened 7 times in 162 chances across 9 models, and all 7 were on the 2 pairs that test rule H12, where the model applied a different rule to the reworded scenario. GPT-6 Astra read 'Not now' as a dismiss (H5, secondary) in 3 of 3 where the key reads it as a bypass (H12, ghost). Nowhere did a model copy a rule's answer because the scenario echoed the rule's words. Wheel 001's result stands, with the caveat that rule conflicts can break a pair.

### The 9 models agree with each other on 23 of 29 scenarios with rules, 17 with documentation, 4 with names only

Agreement between models is measured without the key: for each scenario, do all 9 models give the same majority answer? With rules they do on 23 of 29. With documentation, 17 of 29. With names only, 4 of 29. Rules do not only move models towards the designer; they move models towards each other.

The 6 scenarios where models split with rules are exactly the 3 open readings below, and nothing else:

| Scenario | Key | Models |
| --- | --- | --- |
| 14 'Archive project' | secondary | ghost 5, secondary 4 |
| 13 'Log out' | secondary | secondary 7, ghost 2 |
| 8 'Export CSV' | secondary | secondary 8, ghost 1 |
| 25 'Stay on Free' | secondary | secondary 8, ghost 1 |
| 28 'Not now' | ghost | ghost 8, secondary 1 |
| 18 'Discard changes' | destructive | destructive 8, secondary 1 |

On 'Archive project' the majority of models disagree with the key. That does not make the key wrong, but it is the one scenario where the designer's reading is the minority one, and the rule that settles it has to be written with that in mind.

This measure needs no designer. A rule set can be checked for gaps by running it on several models and reading the splits, before anyone writes an answer key.

### Every miss with rules is one of 3 open readings

| Open reading | Scenarios | Models that read it the other way |
| --- | --- | --- |
| Reversible alternative: secondary or ghost? Precedence step 5 says "secondary if a real choice, ghost if optional and rarely needed" | 14 'Archive project', 13 'Log out', 8 'Export CSV' | GPT-5.6 7 of 9, Gemini Pro 3 of 3 on 14, Gemini Flash 5 of 6, Grok 4.3 4, Grok 4.7 3, all ghost |
| Does redoing work by hand count as undo? Rule H3 says "can be undone or reversed later" | 18 'Discard changes' | Haiku 3 of 3, secondary |
| Two rules in the same precedence step both fit: H5 (dismiss) or H8 (recommended option's alternative) against H12 (bypass) | 28 'Not now', 25 'Stay on Free' | GPT-6 Astra 3 of 3 on 28 as secondary (H5); Gemini Pro 2, Grok 4.7 1, Grok 4.3 1 on 25 as ghost (H12) |

The Claude models read the first and third the designer's way; most others did not. In every case the model named the rule it chose, so the fix is specific: a sentence on where "optional" ends, a definition of "undone", and an order between H5, H8 and H12.

## Failure modes seen

Our setup, not the models, caused 3 stops:

- Haiku 4.5 rejects the reasoning-effort setting the other Claude models accept; the first Haiku run failed on its first call and was rerun with the setting omitted
- Gemini 3.1 Pro preview is capped at 250 requests a day on the account's tier, as a rolling 24-hour window; the run stopped at 247 of 261 on 7 October and the last 14 answers were filled on 8 October with the same command, one or a few at a time as slots freed
- Gemini 2.5 Pro, chosen as the stable fallback, is not available to new Google accounts; Gemini 3.8 Flash was used instead

Two choices were corrected during the wheel, before findings were final: GPT-5.6 sol turned out to be a generation behind OpenAI's flagship, so GPT-6 Astra was added; xAI was added as a fourth company. Google's newest model, Gemini 4, is not reachable with the account's key.

## Open questions raised

These go to `../../QUESTIONS.md`.

- can the 3 open readings be closed with 3 sentences, and do the same 9 models then agree
- is refusing to guess when the system is silent a property to design for, since 5 of 9 models do it by default and a sixth does it a third of the time
- does the gap between rules and documentation shrink at low reasoning effort
