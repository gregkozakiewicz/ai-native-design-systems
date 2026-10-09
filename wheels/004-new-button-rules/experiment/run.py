"""Run wheel 004's main run or its check run through the 10 models of wheel 002.

Usage:
    python3 run.py --model gpt-6-astra                      # main run: new rules, 31 scenarios
    python3 run.py --model claude-fable-5-1 --effort low
    python3 run.py --model gpt-6-astra --check              # check run: wheel 002's rules without examples, 29 scenarios
    python3 run.py --model gpt-6-astra --run2               # run 2: new rules with 2 fixes, 31 scenarios
    python3 run.py --model gpt-6-astra --run3               # run 3: run 2's rules with the reset changes, 32 scenarios

Everything comes from wheel 002's runner except the rules and, for the main
run, the scenarios. The main run reads levels/C-new-rules.md and this folder's
scenarios.md. The check run reads levels/C-no-examples.md and wheel 001's
scenarios.md, unchanged. Run 2 reads levels/C-new-rules-run2.md and this
folder's scenarios.md. Run 3 reads levels/C-new-rules-run3.md and
scenarios-run3.md. Only level C is run. Check runs, run 2 and run 3 go to
folders whose names end in -check, -run2 and -run3.
"""

import datetime
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# Both earlier runners are files called run.py, so they are loaded by path
# under distinct names. Wheel 002's runner does `import run as w1` and must
# get wheel 001's, so that one is registered as "run" first.
load("run", HERE.parents[1] / "001-button-variant" / "experiment" / "run.py")
sys.path.insert(0, str(HERE.parents[1] / "002-other-models" / "experiment"))
r2 = load("run_002", HERE.parents[1] / "002-other-models" / "experiment" / "run.py")

CHECK = "--check" in sys.argv
RUN2 = "--run2" in sys.argv
RUN3 = "--run3" in sys.argv
for flag in ("--check", "--run2", "--run3"):
    if flag in sys.argv:
        sys.argv.remove(flag)
if CHECK + RUN2 + RUN3 > 1:
    sys.exit("Use only one of --check, --run2 and --run3")

r2.w1.LEVELS_DIR = HERE / "levels"
r2.w1.LEVEL_FILES = {"C": "C-no-examples.md" if CHECK else "C-new-rules-run2.md" if RUN2 else "C-new-rules-run3.md" if RUN3 else "C-new-rules.md"}
if not CHECK:
    r2.w1.SCENARIOS_MD = HERE / ("scenarios-run3.md" if RUN3 else "scenarios.md")
r2.RUNS_DIR = HERE.parent / "runs"


def default_out():
    """Wheel 002's folder name, with -check added for the check run."""
    model = sys.argv[sys.argv.index("--model") + 1]
    effort = sys.argv[sys.argv.index("--effort") + 1] if "--effort" in sys.argv else None
    label = f"{model}-{effort}" if effort else model
    if CHECK:
        label += "-check"
    if RUN2:
        label += "-run2"
    if RUN3:
        label += "-run3"
    base = r2.RUNS_DIR / f"{datetime.date.today().isoformat()}-{label}"
    out, n = base, 2
    while out.exists():
        out = base.with_name(f"{base.name}-run{n}")
        n += 1
    return out


if __name__ == "__main__":
    if "--levels" not in sys.argv:
        sys.argv += ["--levels", "C"]
    if "--out" not in sys.argv and "--model" in sys.argv:
        sys.argv += ["--out", str(default_out())]
    r2.main()
