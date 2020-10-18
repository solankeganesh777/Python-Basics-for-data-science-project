#Python Data Structure

#Tuple
tuple1=('ganesh', 28, 57.5)
print(tuple1)

print(tuple1[1])
type(tuple1)

print('\n')

print(type(tuple1[2]))

print('\n')

#Indexing
print(tuple1[0])
print(tuple1[-1])

#Concatenation
tuple2=tuple1 + ("mangesh", 25, 60.2)
print(tuple2)

print('\n')

#Slicing
print(tuple2[0:4])

print('\n')

#length
print(len(tuple1))
print(len(tuple2))

print('\n')

#Sorting
tuple3=('ganesh', 'mangesh', 'balasaheb', 'vaishali')
tuple4=(20,10,19,18,2)
print(sorted(tuple3))
print(sorted(tuple4))

print('\n')

#Nested tuple 
Nestedtuple5=('balasaheb', tuple1, tuple3, ('vaishali', 45, 55.3))
print(Nestedtuple5)
print(Nestedtuple5[0])
print(Nestedtuple5[1])
print(Nestedtuple5[3])

print(Nestedtuple5[1][0])
print(Nestedtuple5[2][3])

#Access strings in nested tuple
print((Nestedtuple5[3][0][0:3]).upper())

#Find index 
Nestedtuple5.index("balasaheb")

