"""Recompute R01 evaluator-private validation from public arrays."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from benchmark.r01_validator import write_validation


parser = argparse.ArgumentParser()
parser.add_argument("--case-dir", type=Path, default=ROOT / "cases_real" / "r01")
args = parser.parse_args()
print(json.dumps(write_validation(args.case_dir.resolve()), indent=2))
