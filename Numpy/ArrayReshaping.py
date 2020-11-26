# Array Reshaping 

x=np.array([1,2,3,4,5,6,7,8,9])
y=x.reshape(3,3)
print(x)
print(x.shape)
print(y)
print(y.shape)

print("\n")
print(x.base)
print(y.base)

print("\n")

#Unknown dimension

x=np.array([1,2,3,4,5,6,7,8])
y=x.reshape(2,2,-1)
print(x)
print(x.shape)
print(y)
print(y.shape)
print("\n")

#Flatterning the array: Multidimension to 1-D

x=np.array([[1,2,3],[4,5,6]])
y=x.reshape(-1)
print(x)
print(x.shape)
print(y)
print(y.shape)
