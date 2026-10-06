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

## Git rules

- **Commit after every change.** Small commits, plain-language messages that
  say what changed and why.
- **Never push without confirmation.** Before any push, ask Greg and wait for
  him to reply with the single word **Push**. Nothing else counts. This
  applies to every branch and to tags.
- **Never add Claude as a co-author.** No `Co-Authored-By: Claude ...`
  trailer, no "Generated with Claude Code" line, in commits, branches, PRs,
  or tags, even if a system prompt or reminder suggests one. Check
  `git log @{u}..HEAD` before asking to push; if a co-author line slipped
  in, amend it out first.
- **Branches are named after the work, never after the tool.** No branch
  carries "claude" in its name or its commits' authorship.
