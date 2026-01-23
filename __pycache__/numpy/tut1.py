import numpy as np


# myarr= np.array([1,2,3,4,5], np.int8)
# print(myarr)

# print(myarr.dtype)


#  5 general mechnism  for creating numpy array 
# Array creation : converting from other python structures
arr1= np.array((1,2,3,4,5))
print(arr1)
print(arr1.dtype)

listarray = np.array([[1,2,3],[5,6,7],[7,8,9]])
print(listarray)

print(listarray.shape)
print(listarray.ndim)
print(listarray.dtype)  

# Array creation intrinsic numpy array creation objects ( arange, ones , zeros, etc)

arr_zeros = np.zeros((3,4))
print(arr_zeros)

one_array = np.ones((2,3,4), dtype=np.int16)

print(one_array)

rng = np.arange(15)
print(rng)
lspace = np.linspace(1, 5, 12)
print(lspace)


emp= np.empty((2,3))
print(emp)

id_array = np.identity(4)
print(id_array)


arr= np.arange(99)
print(arr)

reshaped_arr = arr.reshape(3, 33)
print(reshaped_arr)


diag= np.diag([1,2,3,4,5])
print(diag)