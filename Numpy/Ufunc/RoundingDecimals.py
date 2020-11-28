# Rounding decimals

# 1. Truncation: Trunc()/fix(), returns integer
x=np.array([-1.2558,2.9999,3.0002])
print(x)
print(np.trunc(x))

print(np.fix(x))

print("\n")
# 2. Rounding: around()
x=np.around(3.1666,2)
y=np.around(3.1666,1)
print(x)
print(y)
z=np.array([-1.2558,2.9999,3.0352])
print(z)
print(np.around(z,2))

print("\n")
# 3. Floor: floor(), returns float
x=np.array([-1.2558,2.9999,3.0352])
print(x)
print(np.floor(x))

print("\n")
# 4. Ceil: ceil()
x=np.array([-1.2558,2.9999,3.0352])
print(x)
print(np.ceil(x))
