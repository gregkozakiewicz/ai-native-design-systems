# 3 amended rules meant to fix the last 32 misses raised them to 40

With the rules, models still score 76 to 87 of 87; 3 sentences meant to fix the last 32 misses raised them to 40.

**Wheel:** `wheels/003-three-missing-rules/` · **Runs dated:** 8 October 2026 · **Status:** answered

| 10 of 10 | 40 of 870 | 22 of 22 | 6 of 10 |
| --- | --- | --- | --- |
| models still scored 76 or more of 87 with the rules | answers that missed with the 3 sentences, up from 32 without them | misses fixed on the 3 buttons that the one working sentence was aimed at | models that now call 'Revert to original' in an image editor destructive, not ghost |

## The question

Can we fix [wheel 002](../002-other-models/post.md)'s 32 misses by amending 3 of its rules, without causing new ones on the same 10 models? In wheel 002, 10 models chose button variants with the same 12 rules and scored 80 to 87 of 87. Their 32 misses, the answers that differed from the designer's, all came from 3 gaps in the rules. While those gaps remain, the rules cannot enter the design system as tested on 10 models.

**In scope:** wheel 001's 29 scenarios and correct answers, wheel 002's 10 models at the same settings, and the rules with 3 sentences added.
**Out of scope:** wheel 002's other 2 levels, names only and human written documentation, which did not change; any other change to the rules; new scenarios.

## The answer

No. The rules still work: with the 3 sentences, every model scored 76 to 87 of 87. But the sentences raised the misses from 32 to 40 of 870, where we expected fewer than 10. One sentence fixed all 22 misses it was aimed at, and the other 2 each improved one button and made others worse. The models followed the new text as written, and the text said something the designer did not mean.

**Based on:** one component, 10 models, and the 3 sentences tested together. It does not show how each sentence works on its own.

## One example

'Revert to original' in an image editor toolbar, as seen by every model. The answers are Claude Opus 5.5's.

**The task**

```
Context: An image editor. The user has applied several crops and filters. In the toolbar is a button that removes all of them and shows the original photo again. The user can apply edits again afterwards.
Button label: "Revert to original"

Which variant should this button use?
```

**Without the 3 sentences** (wheel 002's 12 rules)

```
ghost

Under H10, an action that undoes the user's own edits, is rarely needed and cannot cause permanent loss is ghost, and H3 rules out destructive because the edits can be applied again.
```

Opus applied H10, the rule for undoing the user's own edits, and gave the designer's answer in 3 of 3 repeats.

**With the 3 sentences**

```
destructive

Reversibility comes first in the precedence order: reverting discards all crops and filters, and the only way back is to redo them by hand, which H3 says does not count as reversible, so H2 makes it destructive (H10's ghost does not apply because the edits are lost permanently).
```

Opus applied the new sentence, which says redoing work by hand does not count as undoing it, and missed in 3 of 3 repeats. 5 other models did the same in at least 2 of their 3. Full output: `runs/2026-10-08-claude-opus-5-5/`. The run without the sentences is wheel 001's `runs/2026-10-07-opus-5-5-medium-run3/`.

## What we found

### One sentence fixed every miss it was aimed at, and 2 made other buttons worse

We wrote one sentence for each gap that wheel 002 found, and added all 3 to the rules at once.

| Sentence | What it adds to the rules |
| --- | --- |
| 1. Where 'optional' ends | A reversible action the user came to the view for, or may reasonably take there, is secondary, such as archive, export, or log out. Ghost is only for actions most users never take on that view. |
| 2. Which rule wins | If 2 rules about the button's role fit, the more specific one wins. An equal alternative to a recommended option (H8) beats a bypass (H12), and a bypass beats a plain dismiss (H5). |
| 3. What 'undone' means | An action is reversible only if the system can restore the previous state. Redoing the work by hand does not count. |

Sentence 1 fixed all 22 misses on the 3 buttons it was aimed at. Each button got 30 answers: 10 models, 3 repeats each.

| Sentence | Button | Misses without the sentences | Misses with them |
| --- | --- | --- | --- |
| 1 | 'Archive project' on a project settings page | 13 of 30 | 0 of 30 |
| 1 | 'Log out' in an account menu | 6 of 30 | 0 of 30 |
| 1 | 'Export CSV' above a data table | 3 of 30 | 0 of 30 |
| 1 | 'New invoice' in the header of an invoices list page | 0 of 30 | 2 of 30 |
| 2 | 'Not now' on a prompt to turn on notifications | 3 of 30 | 0 of 30 |
| 2 | 'Stay on Free' on a pricing screen | 4 of 30 | 12 of 30 |
| 3 | 'Discard changes' in a dialog about unsaved changes | 3 of 30 | 1 of 30 |
| 3 | 'Reset to defaults' on a profile settings page | 0 of 30 | 8 of 30 |
| 3 | 'Revert to original' in an image editor toolbar | 0 of 30 | 16 of 30 |
| 3 | 'Save changes' at the bottom of a profile settings page | 0 of 30 | 1 of 30 |
| | All 29 scenarios | 32 of 870 | 40 of 870 |

The other 19 scenarios had no misses in either run. All 3 sentences ran together, so we assign each miss to a sentence by the rule the model cited. Runs: `runs/`, one folder per model.

### The models followed the new text, which said something the designer did not mean

Where misses rose, the models' reasons quote the new sentences. On 'Reset to defaults' on a profile settings page and 'Revert to original' in an image editor, 24 of 60 answers missed. All 24 say that redoing work by hand does not count. All 36 correct answers on those 2 buttons cite H10, the rule for undoing the user's own edits, instead.

The table counts the models whose most common answer, over 3 repeats, was destructive.

| Button | Designer's answer | Without the sentences | With them |
| --- | --- | --- | --- |
| 'Discard changes' in a dialog about unsaved changes | destructive | 9 of 10 models | 10 of 10 models |
| 'Reset to defaults' on a profile settings page | ghost | 0 of 10 models | 2 of 10 models |
| 'Revert to original' in an image editor toolbar | ghost | 0 of 10 models | 6 of 10 models |

No single meaning of 'undone' fits all 3 of the designer's answers. All 3 buttons lose work that comes back only if the user redoes it by hand. The designer calls the first destructive and the other 2 ghost. The designer sees a difference, but it is not about undo.

Sentence 2 had the same problem on 'Stay on Free' on a pricing screen. It works only if a model first decides that H8, the rule for an equal alternative, applies. H8's wording fits choices such as rejecting cookies: "a legally or ethically equal alternative". Fable, Opus, Sonnet, and GPT-5.6 cited H8 and chose secondary. GPT-6 Astra, both Grok models, and Gemini 3.1 Pro never cited it, and chose ghost in 11 of their 12 answers.

The models also agree with each other more than before. Taking each model's most common answer, all 10 agreed on 25 of 29 scenarios, up from 23.

A reason is one line the model writes with its answer. It shows the rule the model named, not everything it weighed. Runs: `runs/`.

### 4 of the 5 top-tier models scored lower, and the other 5 held or gained

The top-tier models are each company's flagship that our account can reach, plus Claude Opus 5.5. All scores are out of 87.

| Model | Tier | Without the sentences | With them |
| --- | --- | --- | --- |
| Claude Fable 5.1 | flagship | 87 of 87 | 85 of 87 |
| Claude Opus 5.5 | large | 87 of 87 | 81 of 87 |
| GPT-6 Astra | flagship | 84 of 87 | 76 of 87 |
| Grok 4.7 | flagship | 83 of 87 | 79 of 87 |
| Gemini 3.1 Pro | top Pro model our account can reach | 82 of 87 | 82 of 87 |
| Claude Sonnet 5.5 | mid | 87 of 87 | 87 of 87 |
| Claude Haiku 4.5 | small | 84 of 87 | 86 of 87 |
| GPT-5.6 sol | previous flagship | 80 of 87 | 83 of 87 |
| Grok 4.3 | older | 82 of 87 | 85 of 87 |
| Gemini 3.8 Flash | small | 82 of 87 | 86 of 87 |

The top-tier models made 20 of the 24 misses on the 2 buttons that reset the user's edits. The other 5 had made 16 of the 22 misses that sentence 1 fixed, so they gained most from it. A sentence that says the wrong thing costs most on the models that follow the rules most closely.

This does not show that top-tier models are worse at rules. They followed the new text more closely than the others.

### Where it failed

A reworded pair is a second scenario that tests the same rule in different words. These went wrong, in our setup as well as in the answers:

- 20 of 180 reworded pairs broke, against 7 of 162 in wheel 002
- 12 of the 20 breaks pair 'Reject all' on a cookie banner with 'Stay on Free' on a pricing screen
- the other 8 pair 'Reset to defaults' on a settings page with 'Revert to original' in an image editor
- each pair differs exactly where a new sentence changed the rules, so the breaks come from the new text, not from matching words
- no run failed, and when one Grok call timed out, the runner retried it

## What to do with this

1. Run every rule change against all your scenarios, because all 3 sentences here moved buttons they were not written for.
2. If a rule change causes new misses, read the models' reasons, which here showed a difference in the designer's answers that no rule states.
3. Before you write a rule, write down why your answers differ where the situations look alike.
4. Include your top-tier models in every test run, because they follow a rule that says the wrong thing most closely.

Nothing changes in the system, and the 12 rules stay as they are. Sentence 1 goes into the next run unchanged. Before that run, the designer needs to make 2 decisions. The first is what makes 'Discard changes' in a dialog destructive, but 'Reset to defaults' on a settings page ghost. The second is whether H8 covers 'Stay on Free' on a pricing screen.

## What this does not show

This run has these limits:

- one component and 29 scenarios, the same scenarios that found the gaps
- the 3 sentences ran together, so we have no measure of each one on its own
- sentence 1 names its 3 target buttons as examples, so we have no measure of it on other buttons
- the correct answers are one designer's judgement; the run shows where the text and the answers part, not which is right
- a model's reason is one line it writes with its answer, not a full record of what it weighed
- the cost is an estimate, not a measured figure

## Details

**How we tested**

| Setting | Value |
| --- | --- |
| Models | wheel 002's 10, from Anthropic, OpenAI, Google, and xAI, at the same settings, each through its own application programming interface (API) |
| Information levels | rules only: wheel 001's 12 rules with the 3 sentences added |
| Scenarios | wheel 001's 29, unchanged, with the same correct answers |
| Repeats | 3 per scenario per model, each a fresh conversation: 870 answers |
| Scoring | wheel 001's script, against the same correct answers |
| Dates | 8 October 2026 |
| Cost | about €4 in API credit, pay as you go, for all 10 runs, with no reruns. We estimated it as a third of wheel 002's cost, since each model made a third of the calls: about €0.40 per model |

We wrote the 3 sentences, the expected result, and the success criteria before the first run, and changed nothing after.

**Reproduce it**

- wheel: `wheels/003-three-missing-rules/`
- raw output: `wheels/003-three-missing-rules/runs/`, one folder per model
- rule file and runner: `wheels/003-three-missing-rules/experiment/`, which reuses wheel 002's runner and wheel 001's scenarios and scoring

**Questions this raises**

- what separates 'Discard changes' in a dialog, which is destructive, from 'Reset to defaults' on a settings page, which is ghost
- does H8 cover declining an upgrade, or only choices the law requires, such as rejecting cookies
- should every rule change run on all scenarios before anyone proposes it

**Changes to this post**

- 8 October 2026: first version
