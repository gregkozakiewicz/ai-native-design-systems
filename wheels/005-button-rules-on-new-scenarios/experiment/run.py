"""Run wheel 005 through the 10 models of wheel 004, with Claude Haiku 5.5 for Haiku 4.5.

Usage:
    python3 run.py --model gpt-6-astra                      # main run: 24 new scenarios
    python3 run.py --model claude-fable-5-1 --effort low
    python3 run.py --model claude-haiku-5-5 --baseline      # Haiku 5.5 on wheel 004's 32 scenarios
    python3 run.py --model claude-haiku-5-5 --only 1 --runs 1   # dry run

Everything comes from wheel 002's runner except the rules and the scenarios.
The rules are levels/C-system-rules.md, a copy of wheel 004's run 3 file,
whose sections 1 to 5 are system/button-variant.md. The main run reads
scenarios-run.md, generated from scenarios.md. The baseline reads wheel 004's
scenarios-run3.md. Only level C is run. Baseline folders end in -baseline.
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

BASELINE = "--baseline" in sys.argv
if BASELINE:
    sys.argv.remove("--baseline")

r2.w1.LEVELS_DIR = HERE / "levels"
r2.w1.LEVEL_FILES = {"C": "C-system-rules.md"}
r2.w1.SCENARIOS_MD = (HERE.parents[1] / "004-new-button-rules" / "experiment" / "scenarios-run3.md") if BASELINE else (HERE / "scenarios-run.md")
r2.RUNS_DIR = HERE.parent / "runs"


def default_out():
    """Wheel 002's folder name, with -baseline added for the baseline."""
    model = sys.argv[sys.argv.index("--model") + 1]
    effort = sys.argv[sys.argv.index("--effort") + 1] if "--effort" in sys.argv else None
    label = f"{model}-{effort}" if effort else model
    if BASELINE:
        label += "-baseline"
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
