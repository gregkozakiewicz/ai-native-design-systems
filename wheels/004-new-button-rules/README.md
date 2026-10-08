# 004: new button rules

**Status:** proposed
**Started:** 2026-10-08

## Question

Do the rewritten button rules, with no examples that name test buttons, give the designer's answers on the same 10 models?

## Why it matters

Wheel 003 amended 3 rules and raised the misses from 32 to 40 of 870. The designer then rewrote the rules that broke and added a hierarchy rule, all recorded in wheel 003's `implications.md`. If the rewritten rules work, the button rules can enter `system/` as tested on 10 models.

The rules also listed test button labels as examples, such as "skip, not now, maybe later". This wheel takes them out, so a good score cannot come from matching words.

## Boundary

**In scope**

The main run uses the rewritten rules, with every change recorded in wheel 003's `implications.md`:

- the new names: hard rules HR1 to HR12, never rules NR1 to NR5, and precedence steps P1 to P5
- every example that names a test button taken out
- P5 from wheel 003, without its examples, and reworded so its 2 halves cannot both apply
- the hierarchy rule in P4: an action that is the only one in the main area of a view, with no role rule applying, is primary
- new HR2 and HR3: an action is destructive when the lost content would have to be recreated from memory
- new HR8 and HR12: declining a recommended option is secondary, and postponing a step is ghost
- reworded HR5: closing something that asks for no decision is secondary
- HR10 added to P3
- HR4 sends a button that postpones a decision to HR12
- HR7 applies only when 2 actions are answers to the same decision
- HR11 also covers a button that leads to further information or adds something optional to the task
- P3's question uses the same words as the new hard rules
- section 1 describes destructive and ghost in the same way as the new hard rules

The main run's scenarios are wheel 001's 29, with 5 descriptions changed and 2 scenarios added:

- 'Archive project' names 'Save changes' beside it, and stays secondary
- 'Export CSV' names 'Delete 3 rows' beside it, and stays secondary
- 'Revert to original' names 'Save', 'Crop' and 'Filters', and stays ghost
- 'Discard changes' says what the unsaved changes are, and stays destructive
- 'Not now' says the app will ask again next week, and stays ghost
- new: 'Archive project' alone in the main area of the page, answered primary
- new: 'No thanks' turns notifications down and is not asked again, but the user can turn them on in settings, answered secondary

That makes 31 scenarios, 3 repeats each, on wheel 002's 10 models at the same settings: 930 answers.

A smaller check run uses wheel 002's rules with only the examples taken out and the new names, on wheel 001's 29 unchanged scenarios. It runs on 9 of the 10 models, without Gemini 3.1 Pro, to stay within its daily limit of 250 requests: 783 answers. It shows how much the examples alone mattered, and the post mentions it briefly.

Some of these changes came from the check described under 'Checked before the run'. They are the last 6 rule changes, the rewording of P5, and the wording of the 2 new scenarios.

**Out of scope**

- names only and human written documentation
- any rule change not recorded in wheel 003's `implications.md`
- other components

## Success criteria

For the main run:

- answered "yes" if the misses fall to 10 or fewer of 930, and every model scores 90 or more of 93
- also needed for "yes": at least 9 of 10 models get both sides of each new pair right
- answered "partly" if the misses fall below 32 but stay above 10, naming the scenarios that still miss
- answered "no" if the misses are 32 or more of 930
- also answered "no" if a scenario on which all 10 models agreed in wheel 002 now splits
- abandon if a model cannot run at the same setting as in wheel 002

The 2 new pairs are 'Archive project' with and without 'Save changes', and 'Not now' with 'No thanks'.

For the check run, compare the 12 scenarios whose labels were examples with wheel 002, on the same 9 models. In wheel 002 those 9 models missed 19 of 324 answers on these 12 scenarios. A rise of 6 or fewer means the models read the situation, not the words. A rise of more than 20 means wheels 001 and 002 relied on matching words, and their posts need a note.

A rise of 6 allows for variation between runs. In wheel 001, Opus's scores moved by 3 to 4 answers between runs 2 and 3, with names only and with human written documentation. That count leaves out the one scenario that changed between the runs.

The check run also carries the new names, so it differs from wheel 002 in 2 ways, not one.

## Checked before the run

On 8 October 2026, before any model ran, 19 Claude agents read the new rules against all 31 scenarios. 5 read in different ways, such as strictly in order or skimming. Others checked each scenario where a reader disagreed, and one compared the files with the designer's approved decisions.

Read in order, the rules gave the designer's answer on all 31. But 8 scenarios had a second reading a model could plausibly take. 4 of these appeared only because the examples were taken out. The designer approved a change for each one, and none of the designer's answers changed.

On 9 October 2026, a second check by 17 Claude agents read the changed rules the same way. The 8 risks were gone, and 4 smaller ones remained. The designer approved 3 more changes:

- HR8 sends a button that postpones a decision to HR12, as HR4 does
- P4 says the only action in the main area counts as the one the product recommends, even if it does not move the user forward
- P4 says a page header is part of the main area

The fourth risk, that a model calls 'Export CSV' a side task, was left as it is. The suggested fix copied the scenario's own words into the rules.

Both checks used Claude models only, so they may have missed readings that models from other companies take.

