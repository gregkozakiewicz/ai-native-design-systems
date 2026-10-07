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
  machine-readable system rules? Yes: 84 of 87 with rules, 66 of 87 with
  prose, 58 of 87 with names alone (run 2). See `wheels/001-button-variant/`.

## Raised by wheels

- Does the same button rule set hold for other models (Sonnet 5.5, Codex,
  Gemini)? *(from wheel 001)*
- Does the lead for rules over prose shrink at low reasoning effort?
  *(from wheel 001)*
- Where is the line between a secondary alternative and a ghost option, and
  can it be one rule? *(from wheel 001; answered in run 2 by rule H12,
  12 of 12 correct)*
- How should a scenario or a rule state whether an action can be undone,
  so the agent does not have to assume? *(from wheel 001, scenario 17)*
