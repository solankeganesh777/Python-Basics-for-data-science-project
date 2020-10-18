#Python Data structures

#Sets
tastes={'spicy','sweet','bitter','sour','sour'}
print(tastes)

print('\n')

#Convert lists to sets
cars=['hyundai', 'honda', 'mg','bmw','bmw','honda' ]
print(cars)
print(type(cars))
cars_set=set(cars)
print(cars_set)
print(type(cars_set))

print('\n')

#Set operations
bike={'shine','yuga','unicorn','stunner'}
print(bike)

#Add element
bike.add('dawn')
print(bike)

#Remove element from set
bike.remove('yuga')
print(bike)

#Verify if element is in the set
print(('shine') in bike)

print('\n')

#Set logic operations
#check the difference between sets, as well as the symmetric difference, intersection, and union
bike1={'shine','yuga','unicorn','stunner'}
bike2={'shine','deluxe','ambition','yuga'}
print(bike1)
print(bike2)

print('\n')

#Intersection
print(bike1 & bike2)
print(bike1.intersection(bike2))

print('\n')

#Difference (Elements containes only in one set)
print(bike1.difference(bike2))
print(bike2.difference(bike1))

print('\n')

#Union: Elements in all sets
print(bike1.union(bike2))

print('\n')

#Check if set is superset or subset of another set
print(bike1.issuperset(bike2))
print(bike1.issubset(bike2))

print({'shine', 'yuga'}.issubset(bike1))
