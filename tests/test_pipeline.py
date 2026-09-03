import numpy as np
from remote.run_experiment import apply_pipeline
def test_rot180_pipeline():
    a=np.arange(9).reshape(3,3);b,v=apply_pipeline(a,[{'type':'transform','operation':'rot180'}]);assert np.array_equal(b,np.rot90(a,2));assert v.all()
def test_compound_order():
    a=np.arange(9).reshape(3,3);b,_=apply_pipeline(a,[{'type':'transform','operation':'rot180'},{'type':'shift','dr':1,'dc':0}]);assert b[1,0]==a[2,2]
