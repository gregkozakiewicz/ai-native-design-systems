# Rules plus an automatic check

**Written:** 10 October 2026

## What it is

An idea note, not a reading note. Every wheel so far has tested what an
agent chooses when it is given rules. None has tested what happens when a
check runs after the agent has built something and refuses work that breaks
the system.

The idea has 4 parts:

- spec files kept in the repo next to the code, which the agent reads at the
  start of every session, so the rules change in the same commit as the
  components
- a closed set of tokens in 3 layers: the system's own values, project names
  that point at them, and components that use only the project names
- a script that finds raw values (a hex colour, a pixel size) where a token
  exists, names the token to use, and fails the build
- a warning when the upstream design system changes in a way the specs may
  not cover yet

## What is useful here

- specs should describe how to build the next thing, not only list what
  exists. That is close to the candidate question on what component
  documentation does not tell an agent
- a small, accurate spec layer for the components that really exist beats a
  complete one that goes stale
- written rules and a check do different jobs. The rules say what to do. The
  check catches what the agent did anyway

## What it does not cover

- a check can tell that a colour is a raw value. It cannot tell that a
  button should have been destructive. A wrong variant built entirely from
  tokens passes every check. Wheels 001 to 004 measure that kind of choice,
  and a check does not replace them
- whether the agent's work is consistent from one session to the next is
  a claim until someone measures it: same tasks, several sessions, with and
  without the check
- a check only helps when the right token exists. When it is missing, the
  agent has to invent one or break the rule, and nothing here says which

## Which wheel or question it touches

- candidate wheel on what component documentation does not tell an agent:
  "how to build the next thing" is one answer to test
- new question parked in `QUESTIONS.md`: does an automatic check stop
  mistakes that rules alone miss, and which kinds
- big question on what replaces component documentation: one answer is
  rules for choices plus a check for values, each doing a job the other
  cannot
