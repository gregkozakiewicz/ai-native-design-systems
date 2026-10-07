# Experiment

## Setup

Which agent(s), which model(s), what inputs, how many runs.

Before the first run, check the daily request cap of every model on the
account's tier and size the run to the lowest one. On 7 October 2026 a
Gemini preview model allowed 250 requests a day, so 3 levels by 3 repeats
means 27 scenarios or fewer (243 calls). If a run must exceed a cap, split
it across days by design and say so here.

## Inputs

List the files in this folder and in `examples/` that the agent is given.

## Scoring

How a run is judged correct or incorrect. Be mechanical where possible.

## How to run

Commands, in order. Output goes to `../runs/YYYY-MM-DD-<label>/`.
