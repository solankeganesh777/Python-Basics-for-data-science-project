#NumPy in Python

#2D Numpy

import numpy as np
import matplotlib.pyplot as plt

a=[[1,5,7],[6,5,7],[9,8,3]]
print(a)
print(type(a))

A=np.array(a)
print(A)
print(type(A))
print(A.ndim)
print(A.shape)
print(A.size)

print("\n")
#Access elements of Numpy arrray
print(A[1,2])
print(A[1][1])

print("\n")
#Slicing
print(A[0][0:2])
print(A[0:2,2])

print("\n")
#Basic Operations
p=np.array([[1,2],[3,4]])
q=np.array([[3,2],[1,2]])
print(p)
print(q)
print(p+q)

print("\n")
#Multiplying numpy array by scalar
print(p)
print(p*3)


print("\n")
#Array Multiplication
print(p)
print(q)
print(p*q)

print("\n")
#Matrix Multiplication
x=np.array([[1,2,5],[5,3,2]])
y=np.array([[2,3],[3,1],[6,4]])
print(x)
print(y)
z=np.dot(x,y)
print(z)

print("\n")
#Mathematical functions

#Trignometric
print(np.sin(z))

print("\n")
#Transpose
j=np.array([[2,3,1],[4,5,8],[2,1,3]])
print(j)
print(j.T)
