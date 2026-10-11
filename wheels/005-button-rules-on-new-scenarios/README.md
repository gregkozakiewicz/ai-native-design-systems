# 005: button rules on new scenarios

**Status:** proposed
**Started:** 2026-10-11

## Question

Do the button rules in `system/` give the designer's answers on 24 scenarios they were not written for?

## Why it matters

The button rules were changed over 4 wheels against the same 32 scenarios. Run 3 of wheel 004 got 948 of 960 answers right, but the rules may only work on the buttons they were tuned on. `system/button-variant.md` lists this as a known limit.

If the rules hold on new buttons, the 98.8% is a property of the rules, not of the scenarios. If they do not, the misses show which rules only worked on the cases they were written for.

## Boundary

**In scope**

- the rules in `system/button-variant.md`, sections 1 to 5, unchanged, with the same answer format as wheel 004's run 3
- 24 new scenarios, from products the 32 scenarios do not cover, in `experiment/scenarios.md`
- every hard rule, HR1 to HR12, tested by at least 2 scenarios
- 4 scenarios where 2 rules apply, and 2 where the answer is 'none'
- 4 models: Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 and GPT-6 Astra
- 3 repeats for each scenario, at the settings used in wheel 004: 288 answers

The 4 models are the ones most people building with Claude Code and Codex use. Wheels 002 and 004 tested the rules on 10 models from 4 companies. Gemini and Grok are left out of this wheel to save time and cost, and the post must say so.

Claude Haiku 5.5 is new, so it has no wheel 004 score. Before the main run, it runs once on wheel 004's 32 scenarios with run 3's rules: 96 answers. That gives it the same starting point as the other 3 models.

**Out of scope**

- any change to the rules; if a rule fails, the change goes in `implications.md` for a later wheel
- names only and human written documentation
- Gemini 3.1 Pro, Gemini 3.8 Flash, Grok 4.7, Grok 4.3, GPT-5.6 sol, Claude Haiku 4.5 and Claude Fable 5.1
- other components

## Before the run

- the designer decides the answer to every scenario, without seeing any model's answer
- confirm that GPT-6 Astra is the model Codex uses by default on 11 October 2026
- confirm the effort setting for Claude Haiku 5.5; Haiku 4.5 ran without one in wheels 002 to 004

## Success criteria

The designer set the bar for 'yes' at more than 95% of answers right, after wheel 004.

- answered 'yes' if more than 95% of the 288 answers are right, that is 274 or more, and no model scores below 65 of 72
- answered 'partly' if 245 to 273 of the 288 answers are right, naming the scenarios that miss and the rules they test
- answered 'no' if fewer than 245 of the 288 answers are right, which is below 85%
- also answered 'no' if more than one model misses every repeat of the same scenario, which shows a question the rules do not answer
- abandon if a model cannot run at the same settings as in wheel 004

If Claude Haiku 5.5 scores below 90 of 96 on wheel 004's scenarios, its result in this wheel is reported separately from the other 3.
