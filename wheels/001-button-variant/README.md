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
- 29 written scenarios, 27 in run 1, each a button in a context with one correct answer fixed before the run
- 3 ways of describing the system to the agent: names only, typical human documentation, and machine-readable rules
- one model, Claude Opus 5.5, at medium reasoning effort, run 3 times on 7 October 2026

**Out of scope**

- other components, layouts or patterns
- visual rendering: the agent names a variant, it does not draw one
- other models or agents (a later wheel)
- whether the designer's answers are themselves good design; they record one designer's judgement

## Success criteria

- the wheel is answered "yes" if machine-readable rules score at least 90% accuracy and beat human documentation by 10 points or more
- the wheel is answered "no" if machine-readable rules do no better than human written documentation
- it is also answered "no" if the agent gets an original scenario right and its reworded pair wrong, which means it matched words
- abandon if the agent cannot return a usable answer for most scenarios at any level
