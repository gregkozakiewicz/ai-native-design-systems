# 004: rules without button examples

**Status:** proposed
**Started:** 2026-10-08

## Question

Do the 10 models still give the designer's answers when the rules no longer list examples that match the test buttons?

## Why it matters

Several rules give examples in brackets that are the labels of test buttons, such as "skip, not now, maybe later" in H12. A model can match a label to an example instead of reading the situation. Wheels 001 and 002 report 80 to 87 of 87 with rules, and we cannot tell how much of that comes from matching words. If it is a lot, the published posts for wheels 001 and 002 need a note, and the rules need different examples.

## Boundary

**In scope**

- wheel 002's rules file with every example that matches a test button taken out, and nothing else changed
- the examples taken out: H3 "log out, archive, reset, unsubscribe", H4 "cancel, close, go back", H11 "attach a file, give feedback, learn more", and H12 "skip, not now, maybe later"
- the never rule "primary for cancel, close, dismiss or skip" names the role instead: a button that backs out, dismisses something, or skips a step
- the never rule on controls loses its examples "hold, drag, toggle, slider"
- wheel 001's 29 scenarios and correct answers, unchanged
- wheel 002's 10 models at the same settings
- rules only, 3 repeats per scenario per model: 870 answers

**Out of scope**

- the new rules and scenario changes recorded in wheel 003's `implications.md`, which go to wheel 005
- the new names HR, NR and P1 to P5: the rules file keeps wheel 002's names, so the examples are the only change the models see
- names only and human written documentation, which have no examples to take out

## Success criteria

12 of the 29 scenarios have a button whose label appears in an example: 'Add file', 'Archive project', 'Cancel', 'Close', 'Dismiss', 'Hold to record', 'Learn more', 'Log out', 'Not now', 'Reset to defaults', 'Send feedback', and 'Skip for now'. In wheel 002 the models missed 22 of the 360 answers on these 12, and 10 of the 510 answers on the other 17.

- answered "yes, the models read the situation" if misses on the 12 matched scenarios rise by 6 or fewer, to 28 or fewer of 360, and no model loses more than 4 of 87 against wheel 002
- answered "no, the scores relied on matching words" if misses on the 12 matched scenarios rise by more than 20, to over 42 of 360
- answered "partly" for anything in between, naming the scenarios that moved
- if misses on the other 17 scenarios rise by more than 6, report it separately, because taking out examples should not affect them
- abandon if a model cannot run at the same setting as in wheel 002

A rise of 6 allows for variation between runs. In wheel 001, Opus's scores with unchanged names only and unchanged human written documentation moved by 3 to 4 of 87 between runs 2 and 3.
