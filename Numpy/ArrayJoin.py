# Numpy Array Join

import numpy as np
x=np.array([1,2,3])
y=np.array([5,6,7])

z=np.concatenate((x,y))
print(z)
print(z.shape)
print(z.ndim)
print(z.size)

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

ar=np.concatenate((arr1,arr2),axis=1)
print(ar)
print(ar.shape)
print(ar.ndim)
print(ar.size)

print("\n")

# Joining arrays using stack function
x=np.array([1,2,3])
y=np.array([5,6,7])

z=np.stack((x,y),axis=1)
print(z)
print(z.shape)
print(z.ndim)
print(z.size)

print("\n")

#Stacking along rows
x=np.array([1,2,3])
y=np.array([5,6,7])

z=np.hstack((x,y))
print(z)
print(z.shape)
print(z.ndim)
print(z.size)

print("\n")

#Stacking along columns
x=np.array([1,2,3])
y=np.array([5,6,7])

z=np.vstack((x,y))
print(z)
print(z.shape)
print(z.ndim)
print(z.size)

print("\n")

#Stacking along Height(Depth)
x=np.array([1,2,3])
y=np.array([5,6,7])

z=np.dstack((x,y))
print(z)
print(z.shape)
print(z.ndim)
print(z.size)

print("\n")
