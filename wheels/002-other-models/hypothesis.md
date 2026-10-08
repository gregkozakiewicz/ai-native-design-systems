# Hypothesis

Written on 7 October 2026, before any run.

## Expectation

The order holds on every model: rules above human documentation, human documentation above names only. The size of the gap changes. Smaller and cheaper models gain more from the rules, because they have less convention to fall back on. The rules score at least 80 of 87 on every model.

## Reasoning

The rules were written to remove judgement calls: a definition, a precedence order, and an explicit 'none'. That should help any model that can follow a list, which is all of them. Convention, which is what names-only relies on, varies more between models than instruction-following does, so level A should move the most between models.

## What would surprise us

- a model that scores lower with rules than with human written documentation
- a model that uses 'none' as an escape hatch, which no Opus run did in 765 answers
- the matched pairs breaking on another model: the original right, the reworded pair wrong
- a model that reads the precedence order differently and answers consistently but differently, showing a reading of the rules we did not see
