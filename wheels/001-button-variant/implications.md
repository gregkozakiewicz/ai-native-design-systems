# Implications for the system

## Proposed rules

- button variant guidance is written as hard rules with a precedence order for conflicts, not as prose descriptions with examples; run 1 showed 76 of 81 correct with rules against 64 of 81 with prose, run 2 showed 84 of 87 against 66 of 87, and run 3 showed 87 of 87 against 63 of 87
- an alternative that exits or bypasses the current task is ghost, and one that completes the task another way is secondary (rule H12); run 2 showed 12 of 12 correct on the 4 scenarios that test it, and 6 of 6 of those answers went against the convention the agent used without rules
- every scenario, and every rule that depends on whether an action can be undone, must state that fact; 'Remove member' did not, and the agent made opposite assumptions in run 1 and run 2, each time saying so
- a variant encodes how much the product recommends an action, nothing else; this definition let the agent flag a press-and-hold control as outside the system in 3 of 3 runs, where both other levels forced a variant
- the system states that 'none' is a valid answer and says when to use it; across 765 answers in 3 runs the agent never used it as an escape hatch

## Rule set status

The 12 rules in `experiment/levels/C-machine-rules.md` are tested on 29 scenarios in run 3 and scored 87 of 87, with every scenario answered the same way in all 3 repeats. The set is in `system/button-variant.md` as the button variant rules, accepted on 7 October 2026 on the strength of run 3, for one model at medium effort.

## What this does not justify

- any claim about other models; one model was tested
- any claim about other components; the rules cover buttons only
- the designer's answers as good design; 'Log out' and 'Skip for now' showed the agent's other reading was defensible
- a claim that human documentation is bad in general; the documentation tested was written by us in the style of a typical design system site, not taken from a real one
- a claim about low reasoning effort; medium effort was used throughout
