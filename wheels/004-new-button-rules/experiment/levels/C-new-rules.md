# Button variant rules (machine-readable)

Follow this file literally. Where rules conflict, apply the precedence order in section 4.

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
    intent: available but not recommended
  destructive:
    intent: permanently removes content people created, which would have to be recreated from memory
  none:
    intent: no variant applies; flag it instead of forcing one
```

## 2. Hard rules (must hold)

```yaml
hard_rules:
  - id: HR1
    rule: at most one primary per view (a page, dialog, banner or composer is one view)
  - id: HR2
    rule: an action that permanently removes content people created, which would have to be recreated from memory, is destructive, even if it is the main action of the view
  - id: HR3
    rule: an action is never destructive if it can be undone later, or if all it removes are choices the user can make again from the options on screen
  - id: HR4
    rule: the button that backs out of a dialog without acting is always secondary; a button that postpones a decision follows HR12 instead
  - id: HR5
    rule: a button that only closes something that asks the user for no decision is secondary, even when it is the only button; primary is reserved for actions that move the user forward
  - id: HR6
    rule: a button that is repeated on every item in a list or grid is ghost, never primary or secondary
  - id: HR7
    rule: when two actions are equally important answers to the same decision, the positive or forward-moving one is primary and the other is secondary; never two primaries
  - id: HR8
    rule: when the view asks the user to decide on a recommended option, the recommended option is primary and the button that declines it is secondary; it must remain a visible button, never ghost; a button that postpones a decision follows HR12 instead
  - id: HR9
    rule: when something has failed and there is one clear recovery action, that action is primary wherever it appears
  - id: HR10
    rule: an action that undoes the user's own edits, is rarely needed and cannot cause permanent loss, is ghost
  - id: HR11
    rule: an action that opens a side task, leads to further information, or adds something optional to the current task, rather than completing it, is ghost
  - id: HR12
    rule: an alternative that postpones or skips the current step, leaving the decision for later, is ghost; an alternative that completes the task another way is secondary
```

## 3. Never rules

```yaml
never:
  - id: NR1
    rule: primary for a button that backs out, dismisses something, or skips a step
  - id: NR2
    rule: destructive for anything the user can reverse
  - id: NR3
    rule: two primary buttons in the same view
  - id: NR4
    rule: ghost for an action the user must be able to find to complete the task
  - id: NR5
    rule: a variant for a control that is not a plain click or tap: answer none
```

## 4. Precedence (when rules conflict)

Apply in this order; the first rule that applies wins.

- **P1: Reversibility**. Can it be undone? Decides destructive vs not (HR2, HR3).
- **P2: Interaction**. Is it a plain click or tap? If not, answer none.
- **P3: Role in the view**. Does it back out of a dialog, close something that asks for no decision, repeat on every item, postpone or skip a step, undo the user's own edits, open a side task, lead to further information, or add something optional? (HR4, HR5, HR6, HR10, HR11, HR12)
- **P4: Recommendation**. Is it the one action the product recommends? (HR1, HR7, HR8, HR9) When an action is the only one in the main area of a view, and no role rule applies, it is primary. It counts as the one action the product recommends, even if it does not move the user forward. A page header is part of the main area; navigation, menus and footers are not.
- **P5: Emphasis**. Anything left: if the user came to the view to do it, or may reasonably do it there, it is secondary, even if most users never take it. Otherwise it is ghost.

## 5. Unknowns

Anything not covered above is intentionally undefined. Choose the closest variant using the precedence order and say which rule you applied. If no rule applies at all, answer none.

## 6. Answer format

Answer with exactly one of: `primary`, `secondary`, `ghost`, `destructive`, `none`, followed by one line naming the rule you applied.
