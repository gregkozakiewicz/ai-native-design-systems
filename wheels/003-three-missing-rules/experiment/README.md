# Experiment

## Setup

Wheel 002's runner and models, with one change: the rule file. `levels/C-machine-rules.md` is wheel 001's rule file plus the 3 sentences proposed in wheel 002's `implications.md`. Only level C runs. Each of the 10 models answers the 29 scenarios 3 times: 87 answers per model, 870 in all.

Before the run, the daily cap check from the wheel template: Gemini 3.1 Pro allows 250 requests a day on the account's tier and this run needs 87 per model, so no run is split.

## The 3 sentences

| Gap found in wheel 002 | Where it goes | Sentence added |
| --- | --- | --- |
| Where "optional" ends | precedence step 5 | a reversible action the user came to the view to do, or may reasonably do there (archive, export, log out), is secondary; ghost is only for actions most users never take on that view |
| Which rule wins inside a step | precedence step 3, with H8 moved into it from step 4 | if two fit, the more specific description of the button's role wins: an equal alternative to a recommended option (H8) beats a bypass (H12), and a bypass (H12) beats a plain dismiss (H5) |
| What "undone" means | rule H3 | an action is reversible only if the system can restore the previous state, and redoing the work by hand does not count |

The examples in the first sentence name the 3 scenarios that split. That is deliberate and is a limit: it tests whether the sentence moves the models, not whether it generalises. Wheel 002's reworded pairs still apply, so a model that matches the examples instead of reading the sentence shows up there.

## Inputs

- `levels/C-machine-rules.md`: the rule file under test
- `run.py`: wheel 002's runner, pointed at this folder's rules and this wheel's `runs/`
- scenarios and correct answers: wheel 001's, unchanged

## Scoring

Wheel 001's `score.py`, pointed at each model's run folder. The headline is misses with rules per model, against wheel 002's 32 in total, and which of wheel 002's 6 split scenarios still split.

## How to run

Keys for all four companies in the repo's `.env`.

1. Run `python3 run.py --model MODEL` from this folder, once per model; Fable takes `--effort low` to match wheel 002.
2. Run `python3 ../../001-button-variant/experiment/score.py ../runs/<folder>` for each.
