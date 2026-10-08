"""Run wheel 001's scenarios through the 10 models of wheel 002, with this wheel's rule file.

Usage:
    python3 run.py --model gpt-6-astra
    python3 run.py --model claude-fable-5-1 --effort low

Everything comes from wheel 002's runner except the rules: level C is read
from this folder's levels/, which holds wheel 001's rule file plus the 3
sentences proposed by wheel 002. Only level C is run.
"""

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

r2.w1.LEVELS_DIR = HERE / "levels"
r2.w1.LEVEL_FILES = {"C": "C-machine-rules.md"}
r2.RUNS_DIR = HERE.parent / "runs"

if __name__ == "__main__":
    if "--levels" not in sys.argv:
        sys.argv += ["--levels", "C"]
    r2.main()
