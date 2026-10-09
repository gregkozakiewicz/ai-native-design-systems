# Implications for the system

## Run 3's rules replace the button rules in the system

On 9 October 2026 the designer chose to keep run 3's rules. This file proposes that they replace `system/button-variant.md`, which holds wheel 001's 12 rules.

The proposed text is `experiment/levels/C-new-rules-run3.md`, sections 1 to 5. Section 6 sets the experiment's answer format, so it stays out, as it did for wheel 001. The system file's header would say:

> Proved by: wheel 004, run 3 of 9 October 2026. 10 models from 4 companies gave the designer's answer in 948 of 960 answers, on 32 scenarios. 5 of the 10 scored 96 of 96, and the lowest, Claude Haiku 4.5, scored 90.

These runs justify the change:

- wheel 002's original rules missed 32 of 870
- wheel 004's rewritten rules missed 13 of 930 in run 1, 10 of 930 in run 2, and 12 of 960 in run 3
- without their examples, the original rules missed 69 of 783 on 9 models, so part of their score came from matching button labels

Compared with wheel 001's rules, run 3's rules change in these ways:

- the hard rules are HR1 to HR12, the never rules NR1 to NR5, and the precedence steps P1 to P5
- no rule gives an example that names a test button
- HR2 and HR3 make an action destructive when the content or configuration lost would have to be recreated from memory
- HR3 says an action is not destructive when the user loses only a few choices they can remember and make again
- HR4 sends a button that postpones a decision to HR12, and so does HR8
- HR5 covers a button that closes something that asks for no decision
- HR7 covers only 2 actions that are answers to the same decision
- HR8 makes the button that declines a recommended option secondary
- HR10 covers undoing a few choices the user can remember and make again
- HR11 covers a side task, further information, or an optional extra on the thing the user is creating
- HR12 covers postponing or skipping a step
- P3 asks its question in the words of these hard rules, and includes HR10
- P4 makes the only action in the main area of a view primary, and says a page header is part of the main area
- P5 is one test: secondary if the user may reasonably do it on that view, otherwise ghost
- section 1 describes destructive in the same words as HR2, and ghost as "available but not recommended"

## These limits go into the system file with the rules

- the rules were developed against these 32 scenarios over 4 wheels, so they are untested on buttons they were not written for
- in run 3, 3 of 30 answers called 'Revert to original' in an image editor destructive
- that scenario says "several crops and filters", but not how many, so the amount lost is unclear
- Grok 4.3 called 'Export CSV' or 'Archive project' ghost in 2 or 3 answers in every run, as optional extras or side tasks
- Haiku 4.5 missed the same 6 answers in every run, on 'Discard changes' and on 'Archive project' alone
- the names HR, NR and P have not been tested on their own

## The wheel 001 and 002 posts need a note about the examples

These notes would go under 'Changes to this post', once the designer approves them:

- wheel 001: "9 October 2026: wheel 004 tested these rules without their examples, some of which named test buttons. Opus 5.5 then scored 81 of 87, not 87. Part of the result came from matching button labels."
- wheel 002: "9 October 2026: wheel 004 tested these rules without their examples, some of which named test buttons. 9 of the 10 models then missed 69 of 783 answers, not 27. Part of the result came from matching button labels."

## A reset is destructive when much would be lost

In run 2, GPT-6 Astra called 'Reset to defaults' on a profile settings page secondary in 2 of 3 tries. It would not assume that the reset is "rarely needed", which HR10 requires.

Looking at that miss, the designer found a second problem in HR10. It says the action "cannot cause permanent loss", but not loss of what. A reset does not lose the settings themselves: every switch and slider is still there. It does lose the user's configuration, the values they chose. With a few settings, the user can set them again in a moment. With many switches and sliders, they may not remember what they had, so the loss is permanent in practice. HR2 and HR3 had the same gap.

On 9 October 2026 the designer decided that the answer depends on how much would be lost:

- resetting a few choices the user can remember and make again is not destructive, and HR10 can make it ghost
- resetting a large custom configuration that the user would have to rebuild from memory is destructive, under HR2

The designer approved the wording of HR2, HR3, HR10 and both reset scenarios, and run 3 tested them. Both reset scenarios were right on every model, every time.

## What this does not justify

- a claim that the rules work on buttons they were not written for
- a claim that small models can apply these rules reliably, since Haiku 4.5 missed 6 in every run
- a claim that run 2's change to P5 caused the split on 'Reset to defaults'; 2 tries cannot tell it apart from variation
- any claim about layouts, patterns or other components

## What carries forward

- test the rules on buttons they were never written for, as parked in `QUESTIONS.md`
- the designer can decide how much 'Revert to original' loses, as for the resets
- every rule change runs on all scenarios before it is accepted; in run 3, a change for the resets moved 'Revert to original'
