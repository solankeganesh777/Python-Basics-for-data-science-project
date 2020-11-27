# Numpy random data distribution

import numpy as np

# Random Distribution
x=random.choice([2,4,6,8],p=[0.1,0.3,0.6,0.0],size=(5,2))
print(x)

print("\n")

#Random permutation: shuffle() and permutation()
x=np.array([1,2,3,4,5,6,7,8,9])
print(x)
random.shuffle(x)
print(x)

print("\n")
p=np.array([9,5,1,3,5,7])
print(p)
q=random.permutation(p)
print(q)
