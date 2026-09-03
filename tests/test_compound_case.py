import numpy as np
from pathlib import Path
from remote.run_experiment import apply_pipeline,metrics
def test_b02_requires_compound_repair():
    d=Path(__file__).resolve().parents[1]/'cases/b02/public/data';ref=np.load(d/'reference.npy');target=np.load(d/'target_faulty.npy');valid=np.load(d/'target_valid.npy')
    partial,pv=apply_pipeline(target,[{'type':'transform','operation':'rot180'}],valid);repair,rv=apply_pipeline(target,[{'type':'transform','operation':'rot180'},{'type':'shift','dr':-5,'dc':5}],valid)
    assert metrics(ref,partial,pv)['agreement']<.85;assert metrics(ref,repair,rv)['agreement']>=.85
