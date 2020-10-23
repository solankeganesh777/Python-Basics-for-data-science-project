# Check the Python Version

"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
"""

import sys
print(sys.version)


#Type check
print(type(32))
print(type((2.3)
print(type("welcome"))

#Integer
n=2
print(n)
type(n)

#Float
b=2.1
print(b)
type(b)

#String
strr=type(n)
type(strr)

#Converting from one object type to a different object type
int(1.1)
int('1')
float('1.2')
str(1)
str(1.2)

#Boolean
type(True)
type(False)
bool(0)
float(True)

#Complex
x=1j
print(x)
print(type(x))
           
#Sequence: Range
x=range(6)
print(x)  
print(type(x) 
 
#Set:FrozenSet
y=frozenset({'apple','mango','melon'})
print(y)      
print(type(y))      
      
#Binary:bytes 
x=b"hello"
print(x)
print(type(x))
      
#Binary:bytearray
x=bytearray(5) 
print(x)
print(x)
      
#Binary:Memoryview
x=memoryview(bytes(5))
print(x)
print(type(x)      
