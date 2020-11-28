# Set operations: unique()

x=np.array([2,3,3,8,9,16,9,21])
y=np.unique(x)
print(x)
print(y)

print("\n")
# Finding union: union1d()
x=np.array([1,2,3,4])
y=np.array([3,4,5,6])
print(x)
print(y)
print(np.union1d(x,y))

print("\n")
#Finding Intersection: intersection1d()
print(x)
print(y)
print(np.intersect1d(x,y))
print(np.intersect1d(x,y,assume_unique=True))

print("\n")
# Finding Difference: setdiff1d()
print(x)
print(y)
print(np.setdiff1d(x,y))
print(np.setdiff1d(x,y,assume_unique=True))

print("\n")
# Symmetric Difference: setxor1d()
print(x)
print(y)
print(np.setxor1d(x,y))
print(np.setxor1d(x,y,assume_unique=True))
