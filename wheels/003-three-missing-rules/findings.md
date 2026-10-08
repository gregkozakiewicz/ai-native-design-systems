# Findings

## Summary

No. The 3 sentences raised the misses from 32 to 40 across the 10 models. One sentence worked completely, one worked on half its scenarios, and one backfired. In every case the models followed the new text as written. Where the result went wrong, the text said something the designer did not mean.

The sentence that backfired exposed a distinction in the designer's own answers that no rule states yet. 'Discard changes' is destructive, while 'Reset to defaults' and 'Revert to original' are ghost, and nothing says why.

## Evidence

Runs are in `runs/`, one folder per model, each with a `summary.md`. Wheel 002's figures are its level C results with the original 12 rules.

| Model | Wheel 002 | Wheel 003 |
| --- | --- | --- |
| Claude Fable 5.1 | 87 of 87 | 85 of 87 |
| Claude Opus 5.5 | 87 of 87 | 81 of 87 |
| Claude Sonnet 5.5 | 87 of 87 | 87 of 87 |
| Claude Haiku 4.5 | 84 of 87 | 86 of 87 |
| GPT-6 Astra | 84 of 87 | 76 of 87 |
| GPT-5.6 sol | 80 of 87 | 83 of 87 |
| Grok 4.7 | 83 of 87 | 79 of 87 |
| Grok 4.3 | 82 of 87 | 85 of 87 |
| Gemini 3.1 Pro | 82 of 87 | 82 of 87 |
| Gemini 3.8 Flash | 82 of 87 | 86 of 87 |

Misses in total went from 32 of 870 to 40 of 870.

### Sentence 1 closed all 22 misses it was aimed at

The sentence on where "optional" ends took 'Archive project', 'Log out' and 'Export CSV' from 22 misses to 0. All 10 models now agree on all 3.

It cost 2 misses elsewhere. GPT-6 Astra called 'New invoice' secondary in 2 of 3 repeats. Its reason quotes the new wording: "a reasonable action on this view, but it is not identified as the product's recommended action".

### Sentence 2 fixed 'Not now' and made 'Stay on Free' worse

The sentence on which rule wins inside a step took 'Not now' from 3 misses to 0. On 'Stay on Free' misses rose from 4 to 12.

The sentence says an equal alternative (H8) beats a bypass (H12). It only works if a model first decides H8 applies. H8 is worded for cases like cookie consent: "a legally or ethically equal alternative". Sonnet and GPT-5.6 read 'Stay on Free' that way and chose secondary. GPT-6 Astra, both Grok models and both Gemini models did not consider H8 at all. The sentence's own example then made the bypass rule easier to reach.

### Sentence 3 fixed 'Discard changes' and broke 2 scenarios that were unanimous

The sentence on what "undone" means took 'Discard changes' from 3 misses to 1. It also took 'Reset to defaults' from 0 misses to 8 and 'Revert to original' from 0 to 16. Grok 4.7 called 'Save changes' destructive once, for the same reason.

The models that broke read the sentence exactly. Opus gave this reason on 'Revert to original':

> the only way back is to redo them by hand, which H3 says does not count as reversible, so H2 makes it destructive
 The models that held cited rule H10 instead: undoing your own edits, rarely needed, no permanent loss, so ghost.

No single definition of "undone" fits all 3 of the designer's answers. 'Discard changes', 'Reset to defaults' and 'Revert to original' all lose state that can only come back by redoing it by hand. The designer calls the first destructive and the other two ghost. The difference is real, but it is not about undo.

### The largest models lost points and the smaller ones gained

4 of the 5 largest models scored lower than in wheel 002, and the fifth held. Fable lost 2, Opus 6, GPT-6 Astra 8, and Grok 4.7 4, while Gemini 3.1 Pro held. All 5 smaller or older models held or gained: Sonnet 0, Haiku 2, GPT-5.6 3, Grok 4.3 3, Gemini Flash 4. The largest models applied the precedence order most strictly, so reversibility, step 1, decided before H10 was reached. A rule that says the wrong thing costs most on the models that follow rules best.

### Models agreed with each other more, including when they were wrong

All 10 models gave the same majority answer on 25 of 29 scenarios, up from 23. The 4 splits are all new. 'New invoice' split 9 to 1 and 'Reset to defaults' 8 to 2. 'Stay on Free' and 'Revert to original' both split 6 to 4. On 'Revert to original' the majority now disagrees with the designer.

## Failure modes seen

- sentence 1 named its 3 target scenarios as examples, so it shows the sentence moves the models, not that it generalises
- the reworded pairs broke 20 times, all on 2 pairs: 'Reset to defaults' with 'Revert to original', and 'Reject all' with 'Stay on Free'
- each of those pairs differs in exactly what a new sentence turned on, so the breaks come from the wording, not from word-matching
- no run failed; Grok timed out once and retried

## Cost

About €4 in API credit, pay as you go. This is an estimate: each model ran 1 level instead of 3, so about a third of wheel 002's cost.

## Open questions raised

These go to `../../QUESTIONS.md`.

- what makes 'Discard changes' destructive but 'Reset to defaults' and 'Revert to original' ghost, in words a rule can hold
- does H8 cover declining an upgrade, or only legally required choices such as rejecting cookies
- should a rule change be run on every scenario before it is proposed, since all 3 sentences moved scenarios they were not aimed at
