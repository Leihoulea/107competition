import numpy as np
from remote.run_experiment import shift_without_wrap
def test_shift_does_not_wrap():
    a=np.array([[1,2,3]]);b,v=shift_without_wrap(a,0,1);assert b.tolist()==[[0,1,2]];assert v.tolist()==[[False,True,True]]
