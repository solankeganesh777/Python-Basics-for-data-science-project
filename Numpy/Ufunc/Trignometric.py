# Numpy trignometric functions: sin(),cos(),tan()

import numpy as np
print(np.sin(np.pi/2))
print(np.cos(np.pi/2))
print(np.tan(np.pi/2))

x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
print(np.sin(x))
print(np.cos(x))
print(np.tan(x))

print("\n")
# Degree to radians & Radians to degress: deg2rad(),rad2deg

x=np.array([90,180,270,360])
y=np.deg2rad(x)
print(x)
print(y)
z=np.rad2deg(y)
print(z)

print("\n")
# Finding Angles: arcsin(),arccos(),arctan()
print(np.arcsin(1.0))
print(np.arccos(1.0))
print(np.arccos(1.0))

x=np.array([1,-1,0,0.1])
print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))

print("\n")
# Hypotenues: hypot()
base=3
perp=4
print(np.hypot(base,perp))
