# Numpy Filtering arrays

x=np.array([4,6,2])
y=[True,False,True]
z=x[y]
print(x)
print(y)
print(z)
print(type(z))

print("\n")

#creating a filter
x=np.array([2,9,55,4,35,55,28])
filter=[]

for i in x:
    if i%2==0:
        filter.append(True)
    else:
        filter.append(False)

y=x[filter]
print(x)
print(filter)
print(y)
 
print("\n")

# Create filter directly from arrays
x=np.array([55,6,8,2,55,3,2,44])
filter= x%2==0
y=x[filter]
print(x)
print(filter)
print(y)
