# Findings

Draft of 7 October 2026. The Gemini 3.1 Pro preview run is 13 answers short at level C, held by Google's 250 requests a day cap, and finishes on 8 October. Its figures below are marked partial. Nothing else is pending.

## Summary

The rules travel. On every model tested, machine-readable rules scored higher than human documentation, by 16 to 24 points, and higher than variant names alone. With rules, 4 of 5 models scored 80 of 87 or more: Sonnet 5.5 87, Haiku 4.5 84, Gemini 3.8 Flash 82, GPT-5.6 80. Gemini 3.1 Pro preview is at 70 of 74 with 13 answers to come.

Every miss with rules, on every model, is one of 2 readings the rules leave open: when a reversible alternative is ghost rather than secondary, and whether redoing work by hand counts as "undo". Both were already visible in wheel 001.

## Evidence

Runs are in `runs/`, one folder per model, each with a `summary.md`. The Opus row is wheel 001's run 3, for comparison.

| Model | Rules | Human docs | Names only |
| --- | --- | --- | --- |
| Opus 5.5 (wheel 001) | 87 of 87 | 63 of 87 | 54 of 87 |
| Sonnet 5.5 | 87 of 87 | 66 of 87 | 27 of 87 |
| Haiku 4.5 | 84 of 87 | 68 of 87 | 54 of 87 |
| Gemini 3.8 Flash | 82 of 87 | 60 of 87 | 54 of 87 |
| GPT-5.6 sol | 80 of 87 | 62 of 87 | 19 of 87 |
| Gemini 3.1 Pro preview (partial) | 70 of 74 | 65 of 87 | 53 of 87 |

Consistency with rules, meaning scenarios where all 3 repeats gave the same answer: Opus 29 of 29, Sonnet 29 of 29, Haiku 29 of 29, Gemini Flash 28 of 29, GPT 27 of 29, Gemini Pro 24 of 25 so far.

### Rules beat human documentation on every model, by 16 to 24 points

The order rules, then documentation, then names held on all 6 runs. The smallest gap between rules and documentation was Gemini Pro's, 16 points on the partial run; the largest was Gemini Flash's, 25 points. The wheel's criterion was 10 points on every model.

### Two models refused to guess without guidance

With names only, Sonnet answered 'none' on 57 of 84 scenarios where a variant was expected, and GPT on 67 of 84. Both read the instruction to use only the reference literally: no guidance, so no answer. Opus, Haiku and both Geminis filled the gap with convention and scored about 54 of 87. This is why Sonnet's and GPT's names-only scores are so low. It is a difference in how models treat silence, not in how they read rules: with rules, neither used 'none' once in 84 chances.

### No model matched words instead of applying rules

The 6 reworded pairs test whether a model gets the original right and the reworded pair wrong. With rules, that happened 0 times on any model, in 108 chances. Where a pair failed, it was the original that failed: GPT and Gemini Flash got 'Pay by bank transfer' right in 3 of 3 while calling 'Log out' ghost, which is the secondary-or-ghost gap below, not word-matching.

### Every miss with rules is one of 2 open readings

| Scenario | Key | Models that chose otherwise |
| --- | --- | --- |
| 14 'Archive project' | secondary | GPT 3 of 3, Gemini Pro 3 of 3, Gemini Flash 2 of 3, all ghost |
| 13 'Log out' | secondary | Gemini Flash 3 of 3, GPT 2 of 3, all ghost |
| 8 'Export CSV' | secondary | GPT 2 of 3, ghost |
| 25 'Stay on Free' | secondary | Gemini Pro 1 of 3, ghost |
| 18 'Discard changes' | destructive | Haiku 3 of 3, secondary |

The first 4 rows are one reading. Precedence step 5 says "secondary if it is a real choice the user may take, ghost if it is optional and rarely needed", and 3 models read archive, log out and export as optional and rarely needed. The Claude models read them as real choices. The rules do not say which, and the models said so: every reason cites step 5 or H11.

The last row is the other reading. Haiku argued that discarding unsaved changes "can be undone by re-editing", so rule H3 makes it not destructive. The other 5 models read redoing work by hand as not an undo. Wheel 001 met the same ambiguity on scenario 17 and fixed the scenario; this time it is the rule that needs the word.

## Failure modes seen

Our setup, not the models, caused 3 stops:

- Haiku 4.5 rejects the reasoning-effort setting the other Claude models accept; the first Haiku run failed on its first call and was rerun with the setting omitted
- Gemini 3.1 Pro preview is capped at 250 requests a day on the account's tier; the run stopped at 247 of 261 and resumes the next day
- Gemini 2.5 Pro, chosen as the stable fallback, is not available to new Google accounts; Gemini 3.8 Flash was used instead

The runner now stops cleanly at a daily cap and prints the resume command.

## Open questions raised

These go to `../../QUESTIONS.md`.

- can the secondary-or-ghost line be written as a rule that all 6 models read the same way, and does it survive a rerun
- should "can be undone" be defined as "restored by the system", excluding redoing work by hand, and does that fix 'Discard changes' without breaking anything else
- is the refusal to guess without guidance (Sonnet, GPT) a property worth designing for, since a model that says 'none' when the system is silent is safer than one that fills the gap with convention
