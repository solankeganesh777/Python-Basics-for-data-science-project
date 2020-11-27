# Numpy Random

# Random number generation

from numpy import random
x=random.randint(100)
print(x)
print(type(x))

# random float
x=random.rand()
print(x)
print(type(x))

print("\n")

#Generate random array
x=random.randint(100,size=(3,2))
print(x)
print(type(x))

print("\n")
x=random.rand(2,2)
print(x)
print(type(x))

print("\n")

#Generate random number from an array: choice()
x=random.choice([1,2,3,4,5,6],size=(3,3))
print(x)
