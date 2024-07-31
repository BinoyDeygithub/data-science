import numpy as np


# Task 1: Create a new NumPy array Narr with the shape equal to arr1 filled with random values

arr1 = np.array([25, 56, 12, 85, 34, 75])
arr2 = np.array([42, 3, 86, 32, 856, 46])

Narr=np.random.random(arr1.shape)

print(Narr)


# Task 2: Permanently change the dtype of arr1 to complex

# arr1=arr1.astype(complex)
# print(arr1)


# Tast 3

arr1_mat=arr1.reshape((2,3))
arr2_mat=arr2.reshape((2,3))

numerator=arr1_mat**2 - arr2_mat**2
denominator=arr1_mat- arr2_mat

result= numerator/denominator

print("arr1_mat:\n", arr1_mat)
print("arr2_mat:\n", arr2_mat)
print("Result:\n", result)


import numpy as np
arr = np.arange(9)
arr.reshape(3,3)
print(arr.shape)
 


arr1 = np.ones(10)
arr2 = np.arange(10, dtype = np.float64)
arr3 = arr1 + arr2
print(np.result_type(arr1))
print(np.result_type(arr3))


arr = np.arange(4).reshape(4,-1)
print(arr.shape)