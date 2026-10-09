# Questions

The parking lot. Anything can land here. Nothing here is a commitment.

A question is ready to become a wheel when you can write all three of:

1. **Boundary.** What is in scope and, more importantly, what is out.
2. **Test.** Something you can run, with an agent, that produces a result.
3. **Done.** How you will know the answer, including "no".

Move a question to `wheels/` with `tools/new-wheel.sh` once it has all three.

## Candidate wheels (small enough to start)

- What is the smallest piece of information an agent needs to reliably
  choose the correct **UI pattern** for a given task?
- How should an agent decide whether to **reuse** an existing component or
  **create** a new one?
- What does a component need to tell an agent that current component
  documentation does not?

- Does matching the names models already expect (Switch, Box, TextField,
  spacing) do more for compliance than writing guidance? *(from the reading note
  `research/notes/2026-10-06-measuring-agent-use-of-a-design-system.md`)*
- If an agent can ask the design system a question mid-task, what, if
  anything, still has to be told to it up front? *(from the same reading note)*

## Big questions (too large; here so they stop nagging)

- What is an AI-native design system?
- What replaces component documentation when the reader is a model?
- Does a design system for agents still need a visual layer, or only rules?

## Answered

Move questions here once a wheel has findings, with a link to the wheel.

- Can an AI consistently choose the correct **button variant** using only
  machine-readable system rules? Yes: 87 of 87 with rules, 63 of 87 with
  prose, 54 of 87 with names alone (run 3). See `wheels/001-button-variant/`.

- Does the same button rule set hold for other models? Yes: 9 models from
  4 companies score 80 to 87 of 87 with rules, against 60 to 73 with prose.
  See `wheels/002-other-models/`.

- Can the 3 open readings in the button rules be closed with 3 sentences?
  No: misses rose from 32 to 40. See `wheels/003-three-missing-rules/`.

- Do rewritten button rules, with no examples that name test buttons, give
  the designer's answers on 10 models? Yes: run 3's rules got 948 of 960
  answers right, 98.8%, and 5 of 10 models scored 96 of 96. See
  `wheels/004-new-button-rules/`.

## Raised by wheels

- What makes 'Discard changes' destructive but 'Reset to defaults' and
  'Revert to original' ghost, in words a rule can hold? *(from wheel 003)*
- Does H8 cover declining an upgrade, or only choices the law requires?
  *(from wheel 003)*
- Does the step 5 sentence from wheel 003 work on reversible actions it does
  not name, such as 'Duplicate project' on a project page? The models used it
  only on the 3 buttons it names. *(from wheel 003)*
- Why does Haiku 4.5 read a typed report as "choices the user can make
  again", and does HR2 need to say what content is? *(from wheel 004)*
- Should P5's 2 halves be one test, so a model cannot stop at "the user did
  not come to this view"? *(from wheel 004)*
- Does HR11's "adds something optional" need a limit? It caught 'Export
  CSV' and 'Archive project' on Grok 4.3. *(from wheel 004)*
- Do the new names HR, NR and P change answers on their own? *(from wheel 004)*
- Is refusing to guess when the system is silent a property to design for?
  5 of 9 models do it by default. *(from wheel 002)*

- Does the lead for rules over prose shrink at low reasoning effort?
  *(from wheel 001)*
- Where is the line between a secondary alternative and a ghost option, and
  can it be one rule? *(from wheel 001; answered in run 2 by rule H12,
  12 of 12 correct)*
- How should a scenario or a rule state whether an action can be undone,
  so the agent does not have to assume? *(from wheel 001, scenario 17)*
