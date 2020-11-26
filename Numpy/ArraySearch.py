# Numpy Searching arrays

#Search indexes where value is 3
a=np.array([1,2,3,4,5,6,7,8,9,3,5,3])
print(a)
b=np.where(a==3)
print(b)

print("\n")
#Search indexes of even numbers
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
b=np.where(a%2==0)
print(b)

print("\n")

# Search Sorted: Performs a binary search in the array,
#and returns the index where the specified value would be inserted to maintain the search order
x=np.array([2,4,5,6,7,8,9,14])
y=np.searchsorted(x,6)
print(x)
print(y)

# We can give side='right' to return the right most index instead
x=np.array([2,4,5,6,7,8,9,14])
y=np.searchsorted(x,6,side='right')
print(x)
print(y)

print("\n")

# Search multiple values
x=np.array([2,4,5,6,7,8,9,14])
y=np.searchsorted(x,[2,4,8,14])
print(x)
print(y)
