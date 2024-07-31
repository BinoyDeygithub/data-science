import numpy as np

# Step 1: Create a 4x4 matrix initialized with zeros
matrix = np.zeros((4, 4), dtype=int)

# Step 2: Add values 4, 5, 6 above the main diagonal
matrix[0, 1] = 4
matrix[1, 2] = 5
matrix[2, 3] = 6

# Print the resulting matrix
print(matrix)


arr=np.arange(11)
print(arr)
arr[(arr >=6) & (arr <=10)] *=-1 
print(arr)


#problem 3

import numpy as np

# Given matrix and array
mat = np.array([['abc', 'A'], ['def', 'B'], ['ghi', 'C'], ['jkl', 'D']])
arr = np.array(['abc', 'dfe', 'ghi', 'kjl'])

# Iterate through each row of the matrix
for i in range(mat.shape[0]):
    # Check if the element in Column 1 matches the corresponding element in the array
    if mat[i, 0] == arr[i]:
        # Print the corresponding value from Column 2
        print(mat[i, 1])


#problem 4

mat = np.array([[1, 21, 3],
                [5, 4, 2],
                [56, 12, 4]])

sorted_indices= np.argsort(mat[:,1])

print(sorted_indices)

sorted_mat=mat[sorted_indices]
print(sorted_mat)


#problem 5

arr = np.array([90, 14, 24, 13, 13, 590, 0, 45, 16, 50])
top_4=np.argpartition(arr,-4)[-4:]

top_4_value=arr[top_4]
t4sorted=np.sort(top_4_value)[::-1]

print(t4sorted)

#problem 6

arr = np.array([10, 55, 22, 3, 6, 44, 9, 54])

# Define the number to find the nearest to
nearest_to = 50

differences=np.abs(arr - nearest_to)
nearest_index=np.argmin(differences)
nearest_number=arr[nearest_index]
print(nearest_number)