# 001: button variant

**Status:** answered
**Started:** 2026-10-07

## Question

Can an AI agent consistently choose the correct button variant using only machine-readable design system rules?

## Why it matters

Agents building UI today pick button variants from prose documentation or from habit. When they get it wrong, every screen carries a different idea of what matters most. If a small set of written rules fixes this for buttons, the same approach may work for larger choices.

## Boundary

**In scope**

- 4 variants: primary, secondary, ghost and destructive, plus 'none' for a control the system does not cover
- 27 written scenarios, each a button in a described context, with one correct answer fixed before the runs
- 3 ways of describing the system to the agent: names only, typical human documentation, and machine-readable rules
- one model, Claude Opus 5.5, at medium reasoning effort

**Out of scope**

- other components, layouts or patterns
- visual rendering: the agent names a variant, it does not draw one
- other models or agents (a later wheel)
- whether the answer key itself is good design; it records one designer's judgement

## Success criteria

- the wheel is answered "yes" if machine-readable rules score at least 90% accuracy and beat human documentation by 10 points or more
- the wheel is answered "no" if machine-readable rules do no better than human documentation, or if the agent gets the original scenario right and its reworded pair wrong (matching words, not applying rules)
- abandon if the agent cannot return a usable answer for most scenarios at any level
