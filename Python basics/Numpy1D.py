#Numpy in Python

#1D Numpy
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
%matplotlib inline

#Create a Numpy array
a=np.array([1,5,8,65,456,123,6,521])
print(a)
print(type(a))

b=np.array([2.5,22.5,33.8,12.75])
print(b)
# Check the type of the values stored in numpy array
print(a.dtype)
print(b.dtype)

print('\n')
#Mutable like list
print(a)
a[0]=12
print(a)

print('\n')
#Slicing
print(a[0:5])
print(a[2:4])

print('\n')
#assign new values to the corresponding indexes
print(a)
a[0:2]=100,200
print(a)

print('\n')
#Assign value with list
c=np.array([100,2,5,8,6])
print(c)
li=[2,3]
g=c[li]
print(g)
type(g)


print('\n')
#Number of elements in array
print(g)
print(g.size)
print(a)
print(a.size)

print('\n')
#number of array dimensions or the rank of the array
print(a)
print(a.ndim)

print('\n')
#tuple of integers indicating the size of the array in each dimension
print(a)
print(a.shape)

print('\n')
#Mean. Standard Deviation, max, min
h=np.array([5,3,2,2])
print(h)
print(h.mean())
print(h.std())
print(h.min())
print(h.max())

print('\n')
#Array operations

#Addition:Equivalent to vector addition
u=np.array([3,1])
v=np.array([2,2])
w=u+v
print(u)
print(v)
print(w)

print('\n')
#Array Multiplication:Equivalent to multiplicating vector by scalar
x=np.array([1,2])
y=2*x
print(x)
print(y)

print('\n')
#Product of arrays
u=np.array([3,1])
v=np.array([2,2])
w=u*v
print(u)
print(v)
print(w)

print('\n')
#Dot product: Same as matrix multiplication
u=np.array([3,1])
v=np.array([2,2])
w=np.dot(u,v)
print(u)
print(v)
print(w)

print('\n')
#Adding constant to numpy arrray
u=np.array([2,1,5,-1])
print(u)
print(u+1)

print('\n')
#Mathematical functions

#Access pi
print(np.pi)

#Create numpy array in radians
x=np.array([0,np.pi/2,np.pi])
print(x)

#Trignometric functions
print(x)
print(np.sin(x))
print(np.cos(x))

print('\n')
#linspace: Useful function for plotting mathematical functions is "linespace". 
#Linspace returns evenly spaced numbers over a specified interval

print(np.linspace(-2,2,5))
print(x)
y=np.sin(x)
plt.plot(x,y)
