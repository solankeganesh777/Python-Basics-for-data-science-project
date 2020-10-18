#Python Data Structure

# Dictionaries
dict={'key1':10,'Key2':15,(0,1):6}
print(dict)

print('\n')

#Keys can only be strings, numbers, or tuples and values can be any data type
print(dict['key1'])
print(dict[(0,1)])

print('\n')

#retrieve the keys of the dictionary
print(dict.keys())

#retrieve the values of the dictionary
print(dict.values())

print('\n')

#Add an entry
dict['key3']=51
print(dict)

print('\n')

#Delete an entry
del(dict['key1'])
print(dict)

print('\n')

#Verify if element(key) is in the dictionary
print('Key2' in dict)
print(dict)
