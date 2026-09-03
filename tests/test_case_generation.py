import json, subprocess, sys
from pathlib import Path
def test_case_thresholds():
    root=Path(__file__).resolve().parents[1]; subprocess.run([sys.executable,str(root/"scripts"/"create_demo_case.py")],check=True); initial=json.loads((root/"cases/geo_001/initial_result.json").read_text()); assert initial["agreement"]<.65
