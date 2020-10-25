#Array Slicing (Positive & Negative & Step)

import numpy as np

a=np.array([2,6,9,3,7,5])
print(a[1:3])
print(a[2:])
print(a[:4])
print(a[:])

print("\n \n")
a=np.array([2,6,9,3,7,5])
print(a[-3:-1:])
print(a[-4:])
print(a[:-4])
print(a[:])

print("\n")
a=np.array([[1,6,8,7],[3,6,5,7]])
print(a[0,1:4])

print("\n")
a=np.array([[1,6,8,7],[3,6,5,7]])
print(a[0:2,3])

print("\n")
a=np.array([[1,6,8,7],[3,6,5,7]])
print(a[0:2,0:3])

print("\n \n")
#Step
a=np.array([2,6,9,3,7,5])
print(a)
print(a[1:6:2])
print(a[::2])
