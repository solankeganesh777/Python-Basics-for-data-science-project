import numpy as np

#Creating arrays

a=np.array([[1,2,3],[5,8,2],[6,9,2]])
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.dtype)
print(a.shape)
print(np.__version__)
print(type(a))

print("\n")
#0-dimensional array
a=np.array(5)
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("\n")
#1-dimesnional array
a=np.array([5,6,9,24,8])
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("\n")
#2-dimesnional array
a=np.array([[5,6,9,24],[2,8,9,5]])
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("\n")
#3-dimesnional array
a=np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("\n")
#Higher dimensional array
#Create an array with 5 dimensions, using the ndmin argument
a=np.array([1,2,3,4],ndmin=5)
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)
