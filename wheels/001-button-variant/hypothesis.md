# Hypothesis

This file was written on 7 October 2026, after the first run. The wheel started before the repo adopted its method. The expectations below are the ones we discussed before running, recorded from the conversation, not invented after seeing the results.

## Expectation

Machine-readable rules score highest, human documentation second, and names only lowest. The gap between human documentation and rules is the useful finding. The easy scenarios score the same at every level.

## Reasoning

Prose documentation describes variants but rarely says which rule wins when two apply. Rules with a precedence order remove that guesswork. With names only, the agent falls back on convention, which is right for common cases and wrong for the rest.

## What would surprise us

- rules doing no better than prose, which would mean the model's own convention is already as good as a written system
- the agent getting a scenario right but its reworded pair wrong, which would mean it matched words in the rules rather than applying them
- the agent using 'none' as an escape hatch when unsure
