# Experiment

## Setup

Wheel 001's test, run unchanged on other models. The scenarios, the 3 information levels, the system prompt, the answer format and the scoring are wheel 001's files, read from `../../001-button-variant/experiment/`. Nothing is copied, so the two wheels cannot drift apart.

Each model runs every scenario 3 times at each of the 3 levels: 261 calls per model. Each model runs at its default reasoning setting; wheel 001 ran Opus 5.5 at medium, which is its default.

Models, one per company at the tier closest to Opus 5.5, plus smaller or older ones where the company offers them:

| Model | Company | API |
| --- | --- | --- |
| `gpt-5.6-sol` | OpenAI | Responses API with a strict JSON schema |
| `gemini-3.1-pro-preview` | Google | generateContent with a response schema |
| `gemini-3.8-flash` | Google | same; the newest stable Flash model, added when the preview hit its daily cap (Gemini 2.5 Pro is not available to new accounts) |
| `grok-4.7` | xAI | chat completions with a strict JSON schema; the current flagship |
| `grok-4.3` | xAI | same; an older model, for a within-company comparison |
| `claude-sonnet-5-5` | Anthropic | wheel 001's code, same as Opus |
| `claude-haiku-4-5` | Anthropic | wheel 001's code, same as Opus |

The model names were taken from each API's own model list on 7 October 2026.

Google caps `gemini-3.1-pro-preview` at 250 requests a day on the account's tier, so that run stopped at 247 of 261 on 7 October and the last 14 answers, all at level C, were filled the next morning with the same command. The runner now stops cleanly at a daily cap and prints the resume command.

## Inputs

- `run.py`: picks the API from the model name and sends wheel 001's prompt and schema to it; everything else is imported from wheel 001
- `../../001-button-variant/experiment/scenarios.md`, `levels/`: unchanged

Each API is given the same two things: the system text (wheel 001's instruction plus the level's reference) and the user text (the scenario and the button label). Each is asked for the same 2 fields: a variant from the list of 5 and a one-line reason. The only differences are the API's own names for those parts.

## Scoring

Wheel 001's `score.py`, pointed at each model's run folder. Same 3 measures, same matched pairs.

## How to run

Keys for all four companies go in the repo's `.env` file (see `.env.example`).

1. Run `python3 run.py --model MODEL` from this folder, once per model. Output goes to `../runs/<date>-<model>/`.
2. Run `python3 ../../001-button-variant/experiment/score.py ../runs/<that folder>` for each.

To check a model works before spending on it: `python3 run.py --model MODEL --only 6 21 --runs 1`.
