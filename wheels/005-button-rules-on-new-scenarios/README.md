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
- 24 new scenarios, from products the 32 scenarios do not cover, in `experiment/scenarios.md`: 20 of the first 24, and 4 added on the line between secondary and ghost
- every hard rule except HR9 tested by at least 2 scenarios; HR9 by one
- 8 scenarios where 2 rules apply, and none where the answer is 'none'
- wheel 004's 10 models, with Claude Haiku 5.5 in place of Claude Haiku 4.5: Claude Fable 5.1 at low effort, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, GPT-6 Astra, GPT-5.6 sol, Gemini 3.1 Pro, Gemini 3.8 Flash, Grok 4.7 and Grok 4.3
- 3 repeats for each scenario, at the settings used in wheel 004: 720 answers

On 13 October 2026 the designer chose all 10 models over the 4 behind Claude Code and Codex, to use the credit left on Google and xAI. The estimated cost is about €2.50.

Claude Haiku 5.5 is new, so it has no wheel 004 score. Before the main run, it runs once on wheel 004's 32 scenarios with run 3's rules: 96 answers. That gives it the same starting point as the other 9 models.

**Out of scope**

- any change to the rules; if a rule fails, the change goes in `implications.md` for a later wheel
- names only and human written documentation
- Claude Haiku 4.5, replaced by Claude Haiku 5.5
- other components

## Changed before the run

On 13 October 2026, before any model ran, the designer removed 4 scenarios that are not clearly buttons or test what 'none' means: 'Go to field', 'Read tips', 'Set temperature' and 'Slide to pay'. The designer added 4 on the line between secondary and ghost: 'Save for later', 'Copy link', 'Add to wishlist' and 'Send test email'. The total stays at 24.

## Scored against 3 sets of answers

The main score is against the designer's answers, as the success criteria below say. The findings also report 2 other comparisons, because the designer's answers differ from what the rules give on 11 of the 24 scored scenarios:

- the answers the rules give when read in order, in `experiment/draft-answers.md`, which shows whether the models apply the rules correctly
- the most common answer from designers in the designer judgement portal, once at least 5 have answered a scenario

## Before the run

- the designer decides the answer to every scenario, without seeing any model's answer
- confirm the effort setting for Claude Haiku 5.5; Haiku 4.5 ran without one in wheels 002 to 004

## Success criteria

The designer set the bar for 'yes' at more than 95% of answers right, after wheel 004.

- answered 'yes' if more than 95% of the 720 answers are right, that is 685 or more, and no model scores below 65 of 72
- answered 'partly' if 612 to 684 of the 720 answers are right, naming the scenarios that miss and the rules they test
- answered 'no' if fewer than 612 of the 720 answers are right, which is below 85%
- also answered 'no' if more than one model misses every repeat of the same scenario, which shows a question the rules do not answer
- abandon if a model cannot run at the same settings as in wheel 004

If Claude Haiku 5.5 scores below 90 of 96 on wheel 004's scenarios, its result in this wheel is reported separately from the other 9.
