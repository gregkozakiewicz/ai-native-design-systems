# Written rules let an agent pick the right button every time

With 12 written rules, Claude chose the correct button variant in 87 of 87 answers, against 63 of 87 with typical human written documentation.

**Wheel:** `wheels/001-button-variant/` · **Runs dated:** 7 October 2026 · **Status:** answered

| 87 of 87 | 63 of 87 | 54 of 87 | 29 of 29 |
| --- | --- | --- | --- |
| correct answers with machine-readable rules | correct answers with human written documentation | correct answers with variant names only | scenarios answered the same way in all 3 repeats, with rules |

## The question

Can an AI agent consistently choose the correct button variant using only machine-readable design system rules? Agents building user interfaces today choose variants from human written documentation, conventions learned in training, or what they learned from the project's code repository. When they choose wrongly, their button choices can make the wrong actions look most important.

**In scope:** 29 written scenarios and 4 button variants, primary, secondary, ghost, and destructive. A fifth option, 'none', lets the agent reject all 4 or say it does not know.
**Out of scope:** other components, visual rendering, other models.

## The answer

Yes. When given the rules, Claude Opus 5.5 got every one of 87 answers right and gave the same answer every time it was asked. When given documentation written the way design system owners usually write it, it got 63 of 87. It also changed its mind between repeats on 3 of 29 scenarios. Based on one model, one component, and one designer's decision, the result says nothing yet about other models or larger choices.

## One example

The agent sees a short instruction, the reference text for its level, and one scenario. This is scenario 21, as seen by the agent.

**The task**

```
Context: A chat app message composer. The user presses and holds this
button to record a voice message, and releases it to send.
Button label: "Hold to record"

Which variant should this button use?
```

**Without rules** (level A, the 4 variant names and nothing else)

```
primary

The reference only names the four variants and gives no usage rules, so I
chose primary because recording and sending a voice message is the
composer's main action; this is a judgment call rather than a documented
guideline.
```

The agent forced a press-and-hold control into a variant made for taps, in 3 of 3 repeats. The correct answer is 'none'.

**With rules** (level C)

```
none

Per precedence step 2 and the never rule, a press-and-hold control is not a
plain click or tap, so no variant applies and it should be flagged as none.
```

The rules say what a variant is for, so the agent could tell this control falls outside them, in 3 of 3 repeats. Full output: `runs/2026-10-07-opus-5-5-medium-run3/`.

## What we found

### Rules beat human written documentation by 28 points and names alone by 38

Each of the 29 scenarios was sent to the model 3 times at each of 3 levels. Only the reference text changed between levels.

```
names only                   ████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░  54 of 87
human written documentation  ██████████████████████████████████████████████░░░░░░░░░░░░░░░░░░  63 of 87
machine rules                ████████████████████████████████████████████████████████████████  87 of 87
```

| Level | What the agent was given | Correct answers | Scenarios with 3 identical answers |
| --- | --- | --- | --- |
| A | the 4 variant names and 'none' | 54 of 87 | 26 of 29 |
| B | a description and examples per variant, 3 soft guidelines | 63 of 87 | 26 of 29 |
| C | what a variant means, 12 hard rules, 5 never rules, an order for conflicts | 87 of 87 | 29 of 29 |

The 29 scenarios fall into 6 groups, from obvious controls to deliberate traps. All 3 levels got every control right, so the gap between the levels comes from the other 5 groups.

| Scenario group | What it tests | Names only | Human written documentation | Rules |
| --- | --- | --- | --- | --- |
| Controls, 5 scenarios | obvious cases, such as 'Create account' on a sign-up form | 15 of 15 | 15 of 15 | 15 of 15 |
| Context, 7 scenarios | the answer depends on what sits around the button, such as 'Cancel' next to 'Delete project' | 12 of 21 | 16 of 21 | 21 of 21 |
| Traps, 4 scenarios | the button sounds like one variant but is another, such as 'Log out', which is not destructive | 6 of 12 | 6 of 12 | 12 of 12 |
| Conflicts, 4 scenarios | 2 rules apply and one must win, such as 'Discard changes' in a dialog that also offers 'Save' | 10 of 12 | 11 of 12 | 12 of 12 |
| Interaction and tools, 3 scenarios | a press-and-hold control, and side tasks such as 'Add file' in a chat composer | 1 of 9 | 3 of 9 | 9 of 9 |
| Matched pairs, 6 scenarios | earlier scenarios reworded, to test the same rule with different words | 10 of 18 | 12 of 18 | 18 of 18 |

These figures come from run 3 of 3. Runs 1 and 2 are described further down, under the heading about the 3 runs.

### The agent recognised the situation, not the wording

The risk with written rules is that the agent spots the rule's words in the scenario and copies the answer. So 6 scenarios reword a rule that another scenario tests directly, with no words in common. 'Try again' after a failed upload is paired with 'Update card' after a declined payment. With rules, all 6 pairs were right in all 3 repeats: 18 of 18. No repeat at any level got the original right and the reworded pair wrong.

### Rules changed answers that convention gets wrong

'Log out' in an account menu was ghost in 6 of 6 answers at levels A and B. The designer's answer is secondary: it is a real action the user chose, not a low-emphasis extra. With rules it was secondary in 3 of 3. The rules did not make the agent cleverer; they replaced the convention it falls back on with the designer's decision.

### It took 3 runs, and every fix was to the rules or the scenarios

| Run | Scenarios | Rules | Correct with rules | What the misses showed |
| --- | --- | --- | --- | --- |
| 1 | 27 | 11 | 76 of 81 | the rules did not say when an alternative is ghost rather than secondary |
| 2 | 29 | 12 | 84 of 87 | one scenario did not say whether the action could be undone |
| 3 | 29 | 12 | 87 of 87 | no misses |

We recorded each change before the next run. Earlier runs keep their original scores, even where we later changed a correct answer. The misses with rules were not random. In each run they had one cause, which the agent named in its own reasons. One change fixed it.

### Where it failed

- with human written documentation, the agent changed its answer between repeats on 3 of 29 scenarios
- one repeat on 'Close' wrote "one could argue for Secondary", then chose primary
- with human written documentation, 'Revert to original' was called destructive in 3 of 3 repeats, because redoing edits by hand "is not an undo"
- our level B first contained a line that gave away scenario 21; we removed it before the first full run
- our scenario 17 did not say whether removing a member could be undone
- the agent made opposite assumptions about scenario 17 in runs 1 and 2, and said so each time

## What this does not show

- one model, Claude Opus 5.5 at medium reasoning effort; other models and lower effort are untested
- one component; nothing here says rules work for layouts, patterns, or whole screens
- the correct answers are one designer's judgement, and the designer changed one of them after seeing the agent's reasoning
- we wrote the human written documentation ourselves, copying the style of a typical design system site rather than a real one
- the agent names a variant; it does not render a button, so nothing is claimed about the result on screen

## What to do with this

1. Write your button variant guidance as rules with IDs, and say which rule wins when 2 apply.
2. Say what a variant means, so the agent can tell when a control falls outside the system.
3. Give the agent 'none' as a valid answer; in 765 answers across 3 runs it never used it as an escape hatch.
4. Test rules with reworded scenarios, so you know the agent applies them rather than matching words.

The 12 rules in `wheels/001-button-variant/experiment/levels/C-machine-rules.md` are proposed for `system/` on the strength of run 3.

## Details

**How we tested**

| Setting | Value |
| --- | --- |
| Models | Claude Opus 5.5, through the Anthropic application programming interface (API), at medium reasoning effort |
| Information levels | the reference text only: names, human written documentation, or machine-readable rules |
| Scenarios | 29, in `experiment/scenarios.md`, grouped as controls, context, traps, conflicts, interaction, and matched pairs |
| Repeats | 3 per scenario per level, each a fresh conversation |
| Scoring | mechanical, by `experiment/score.py`, against the correct answers decided before each run |
| Dates | 7 October 2026, 3 runs |
| Cost | about €1 per run in API credit, pay as you go, not a Claude subscription. About €3 for all 3 runs, 765 calls, as our own mistakes meant 2 reruns. |

The designer's answers changed once, after run 1: 'Log out' moved from ghost to secondary. Scenario 17 gained one sentence after run 2. Both changes are recorded in `experiment/scenarios.md`.

**Reproduce it**

- wheel: `wheels/001-button-variant/`
- raw output: `wheels/001-button-variant/runs/`
- scoring and setup: `wheels/001-button-variant/experiment/`

**Questions this raises**

- does the same rule set hold for other models, such as Sonnet 5.5, Codex, and Gemini
- does the lead for rules shrink at low reasoning effort
- how should a scenario or a rule state whether an action can be undone, so the agent does not assume

**Changes to this post**

- 7 October 2026: first version
- 7 October 2026: cost restated in euros as API credit, with the total across all 3 runs
