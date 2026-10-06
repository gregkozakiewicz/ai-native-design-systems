# Implications for the system

## Proposed rules

- button variant guidance is written as hard rules with a precedence order for conflicts, not as prose descriptions with examples; `runs/2026-10-07-opus-5-5-medium/` showed 76 of 81 correct with rules against 64 of 81 with prose
- a variant encodes how much the product recommends an action, nothing else; this definition let the agent flag a press-and-hold control as outside the system in 3 of 3 runs, where both other levels forced a variant
- the system states that 'none' is a valid answer and says when to use it; across 243 answers the agent never used it as an escape hatch

## Rules to test before this wheel's rule set enters `system/`

The rule set in `experiment/levels/C-machine-rules.md` had one gap, shown by 5 of its 5 misses in run 1. It did not say when a legitimate alternative is ghost rather than secondary. Rule H12 now says: an alternative that exits or bypasses the current task is ghost; an alternative that completes the task another way is secondary. Scenarios 28 and 29 test it with different wording. H12 is untested until a second run.

## What this does not justify

- any claim about other models; one model was tested
- any claim about other components; the rules cover buttons only
- the answer key as good design; it records one designer's judgement, and 'Log out' and 'Skip for now' are cases where the agent's alternative reading was defensible
- a claim that human documentation is bad in general; the documentation tested was written by us in the style of a typical design system site, not taken from a real one
- a claim about low reasoning effort; medium effort was used throughout
