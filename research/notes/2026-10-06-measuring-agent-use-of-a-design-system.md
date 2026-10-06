# Two posts on measuring and grounding how agents use a design system

**Read:** 6 October 2026

## What they are

The first post presents an open benchmark. A free static check reads a
component library's repo and scores how legible it is to a machine. A paid
run then gives real coding agents a user need, never a component name, and
grades what they build. The post reports a static check of 4 systems and
agent runs against one of them.

The second post presents a template that turns a design system into a
server an agent can ask questions mid-task, using MCP (Model Context
Protocol, a standard way for an agent to call tools). The server answers
"does this component exist", "what are its real props", "which token is this
colour" and "is this file valid". It also generates the agent instruction
files from the same data. It is a product page, not an experiment write-up.

## What is useful here

- the benchmark method is the closest published cousin to our wheels: one bounded question, a fixed task set, scoring written before the run, raw output kept
- task prompts never name the expected component, and a linter enforces that against the catalogue, which is the leak our own scenarios also need to guard against
- grade the worst dimension, not the average: 3 failure shapes (uses the system but gets the API wrong, avoids the system and passes every check, builds something ambitious that does not compile) give the same average score
- "ignored the design system" is tracked as its own number, because a model that never touches the system passes every API check
- report the gain from guidance as a difference between no guidance and guidance, not as a level, because a difference is harder to argue with
- the biggest step is from no instruction file to any instruction file; refining the file adds much less
- how much guidance helps varies several-fold between models, and the model that looks best with no help can respond least to help
- models arrive with a vocabulary of component and prop names from training, and a system whose names sit close to it gets compliance for free
- every system checked had components that were documented but not exported, and no documentation fixes that
- a design rule worth copying: when an agent asks for a name that does not exist, answer "not in this system" plus the nearest real names, never a plausible substitute
- a short alias file that maps the names people reach for to the names the system uses is claimed to prevent more wrong guesses than any other file
- one committed, hashed data layer feeds both the server and the generated instruction files, so the written guidance cannot drift from the shipped components

## Which wheel or question it touches

- wheel 001 on button variants: their guidance levels (none, instruction files, files plus skills plus catalogue) mirror our levels A, B and C
- candidate wheel on the smallest piece of information an agent needs: their finding that the first file matters most is a first data point
- candidate wheel on reuse or create: a resolve-the-name tool is one answer to "is there already a component for this"
- big question on what replaces component documentation: one post answers "exports, names, changelog and tokens as a machine-facing surface", the other answers "a server the agent can ask"
- 2 new questions parked in `QUESTIONS.md`: whether matching the names models expect beats writing guidance, and what still has to be said up front when the agent can ask

## What the posts do well

- the first screen carries the problem, the claim and a handful of numbers, so a reader who stops there still knows what was found
- one task, or one before and after, is shown in full before any abstraction is introduced
- every chart has a data table under it, and the chart is dated
- headings are findings, not topics
- the benchmark post separates what was read from the repo and what the agents did, and says plainly that the agent data covers one system
- it reports its own tool breaking on real code, which makes the other findings easier to trust
- the server post describes each tool as the question an agent asks mid-task, grouped by when the question arises
- both state the reasons behind a design or scoring choice, not only the result

## What the posts do badly

- the benchmark post is 2 documents in one: an argument and a user manual, and the manual half belongs in the repo
- 3 of the 4 systems checked are anonymised, so nothing can be verified or learnt from them
- hundreds of generations are reported as single figures to one decimal place, with no count per cell, no spread and no repeat runs
- the model count differs between a paragraph and the charts in the same post
- the text says one-shot and agentic runs are never ranked against each other, then puts both on the same chart
- the vocabulary list is mined from one company's systems, then used to score every other system, with no word on how far that generalises
- a score with a product name and 3 tiers is presented as measurement, while the post admits the tier thresholds are arbitrary
- the server post measures the problem but never the fix: no before and after with the server attached, and its strongest claims have no numbers
- the server post borrows figures from the benchmark post without a link or a method
- both use terms before explaining them, and the benchmark post hides caveats in an FAQ
- the server post leaves out its biggest limit: the benchmark found some models ignore the design system in over half of runs, and a server only helps an agent that asks

## What we take for our own posts

See `templates/post.md`. Lead with question, answer and dated numbers; show
one example in full; give every number a denominator; say what the data does
not show next to the claim, not in an FAQ; name what you measured or say why
you cannot; keep setup instructions in the repo; and never claim a fix
without a measurement of the fix.
