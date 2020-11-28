# UFUNCS: uNIVERSAL FUNCTIONS

import numpy as np

# Array addition
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
print(np.add(x,y))

print("\n")
# Create your own ufuncs
def myadd(a,b):
    return a+b
myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2],[3,4]))
print(type(myadd))

print("\n")
# Check if function is ufunc
print(type(np.concatenate))
print(type(np.add))
print(type(myadd))
