#Array Indexing (Positive & Negative Indexing)

import numpy as np

a=np.array([2,6,9,3,7,5])
print(a)
print("Dimesnions=", a.ndim)
print("Shape=", a.shape)
print(a[1])
print(a[2])

print("\n")
a=np.array([[1,6,8,7],[3,6,5,7]])
print(a)
print("Dimesnions=", a.ndim)
print("Shape=", a.shape)
print(a[0,1])
print(a[1,3])
print(a[0,2])

print("\n")
a=np.array([[[4,5,6],[8,3,9]],[[5,6,9],[7,5,8]]])
print(a)
print("Dimesnions=", a.ndim)
print("Shape=", a.shape)
print(a[0,1,2])

print("\n \n")
#Negative Indexing
a=np.array([2,6,9,3,7,5])
print(a)
print("Dimesnions=", a.ndim)
print("Shape=", a.shape)
print(a[-1])
print(a[-2])

print("\n")
a=np.array([[1,6,8,7],[3,6,5,7]])
print(a)
print("Dimesnions=", a.ndim)
print("Shape=", a.shape)
print(a[0,-1])
print(a[-1,-3])
print(a[0,-2])
