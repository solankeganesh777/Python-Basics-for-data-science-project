# Numpy Logs

x=np.arange(1,10)
print(x)

print("\n")
#Log at base 2
print(np.log2(x))

print("\n")
#log at base 10
print(np.log10(x))

print("\n")
#Natural log or Log at base e
print(np.log(x))

print("\n")
#Log at any base: Not provided by numpy, created by user
from math import log
nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))
