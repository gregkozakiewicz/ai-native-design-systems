# <Title: the finding or the question, 65 characters or less, sentence case>

<!--
How to use this template

Copy it for any write-up we publish or share during the research phase: a
wheel write-up, a reading note turned into a post, a progress report. Keep
the sections in this order. Delete a section only if it is truly empty, and
say so in one line instead ("No change to the system yet.").

Write to the rules in CLAUDE.md under "Writing": GOV.UK first, Google style
where GOV.UK is silent. The checklist at the bottom is the short version.

Text in angle brackets is a prompt to you. Replace it or delete it. Delete
every comment before publishing.
-->

<Summary: one sentence, 160 characters or less, with a verb, ending in a
full stop. It says what we found, not what the post is about.>

**Wheel:** `wheels/NNN-name/` · **Runs dated:** YYYY-MM-DD · **Status:** answered | partial | abandoned

| <Number> | <Number> | <Number> | <Number> |
| --- | --- | --- | --- |
| <what it counts, with the denominator> | <what it counts, with the denominator> | <what it counts, with the denominator> | <what it counts, with the denominator> |

<!--
The numbers strip is the whole post for a reader who stops here. Each cell is
a number plus what it is a number of: "41 of 69 runs", not "59%". Dated
numbers only. No number that does not appear again, with its evidence, below.
-->

## The question

<One sentence, copied from the wheel's README.md. If it needs two sentences,
it is two posts.>

**In scope:** <one line>
**Out of scope:** <one line>

## The answer

<Two or three sentences. Answer the question directly, including "no" or
"not yet". Then say in one sentence what the evidence does not cover. A
reader who stops here knows the result and its limit.>

## Why it matters

<Two or three sentences. What breaks today because this was unanswered, and
who feels it. No adjectives doing the work of evidence.>

## One example in full

<One scenario, prompt or task exactly as the agent saw it, then exactly what
the agent produced, then how it was scored. Show it before explaining the
method. If the example needs trimming to fit, link to the untrimmed run in
runs/ and say what was cut.>

```
<the prompt, verbatim>
```

```
<the output, verbatim>
```

<Score and reason, one or two sentences.>

## How we tested

<Enough for someone to re-run it. Prose for the shape, a table for the
facts.>

| Setting | Value |
| --- | --- |
| Models | <name and version, one row each if they differ> |
| Information levels | <what changed between runs, and nothing else> |
| Scenarios | <count, and where they live> |
| Repeats | <runs per scenario per level> |
| Scoring | <who or what scores, against what, written before the runs> |
| Dates | <first and last run> |
| Cost | <money and time, roughly> |

<One sentence on what was fixed before the runs started and what was
changed after. If a scoring rule changed mid-way, say so here and in the
findings.>

## What we found

<!--
One sub-heading per finding. The heading is the finding as a statement
("Guidance moved one model by 24 points and another by 6"), never a topic
("Results") and never a question. Order by importance, not by the order you
discovered them.

Under each heading: the claim in one or two sentences, then the table that
supports it, then one or two sentences on what the table does not show.
Every table has a denominator column or a caption that gives it. Every chart
has a table beside it. Point at specific files in runs/.
-->

### <Finding 1 as a statement>

<Claim.>

| <Level or model> | <Measure, n of N> | <Measure, n of N> |
| --- | --- | --- |
| | | |

<What this does not show. Which runs: `runs/YYYY-MM-DD-...`.>

### <Finding 2 as a statement>

<Same shape.>

### <Failure modes we saw>

<One line each: what went wrong, how often, where to look. Include the
failures of our own setup, not only the agent's.>

## What this does not show

<The honest list, beside the claims rather than at the bottom of an FAQ.
Sample size, single system, single model, levels that bundle two changes,
scoring that depends on a model, anything anonymised and why. One sentence
each.>

- <limit>
- <limit>

## What changes in the system

<Only rules proposed in the wheel's implications.md may appear here, each
with the run that justifies it. If nothing changes yet, say "Nothing yet" and
why.>

- <rule in one sentence>: justified by `runs/...`

## Questions this raises

<New questions go to QUESTIONS.md, not into this wheel. List them here with
one line each so the reader can see where the thinking is going.>

- <question>

## Reproduce it

<Where the wheel lives, where the raw runs live, and the one command or the
steps that run it. Setup detail stays in the repo, not in the post.>

- wheel: `wheels/NNN-name/`
- raw output: `wheels/NNN-name/runs/`
- scoring: `wheels/NNN-name/experiment/`

## Changes to this post

<One line per change that alters what a reader would do or believe. Date,
what changed, and the new figure if a number moved. Typos and layout do not
get a line.>

- YYYY-MM-DD: <what changed>

<!--
Checklist before publishing

Content
- [ ] title 65 characters or less, states the finding, no question mark
- [ ] summary 160 characters or less, one sentence, verb, full stop
- [ ] the answer appears before the method
- [ ] one example shown in full before any abstraction
- [ ] every number has a denominator and a date, and appears twice: in the strip and beside its evidence
- [ ] the same figure is used everywhere it appears, here and in other posts
- [ ] every limit sits next to the claim it limits
- [ ] systems and models are named, or the post says why not
- [ ] nothing is claimed about a fix without a measurement of the fix
- [ ] setup instructions live in the repo, the post links to them
- [ ] no FAQ

Writing
- [ ] sentences under 25 words, paragraphs under 5 sentences
- [ ] active voice, "you" and "we", present tense
- [ ] every specialist term explained on first use, every abbreviation expanded on first use
- [ ] headings are statements in sentence case, never questions, no links in them
- [ ] bullets have a lead-in line, start lower case, one sentence each, no full stops
- [ ] no italics, no bold for emphasis, bold only for interface elements
- [ ] code, filenames and commands in code font
- [ ] link text says where it goes, no "click here", no bare URLs in prose
- [ ] none of the words on the GOV.UK avoid list, no "simply", "easy", "just", "please note"
- [ ] no em-dashes, no exclamation marks, no metaphors
-->
