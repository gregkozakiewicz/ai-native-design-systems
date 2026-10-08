# Button variant

**Proved by:** [wheel 001](../wheels/001-button-variant/), run 3 of 7 October 2026. Claude Opus 5.5 at medium effort chose the designer's answer in 87 of 87 answers, the same answer in all 3 repeats for all 29 scenarios. Human documentation scored 63 of 87 and names alone 54 of 87.

**Scope:** one model, one component. The rules are untested on other models (wheel 002, planned) and say nothing about layouts, patterns or rendering.

**Text:** sections 1 to 5 below are the file the agent was given, with one change: 5 em-dashes in the precedence list are now colons, to meet the repo's writing rule. This was not re-run. The tested file also had a section 6 setting the experiment's answer format; it is not a rule and is left out.

Give this file to an agent as it is. Where rules conflict, the precedence order in section 4 decides.

---

## 1. What a variant means

A variant encodes **how much the product recommends this action**, nothing else. It does not encode colour preference, position or how the control is operated.

```yaml
variants:
  primary:
    intent: the one action the product recommends on this view
    max_per_view: 1
  secondary:
    intent: a real alternative to the primary; a choice the user may reasonably make
  ghost:
    intent: available but not recommended; optional, rare or repeated actions
  destructive:
    intent: removes data or has effects the user cannot undo
  none:
    intent: no variant applies; flag it instead of forcing one
```

## 2. Hard rules (must hold)

```yaml
hard_rules:
  - id: H1
    rule: at most one primary per view (a page, dialog, banner or composer is one view)
  - id: H2
    rule: an action that permanently removes data or cannot be undone is destructive, even if it is the main action of the view
  - id: H3
    rule: an action that can be undone or reversed later is never destructive (log out, archive, reset, unsubscribe)
  - id: H4
    rule: the button that backs out of a dialog without acting (cancel, close, go back) is always secondary
  - id: H5
    rule: a button that only dismisses something is secondary even when it is the only button; primary is reserved for actions that move the user forward
  - id: H6
    rule: a button that is repeated on every item in a list or grid is ghost, never primary or secondary
  - id: H7
    rule: when two actions are equally important, the positive or forward-moving one is primary and the other is secondary; never two primaries
  - id: H8
    rule: when the view presents a recommended option and a legally or ethically equal alternative, the recommended one is primary and the alternative is secondary; the alternative must remain a visible button, never ghost
  - id: H9
    rule: when something has failed and there is one clear recovery action, that action is primary wherever it appears
  - id: H10
    rule: an action that undoes the user's own edits, is rarely needed and cannot cause permanent loss, is ghost
  - id: H11
    rule: an action that opens a side task (attach a file, give feedback, learn more) rather than completing the current task is ghost
  - id: H12
    rule: an alternative that exits or bypasses the current task (skip, not now, maybe later) is ghost; an alternative that completes the task another way is secondary
```

## 3. Never rules

```yaml
never:
  - primary for cancel, close, dismiss or skip
  - destructive for anything the user can reverse
  - two primary buttons in the same view
  - ghost for an action the user must be able to find to complete the task
  - a variant for a control that is not a plain click or tap (hold, drag, toggle, slider): answer none
```

## 4. Precedence (when rules conflict)

Apply in this order; the first rule that applies wins.

1. **Reversibility**: can it be undone? Decides destructive vs not (H2, H3).
2. **Interaction**: is it a plain click or tap? If not, answer none.
3. **Role in the view**: does it back out, dismiss, repeat, bypass, or open a side task? (H4, H5, H6, H11, H12)
4. **Recommendation**: is it the one action the product recommends? (H1, H7, H8, H9)
5. **Emphasis**: anything left: secondary if it is a real choice the user may take, ghost if it is optional and rarely needed.

## 5. Unknowns

Anything not covered above is intentionally undefined. Choose the closest variant using the precedence order and say which rule you applied. If no rule applies at all, answer none.
