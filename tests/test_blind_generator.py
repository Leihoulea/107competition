import json
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]


def generate(destination: Path):
    subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_blind_cases.py"), "--count", "8", "--seed", "20260904", "--output-root", str(destination)], check=True, capture_output=True, text=True)


def test_count_seed_and_hidden_recipe_metadata_are_reproducible():
    with TemporaryDirectory(dir=ROOT) as first, TemporaryDirectory(dir=ROOT) as second:
        one, two = Path(first), Path(second); generate(one); generate(two)
        cases = sorted(one.glob("case_*"))
        assert len(cases) == 8
        for case in cases:
            name = case.name
            left = json.loads((case / "hidden" / "ground_truth.json").read_text())
            right = json.loads((two / name / "hidden" / "ground_truth.json").read_text())
            assert left == right and left["generator_seed"] >= 20260904
            assert {"fault", "fault_family", "injected_recipe", "repair_recipe", "clean_baseline", "generator_seed"} <= left.keys()
