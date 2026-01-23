#  undestand all about numpy axis

import numpy as np

x= [[1,2,3],[4,5,6],[7,8,9]]
ar= np.array(x)
print(ar)

ar.sum(axis=0)   # column wise sum
print("column wise sum:", ar.sum(axis=0))
ar.sum(axis=1)   # row wise sum
print("row wise sum:", ar.sum(axis=1))
print(ar.T)


for i in ar.flat:
    print(i)
print (ar.nbytes)    

print(ar.reshape(1,9))

print(ar.ravel())


import numpy as np

ar = np.array([[1,1,1,1],[1,1,1,1]])
ar2 = np.array([[1,2,3,4],[5,6,7,8]])

print(ar2)
print(ar + ar2)
print(ar *ar2)

print(ar2 - ar)

print(np.where(ar2>5))
