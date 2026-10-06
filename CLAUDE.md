# Mila — read this before touching anything

Research repo towards an AI-native design system. Greg Kozakiewicz is a
design director, not an engineer: explain in plain language, skip the jargon,
and never assume he wants to read code.

## The method

One bounded question at a time. The repo is organised around **wheels**
(`wheels/NNN-name/`). Each wheel has, in this order:

1. `README.md`: the question, its boundary, and the success criteria.
   Written before anything else. If these are missing, write them, do not
   start experimenting.
2. `hypothesis.md`: what we expect and why.
3. `experiment/`: the test setup. Prompts, fixtures, scoring method.
4. `runs/`: raw agent output, dated, never edited.
5. `findings.md`: what the runs showed. Honest, including failures.
6. `implications.md`: what this means for `system/`. Only this file may
   propose a change to the design system.

`QUESTIONS.md` is the parking lot. Big ideas go there, not into new wheels.

## What not to do

- Do not create a wheel for an unbounded question. Park it in `QUESTIONS.md`
  and help shrink it first.
- Do not edit anything in `runs/`. Re-run instead.
- Do not add a rule to `system/` without naming the wheel that proved it.
- Do not reorganise the repo. The folder layout is part of the method.

## Related work

Sibling repos in `~/codework`: `roast-my-design-system` (scores a repo as an
environment for AI-generated UI) and `guard-my-design-system`. Mila is the
forward-looking research counterpart; findings here may feed those tools.
