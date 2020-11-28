# Numpy Summations

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.sum([x,y]))

print("\n")
# Summation over an axis
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.sum([x,y],axis=1))

print("\n")
# Cummulative sum
x = np.array([1, 2, 3])
print(np.cumsum(x))
