# Questions

The parking lot. Anything can land here. Nothing here is a commitment.

A question is ready to become a wheel when you can write all three of:

1. **Boundary.** What is in scope and, more importantly, what is out.
2. **Test.** Something you can run, with an agent, that produces a result.
3. **Done.** How you will know the answer, including "no".

Move a question to `wheels/` with `tools/new-wheel.sh` once it has all three.

## Candidate wheels (small enough to start)

- Can an AI consistently choose the correct **button variant** using only
  machine-readable system rules? *(smallest; good first wheel)*
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
