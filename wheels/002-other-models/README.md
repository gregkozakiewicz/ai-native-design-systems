# 002: other models

**Status:** proposed
**Started:** 7 October 2026

## Question

Does the button variant rule set from wheel 001 guide models other than Claude Opus 5.5 as well as it guided Opus?

## Why it matters

Wheel 001 showed that written rules took one model from 54 of 87 to 87 of 87. If that holds only for Opus, the rules are a prompt tuned to one model. If it holds across models from different companies, the rules are a property of the design system, and a team can write them once. Every reader of post 1 will ask this first.

## Boundary

**In scope**

- the 29 scenarios, 3 information levels and answer key from wheel 001, unchanged
- 3 repeats per scenario per level, as before
- at least 3 models besides Opus 5.5: one smaller Anthropic model, one OpenAI model, one Google model, each at its default reasoning setting
- the same 3 measures: accuracy, consistency, over-flagging, plus the matched pairs

**Out of scope**

- changing the rules or scenarios to suit a model; if a model fails, that is the finding
- tuning prompts per model beyond what each API needs to return the same answer format
- rendering, other components, cost comparisons between providers

## Success criteria

- the wheel is answered "the rules travel" if every model scores at least 80 of 87 with rules and the rules beat human documentation by 10 points or more on every model
- the wheel is answered "the rules are Opus-specific" if any model scores below 70 of 87 with rules, or the rules fail to beat human documentation on any model
- anything between is answered "partly", with the per-model gap reported
- abandon if a model cannot be made to return one of the 5 answers for most scenarios
