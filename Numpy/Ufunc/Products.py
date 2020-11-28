# Numpy products

x = np.array([1, 2, 3])
print(np.prod(x))

y = np.array([4, 5, 6])
print(np.prod([x,y]))

print("\n")
# Product over an axis
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.prod([x,y],axis=1))

print("\n")
# Cummulative product
x = np.array([1, 2, 3])
print(np.cumprod(x))
