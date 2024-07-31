
import sys,numpy as np

lst=[5,9,87]
print(sys.getsizeof(lst))

arr=np.array(lst)
print(type(arr[0]),type(arr[2]))
print(arr.nbytes)
print(np.result_type(arr))


arr=np.array([2,4,5,6],dtype= bool)
print(type(arr))

print(np.result_type(arr))


print(np.arange(1,20,1.5, dtype=np.float64))

print(np.linspace(1,180,6,dtype=np.float64))

print(np.array([5,7,8,4,3,9,76,889,55]).reshape(3,3))
# print(np.array([5,7,8,4,3,9,76,889,55]).real(8,3))

print(np.matrix([[6,8],[9,5]]))


print(np.eye(5))

print(np.eye(5,2))

print(np.zeros((4,9)))