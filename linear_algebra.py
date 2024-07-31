import numpy as np
mat1 = np.arange(4).reshape(2,2)
mat2 = (np.arange(4)*2).reshape(2,2)
mat3 = (np.arange(4)*3).reshape(2,2)
''' Performing multiple dot product in one go '''
print(np.linalg.multi_dot( [mat1, mat2, mat3] ))
# [[ 36  66]
#  [132 234]] 
 



 
import numpy as np
a = np.array([[3, 1],[1, 2]])
b = np.array([9, 8])
''' Checking if system of equation has unique solution '''
print(np.linalg.det(a)) 
# 5.0
''' Since det = 5 which is non-zero. Hence, we have unique solutions
 Finding unique solution '''
print(np.linalg.solve(a, b))
# [ 2.  3.]
''' Calculating Inverse: Since, determinant is non-zero 
 hence, matrix is invertible '''
print(np.linalg.inv(a))
# [[ 0.4 -0.2]
#  [-0.2  0.6]]
''' Calculating Rank of the matrix '''
print(np.linalg.matrix_rank(a))
# 2 
 
import numpy as np

# Define the coefficients matrix A
A = np.array([
    [2, 3, 2],
    [1, 0, 3],
    [2, 2, 3]
])

# Define the constants vector b
b = np.array([1, 2, 3])

# Solve the system of equations
solution = np.linalg.solve(A, b)

# Print the solution
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")


import numpy as np

# Define the matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Perform matrix multiplication
C = np.dot(A, B)

# Alternatively, you can use the @ operator
# C = A @ B

# Print the result
print("Result of matrix multiplication:")
print(C)



import numpy as np

# Define the coefficient matrix A
A = np.array([
    [-4, 10],
    [2, -5]
])

# Calculate the determinant of A
det_A = np.linalg.det(A)

# Print the determinant
print(f"Determinant of the coefficient matrix: {det_A}")

# Check if the determinant is non-zero
if det_A != 0:
    print("The system has a unique solution.")
else:
    print("The system does not have a unique solution.")



print(np.arange(5, dtype = "float"))

print(np.arange(5))

print(np.floor(np.linspace(0,4,5)))
print(np.floor(np.linspace(0,5,5)))

import numpy as np
a = np.arange(9).reshape(3,-1)
b = np.ceil(np.linspace(7,15,9)).reshape(3,-1)
print(np.count_nonzero(np.greater_equal(a,b)))


mat = np.matrix([0,1,2,3]).reshape(2,-1)
print(np.linalg.det(mat))