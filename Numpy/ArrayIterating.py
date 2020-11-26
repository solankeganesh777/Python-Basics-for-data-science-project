# Numpy Array Iterating

x=np.array([[1,2,3],[4,5,6]])

for i in x:
    print(i) 

print("\n")
for j in x:
    for k in j:
        print(k)
print("\n")

# Array iterating using nditer()
x=np.array([[1,2,3],[4,5,6]])

for i in np.nditer(x):
    print(i)
print("\n")

# Array ierating with different data types
x=np.array([1,2,3,4,5,6])
print(x.dtype)
for i in np.nditer(x,flags=['buffered'],op_dtypes="S"):
    print(i)
    print(i.dtype)
print("\n")

# Iterating with different step size
x=np.array([[1,2,3,4],[5,6,7,8]])

for i in np.nditer(x[:,::2]):
    print(i)
print("\n")

# Enumerated iteration using ndenumerate
x=np.array([[1,2,3,4],[5,6,7,8]])

for idx, i in np.ndenumerate(x):
    print(idx,i)

    
