import numpy as np
from sklearn.model_selection import  KFold
data= np.array([.1,.2,.3,.4,.5,.6,.8,.12,.15,.14,.21,.25])
kfold = KFold(4)
for train, test in kfold.split(data):
    print(f'train : {data[train]} test : {data[test]}')