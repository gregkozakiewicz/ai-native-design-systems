# Rules plus an automatic check

**Written:** 10 October 2026

## What it is

An idea note, not a reading note. Every wheel so far has tested what an
agent chooses when it is given rules. None has tested what happens when a
check runs after the agent has built something and refuses work whose
choices break the rules.

The check reads what the agent built and tests each choice against the
rules. 'Remove member' deletes data, so H2 says it is destructive. If the
agent made it ghost, the check fails and names the rule. It is the same test
the wheels run on scenarios, run instead on real work.

## What is useful here

- written rules and a check do different jobs. The rules say what to do.
  The check catches what the agent did anyway
- the check can only be as good as the rules. Where the rules leave a
  reading open, as in wheels 002 and 003, the check cannot decide either
- spec files kept in the repo next to the code, read at the start of every
  session, change in the same commit as the components, so the rules do not
  go stale

## What it is not

- a check that finds raw values (a hex colour, a pixel size) where a token
  exists is ordinary code hygiene. Every design system can have one, AI or
  not. It never looks at a choice: a wrong variant built entirely from
  tokens passes it. It is not what this research is about
- whether a check makes the agent's work consistent from one session to the
  next is a claim until someone measures it: same tasks, several sessions,
  with and without the check

## Which wheel or question it touches

- new question parked in `QUESTIONS.md`: can a check that tests the agent's
  choices against the rules catch mistakes the rules alone did not prevent
- big question on what replaces component documentation: one answer is
  rules the agent reads before it builds, plus a check on the choices after
