# Implications for the system

## Proposed rules

- button variant guidance is written as hard rules with a precedence order for conflicts, not as prose descriptions with examples; `runs/2026-10-07-opus-5-5-medium/` showed 76 of 81 correct with rules against 64 of 81 with prose
- a variant encodes how much the product recommends an action, nothing else; this definition let the agent flag a press-and-hold control as outside the system in 3 of 3 runs, where both other levels forced a variant
- the system states that 'none' is a valid answer and says when to use it; across 243 answers the agent never used it as an escape hatch

## Rules to add before this wheel's rule set enters `system/`

The rule set in `experiment/levels/C-machine-rules.md` has one gap, shown by 5 of its 5 misses. It does not say when a legitimate alternative is ghost rather than secondary. A candidate rule is: an alternative that bypasses or exits the current task, rather than completing it another way, is ghost. This rule is untested and must be run before it is adopted.

## What this does not justify

- any claim about other models; one model was tested
- any claim about other components; the rules cover buttons only
- the answer key as good design; it records one designer's judgement, and 'Log out' and 'Skip for now' are cases where the agent's alternative reading was defensible
- a claim that human documentation is bad in general; the documentation tested was written by us in the style of a typical design system site, not taken from a real one
- a claim about low reasoning effort; medium effort was used throughout
