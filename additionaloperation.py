import numpy as np
# x_cumsum= np.cumsum(S_X,axis=1)
# print(x_cumsum)

print(np.arange(0, 10, 5, dtype = np.int32))
print(np.linspace(0, 10, 5, dtype = np.float64))

print(np.linspace(0, 10, 5, dtype = np.int32))

print(np.arange(0, 10, 5, dtype = np.float64))

arr1 = np.arange(4)
arr2 = arr1 
arr2[0]+= 25
print(arr1[0])


import numpy as np

# Define the matrix
mat = np.array([[10, 5, 9],
                [2, 20, 6],
                [8, 3, 30]]).reshape(3, 3)
max_number=np.max(mat,axis=1)
N1,N2,N3=max_number

result_matrix=mat.copy()
print(result_matrix)

upper_half_indices=np.triu_indices(3,k=1)
result_matrix[upper_half_indices]+=N1

main_diagonal_indices=np.diag_indices(3)
result_matrix[main_diagonal_indices]+=N2

lower_half_indices=np.tril_indices(3,k=-1)
result_matrix[main_diagonal_indices]+=N3

print("Resultant matrix:\n",result_matrix)


import numpy as np

# Define the matrix
mat = np.array([[10, 5, 9],
                [2, 20, 6],
                [8, 3, 30]]).reshape(3, 3)

# Find the maximum numbers from each row
max_numbers = np.max(mat, axis=1)
N1, N2, N3 = max_numbers

# Copy the original matrix to avoid modifying it directly
result_matrix = mat.copy()

# Get the indices for the upper half (excluding the main diagonal)
upper_half_indices = np.triu_indices(3, k=1)
result_matrix[upper_half_indices] += N1

# Get the indices for the main diagonal
main_diagonal_indices = np.diag_indices(3)
result_matrix[main_diagonal_indices] += N2

# Get the indices for the lower half (excluding the main diagonal)
lower_half_indices = np.tril_indices(3, k=-1)
result_matrix[lower_half_indices] += N3

print("Resultant matrix:\n", result_matrix)


# quiz

import numpy as np

mat1 = np.matrix([[111, 1322],
                  [785, 554]])

print(mat1.sum(axis = 0).shape)
print(mat1.sum(axis = 1).shape)



arr = np.array([10,5,6,7]).reshape(2,-1)
print(arr.sum(axis = 0))
 

arr = np.arange(9, dtype = "float").reshape(3,3)
print(arr)
ind1 = np.array([[1,2],[0,1]])
ind2 = np.array([[0,2],[1,2]])
print(arr[ind1, ind2].sum())


import numpy as np

arr = np.array([10,22,32])
arrL = arr
arrC = arr.copy()
arrL[0] = 52
arrC[0] += 55
print(arr)