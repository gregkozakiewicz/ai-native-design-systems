# <Title: the finding as a statement, 65 characters or less, sentence case>

<!--
How to use this template

Copy it for any post we publish during the research phase. Each post is one
reading of one wheel. The wheel folder holds the full discipline
(README.md, hypothesis.md, experiment/, runs/, findings.md,
implications.md). The post is the readable version of it, so it stays
short: the reader gets the result in the first screen and the detail at the
bottom.

Write to the rules in the 'Writing' section of CLAUDE.md. They are the only
writing rules, so this template does not repeat them. Text in angle brackets
is a prompt to you: replace it or delete it. Delete every comment before
publishing.

Visual rules for the published page
- build the page by copying the newest wheel page in gkwebsite, so it keeps the same styles; as of 8 October 2026 that is wheel 001
- the summary runs the full content width
- the 4 numbers under the title render as tiles, not a table, each with a bar showing the score out of its total
- a line sits above and below the tiles, with a small gap before the question and answer card
- "The question" and "The answer" render side by side in one white card with an accent edge, with the first word of the answer in large accent type, and "In scope:", "Out of scope:", and "Based on:" in bold
- at least one chart in "What we found", with its data table beside or under it
- in "What we found", each finding has generous space above its heading, and charts and tables have space above and below so they do not run into the text
- a table with long descriptions puts each description under its row name, so the table keeps 4 columns or fewer on a phone
- the example renders as before and after, side by side where the width allows
- "What to do with this" renders as a dark panel, straight after "What we found", headed "Use these <n> steps in your own design system"
- "Details" is collapsed or visually lighter than the rest
- body text keeps the line-heights of the reference page, which are 10% below the site's original
-->

<Summary: one sentence with a verb, ending in a full stop. It says what we
found, not what the post is about. 160 characters or less so it survives a
link preview.>

**Wheel:** `wheels/NNN-name/` · **Runs dated:** YYYY-MM-DD · **Status:** answered | partial | abandoned

| <Number> | <Number> | <Number> | <Number> |
| --- | --- | --- | --- |
| <what it counts, with the denominator> | <what it counts, with the denominator> | <what it counts, with the denominator> | <what it counts, with the denominator> |

<!--
These 4 numbers are the whole post for a reader who stops here. Each is a
number plus what it is a number of: "41 of 69 runs", not "59%". Every number
here appears again below, next to its evidence. Nothing here that is not
proven below.
-->

## The question

<The hook. One sentence, copied from the wheel's README.md, then one or two
sentences on what breaks today because it is unanswered. If the question
needs two sentences, it is two posts.>

**In scope:** <one line>
**Out of scope:** <one line>

## The answer

<Start with "Yes.", "No." or "Partly." on its own, because it renders large
on the page. Then two or three sentences that answer the question directly.
A reader who stops here knows the result and its limit.>

**Based on:** <what the evidence covers, such as one model and one component. Then one sentence on what it does not say.>

## One example

<One scenario exactly as the agent saw it, then what the agent did without
help and what it did with help. One line of explanation under each. Full
output lives in runs/, linked here. If you trim anything, say what was cut.>

**The task**

```
<the prompt, verbatim>
```

**Without <the thing we are testing>**

```
<the output, verbatim or trimmed>
```

<One sentence: what went wrong and the score.>

**With <the thing we are testing>**

```
<the output, verbatim or trimmed>
```

<One sentence: what changed and the score. Link: `runs/YYYY-MM-DD-...`.>

## What we found

<!--
2 to 4 findings. The heading is the finding as a statement ("Guidance moved
one model by 24 points and another by 6"), never a topic ("Results") and
never a question. Order by importance.

Under each heading: the claim in one or two sentences, one chart or table
with denominators, then one sentence on what it does not show and which
runs it comes from.

If the scenarios fall into groups, show the groups in a table before any
sentence refers to them: what each group tests, with one example, and the
result at each level. Never name a group, such as 'control scenarios', that
the reader has not been shown.
-->

### <Finding 1 as a statement>

<Claim.>

| <Level or model> | <Measure, n of N> | <Measure, n of N> |
| --- | --- | --- |
| | | |

<What this does not show. Runs: `runs/YYYY-MM-DD-...`.>

### <Finding 2 as a statement>

<Same shape.>

### <Where it failed>

<One line each: what went wrong, how often, where to look. Include our own
setup's failures, not only the agent's.>

## What to do with this

<For a reader with their own design system. Two to four steps, in order,
each one sentence, each tied to a finding above. If the honest answer is
"nothing yet", say so and say what would change that.>

1. <step>
2. <step>

<One line on what changes in `system/`, if anything, with the rule from the
wheel's implications.md and the run that justifies it. Otherwise "Nothing
changes in the system yet."

## What this does not show

<The honest list, one sentence each: sample size, one system, one model,
levels that bundle two changes, scoring that depends on a model, anything
anonymised and why. Nothing claimed about a fix without a measurement of
the fix.>

- <limit>
- <limit>

## Details

<!--
Reference material. Keep it, but keep it light and last. Setup instructions
stay in the repo; link to them.
-->

**How we tested**

| Setting | Value |
| --- | --- |
| Models | <name and version, one row each if they differ> |
| Information levels | <what changed between runs, and nothing else> |
| Scenarios | <count, and where they live> |
| Repeats | <runs per scenario per level> |
| Scoring | <who or what scores, against what, written before the runs> |
| Dates | <first and last run> |
| Cost | <money and time, roughly> |

<One sentence on anything fixed before the runs started or changed after.>

**Reproduce it**

- wheel: `wheels/NNN-name/`
- raw output: `wheels/NNN-name/runs/`
- scoring and setup: `wheels/NNN-name/experiment/`

**Questions this raises**

<One line each. They go to QUESTIONS.md, not into this wheel.>

- <question>

**Changes to this post**

<One line per change that alters what a reader would do or believe: date,
what changed, new figure if a number moved. Typos and layout get no line.>

- YYYY-MM-DD: <what changed>

<!--
Checklist before publishing

Content
- [ ] title 65 characters or less, states the finding, no question mark
- [ ] summary one sentence, verb, full stop, 160 characters or less
- [ ] 4 numbers under the title, each with a denominator and a date, each repeated beside its evidence
- [ ] the answer appears before the method
- [ ] one example shown before any abstraction, before and after
- [ ] at least one chart, with its data table
- [ ] the same figure is used everywhere it appears, here and in other posts
- [ ] every limit sits next to the claim it limits
- [ ] systems and models are named, or the post says why not
- [ ] nothing is claimed about a fix without a measurement of the fix
- [ ] "What to do with this" has steps a reader can take, in order
- [ ] setup instructions live in the repo, the post links to them
- [ ] no FAQ
- [ ] every group, level, or term is shown to the reader before the post refers to it
- [ ] the answer starts with "Yes.", "No." or "Partly." on its own

Writing
- [ ] every rule in the 'Writing' section of CLAUDE.md, checked line by line, including the rejected words
-->
