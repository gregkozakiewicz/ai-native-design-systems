# Implications for the system

## Proposed rules

- button variant guidance is written as hard rules with a precedence order for conflicts, not as prose with examples
- rules beat prose in all 3 runs, by 12 to 24 correct answers
- an alternative that exits or bypasses the current task is ghost, and one that completes it another way is secondary (rule H12)
- in run 2, H12 was right in 12 of 12 answers on the 4 scenarios that test it
- 6 of 6 of those answers went against the convention the agent used without rules
- every scenario, and every rule that depends on whether an action can be undone, must state that fact
- 'Remove member' did not, and the agent made opposite assumptions in runs 1 and 2, saying so each time
- a variant encodes how much the product recommends an action, nothing else
- this definition let the agent flag a press-and-hold control as outside the system in 3 of 3 runs
- both other levels forced a variant onto that control
- the system states that 'none' is a valid answer and says when to use it
- across 765 answers in 3 runs, the agent never used 'none' as an escape hatch

## Rule set status

The 12 rules in `experiment/levels/C-machine-rules.md` were tested on 29 scenarios in run 3 and scored 87 of 87. Every scenario was answered the same way in all 3 repeats. The set is in `system/button-variant.md` as the button variant rules. It was accepted on 7 October 2026 on the strength of run 3, for one model at medium effort.

## What this does not justify

- any claim about other models; one model was tested
- any claim about other components; the rules cover buttons only
- the designer's answers as good design; 'Log out' and 'Skip for now' showed the agent's other reading was defensible
- a claim that human written documentation is bad in general
- we wrote the human written documentation ourselves, copying the style of a typical design system site rather than a real one
- a claim about low reasoning effort; medium effort was used throughout
