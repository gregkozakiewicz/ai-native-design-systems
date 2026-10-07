# Written rules let an agent pick the right button every time

With 12 written rules, Claude chose the correct button variant in 87 of 87 answers. With typical human written documentation it managed 63 of 87.

**Wheel:** `wheels/001-button-variant/` · **Runs dated:** 7 October 2026 · **Status:** answered

| 87 of 87 | 63 of 87 | 54 of 87 | 29 of 29 |
| --- | --- | --- | --- |
| correct answers with machine-readable rules | correct answers with human documentation | correct answers with variant names only | scenarios answered the same way in all 3 repeats, with rules |

## The question

Can an AI agent consistently choose the correct button variant using only machine-readable design system rules? Agents building UI today pick variants from prose documentation or from habit. When they get it wrong, every screen carries a different idea of what matters most.

**In scope:** 4 button variants, primary, secondary, ghost and destructive, plus 'none' for a control the system does not cover, across 29 written scenarios.
**Out of scope:** other components, visual rendering, other models.

## The answer

Yes. When given the rules, Claude Opus 5.5 got every one of 87 answers right and gave the same answer every time it was asked. When given documentation written the way design system owners usually write it, it got 63 of 87 and changed its mind between repeats on 3 of 29 scenarios. The evidence covers one model, one component and one designer's decision, so it says nothing yet about other models or larger choices.

## One example

The agent sees a short instruction, the reference text for its level, and one scenario. This is scenario 21, as the agent saw it.

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

The agent forced a press-and-hold control into a variant made for taps, in 3 of 3 repeats. The key says 'none'.

**With rules** (level C)

```
none

Per precedence step 2 and the never rule, a press-and-hold control is not a
plain click or tap, so no variant applies and it should be flagged as none.
```

The rules say what a variant is for, so the agent could tell this control falls outside them, in 3 of 3 repeats. Full output: `runs/2026-10-07-opus-5-5-medium-run3/`.

## What we found

### Rules beat documentation by 28 points and names alone by 38

Each of the 29 scenarios was sent to the model 3 times at each of 3 levels. Only the reference text changed between levels.

```
names only     ████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░  54 of 87
human docs     ██████████████████████████████████████████████░░░░░░░░░░░░░░░░░░  63 of 87
machine rules  ████████████████████████████████████████████████████████████████  87 of 87
```

| Level | What the agent was given | Correct answers | Scenarios with 3 identical answers |
| --- | --- | --- | --- |
| A | the 4 variant names and 'none' | 54 of 87 | 26 of 29 |
| B | a description and examples per variant, 3 soft guidelines | 63 of 87 | 26 of 29 |
| C | what a variant means, 12 hard rules, 5 never rules, an order for conflicts | 87 of 87 | 29 of 29 |

The 5 easy scenarios were right at every level, 15 of 15 each. The whole gap is in the hard ones. Run 3 of 3; runs 1 and 2 are below.

### The agent applied the rules rather than matching their words

The risk with written rules is that the agent spots the rule's words in the scenario and copies the answer. So 6 scenarios reword a rule that another scenario tests directly, with no words in common. 'Try again' after a failed upload is paired with 'Update card' after a declined payment. With rules, all 6 pairs were right in all 3 repeats: 18 of 18. No repeat at any level got the original right and the reworded pair wrong.

### Rules changed answers that convention gets wrong

'Log out' in an account menu was ghost in 6 of 6 answers at levels A and B. The designer's decision says secondary: it is a real action the user chose, not a low-emphasis extra. With rules it was secondary in 3 of 3. The rules did not make the agent cleverer; they replaced the convention it falls back on with the designer's decision.

### It took 3 runs, and every fix was to the rules or the scenarios

| Run | Scenarios | Rules | Correct with rules | What the misses showed |
| --- | --- | --- | --- | --- |
| 1 | 27 | 11 | 76 of 81 | the rules did not say when an alternative is ghost rather than secondary |
| 2 | 29 | 12 | 84 of 87 | one scenario did not say whether the action could be undone |
| 3 | 29 | 12 | 87 of 87 | no misses |

Each fix was written down before the next run, and earlier runs were never rescored. The misses with rules were never random: in each run they were one gap, stated in the agent's own reasons, and one change closed it.

### Where it failed

- with human documentation, the agent changed its answer between repeats on 3 of 29 scenarios; one repeat on 'Close' wrote "one could argue for Secondary", then chose primary
- with human documentation, 'Revert to original' was called destructive in 3 of 3 repeats, because redoing edits by hand "is not an undo"
- our level B first contained a line that gave away scenario 21; we removed it before the first full run
- our scenario 17 did not say whether removing a member could be undone, and the agent made opposite assumptions in runs 1 and 2, saying so each time

## What this does not show

- one model, Claude Opus 5.5 at medium reasoning effort; other models and lower effort are untested
- one component; nothing here says rules work for layouts, patterns or whole screens
- the answers are dictated by designer's judgement, and the designer changed it once after seeing the agent's reasoning
- the human documentation was written by us in the style of a typical design system site, not taken from a real one
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
| Models | Claude Opus 5.5, through the Anthropic API, medium reasoning effort |
| Information levels | the reference text only: names, human documentation, or machine-readable rules |
| Scenarios | 29, in `experiment/scenarios.md`, grouped as easy, context, traps, conflicts, interaction and matched pairs |
| Repeats | 3 per scenario per level, each a fresh conversation |
| Scoring | mechanical, by `experiment/score.py`, against a key fixed before each run |
| Dates | 7 October 2026, 3 runs |
| Cost | about €1 per run in API credit (pay as you go, not a Claude subscription); about €3 for all 3 runs and 765 calls, because our own mistakes in the rules and one scenario meant 2 reruns |

The designer decision answer changed once, after run 1: 'Log out' moved from ghost to secondary. Scenario 17 gained one sentence after run 2. Both changes are recorded in `experiment/scenarios.md`.

**Reproduce it**

- wheel: `wheels/001-button-variant/`
- raw output: `wheels/001-button-variant/runs/`
- scoring and setup: `wheels/001-button-variant/experiment/`

**Questions this raises**

- does the same rule set hold for other models, such as Sonnet 5.5, Codex and Gemini
- does the lead for rules shrink at low reasoning effort
- how should a scenario or a rule state whether an action can be undone, so the agent does not assume

**Changes to this post**

- 7 October 2026: first version
- 7 October 2026: cost restated in euros as API credit, with the total across all 3 runs
