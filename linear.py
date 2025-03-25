import numpy as np
from numpy.ma.core import reshape

a=np.array([1,2,3,4,5,6,7,8,9,4,5,6])
reshaped= np.reshape(a,(3,4))
rows, cols = np.shape(reshaped)
print(reshaped)
print(reshaped[0])
print(reshaped[1])
print(reshaped[2])
print(reshaped[:,0])
print(reshaped[:,1])
print(reshaped[:,2])
