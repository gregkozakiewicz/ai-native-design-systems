# Experiment

## Setup

One model, Claude Opus 5.5, called through the Anthropic API at medium reasoning effort. Each scenario is sent 3 times at each of 3 information levels: 243 calls for the 27 scenarios in run 1, 261 for the 29 in later runs. The agent sees a short system prompt, the level's reference text, and one scenario. It must answer with exactly one of `primary`, `secondary`, `ghost`, `destructive` or `none`, plus one sentence naming the rule it applied.

The system prompt tells the agent to base its choice only on the reference. Without that, the names-only level would be answered from general knowledge and the comparison would blur.

## Inputs

- `scenarios.md`: the 29 scenarios with the designer's answers and a note of every change to them, grouped as easy, context, traps, conflicts, interaction and matched pairs; `run.py` reads the tables directly, so this file is the source of truth
- `levels/A-names-only.md`: the 4 variant names and 'none', nothing else
- `levels/B-human-docs.md`: documentation in the style of a typical design system site, with a description and examples per variant and 3 soft guidelines
- `levels/C-machine-rules.md`: what a variant means, 12 hard rules (11 in run 1), 5 never rules, a precedence order for conflicts, and a section on unknowns

Level B had one more line before the first full run: "Button variants are for standard click or tap actions." We removed it because real documentation rarely says this, and it gave away scenario 21. The dry run that used it is not kept.

## Scoring

Scoring is mechanical. `score.py` compares each answer with the designer's answer and reports:

- accuracy: answers matching the designer's answer, out of 3 per scenario per level
- consistency: scenarios where all 3 runs gave the same answer
- over-flagging: answers of 'none' where a variant was expected
- accuracy by category
- matched pairs: for the 4 pairs that test one rule with 2 wordings, whether each run got both, the original only, the pair only, or neither
- the scenarios most often wrong per level, with the wrong answers given

## How to run

You need Python 3 and an Anthropic API key with a few euros of credit. This is pay-as-you-go API credit, separate from a Claude subscription. One full run costs about €1.

1. Install the SDK with `pip3 install anthropic`.
2. Put that API key in the repo's `.env` file (copy `.env.example` if it is missing). Exporting `ANTHROPIC_API_KEY` in the shell also works.
3. Run `python3 run.py` from this folder. It prints the folder it writes to, `../runs/<date>-<model>-<effort>/`, and never reuses an existing one: a second run on the same day gets `-run2` added.
4. Run `python3 score.py ../runs/<that folder>` to write `summary.md` inside it.

To resume a run that stopped early, pass its folder with `--out`; answers already saved there are skipped. To try other settings, use `--model`, `--effort`, `--runs`, `--levels` and `--only`, or `--out` to name the run folder.
