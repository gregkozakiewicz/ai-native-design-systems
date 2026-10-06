# Mila

Research towards an AI-native design system: what a design system has to
contain so that an AI agent reliably builds the right UI from it.

This repo is deliberately **not** a design system yet. It is a series of
small, bounded investigations. Each one answers a single question with a
test you can run, and the design system in `system/` grows only from what
those tests prove.

## How this repo works

The method is: one wheel at a time, not the whole factory.

| Folder | What goes there |
| --- | --- |
| `QUESTIONS.md` | The parking lot. Every idea, big or small, lands here first. Nothing in here is a commitment. |
| `wheels/` | One folder per bounded question. Each has a boundary, a test, raw runs, findings, and what it means for the system. |
| `research/` | Reading notes and reference material not tied to a single wheel (papers, other design systems, agent docs). |
| `examples/` | Reference inputs for tests: component docs, token files, real-world UI, good and bad cases. |
| `system/` | The design system itself. Every rule in here cites the wheel that proved it. |
| `tools/` | Shared scripts for running experiments and scoring results. |
| `templates/` | Skeletons: the folder a new wheel is copied from, and `post.md` for any write-up we publish. |

## Starting a new wheel

```bash
tools/new-wheel.sh "short name of the question"
```

That creates `wheels/NNN-short-name/` from the template, numbered after the
last one. Then fill in `README.md` first: the question, the boundary, and how
you will know it is answered. Do not start the experiment until those three
are written down.

## Rules of the road

- A wheel has to be answerable in days, not months. If it is not, split it.
- Every wheel writes down its success criteria before any agent is run.
- Raw agent output goes in `runs/`, untouched. Interpretation goes in `findings.md`.
- Nothing enters `system/` without a wheel behind it.
- The parking lot is allowed to be messy. The wheels are not.

## Current wheel

None yet. Candidates are in `QUESTIONS.md`.
