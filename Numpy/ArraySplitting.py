# Array Splitting
x=np.array([1,2,3,4,5,6])
y=np.array_split(x,4)

print(y)
print(type(y))

print("\n")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
z=np.array_split(arr,4)
print(z)
print(type(z))

print("\n")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
z=np.array_split(arr,4,axis=1)
print(z)
print(type(z))

print("\n")

#Split along with rows
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
z=np.hsplit(arr,3)
print(z)

print("\n")

#Split along with columns
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
z=np.vsplit(arr,3)
print(z)

print("\n")

#Split along with height/depth
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],ndmin=3)
z=np.dsplit(arr,3)
print(z)
