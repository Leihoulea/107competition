import json,subprocess,sys
from pathlib import Path
def test_v2_cases_have_natural_difference():
    root=Path(__file__).resolve().parents[1];subprocess.run([sys.executable,str(root/'scripts/generate_blind_cases.py')],check=True)
    for name in ('b01','b02','b03'):
        initial=json.loads((root/'cases'/name/'initial_result.json').read_text());truth=json.loads((root/'cases'/name/'hidden/ground_truth.json').read_text());assert .85<truth['clean_baseline']['agreement']<1
        if name=='b03':assert initial['agreement']>=.85
        else:assert initial['agreement']<.65
