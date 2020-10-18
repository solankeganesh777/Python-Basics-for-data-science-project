name="ganesh solanke"
print(name)

#Length of the string
len(name)
len('ganesh solanke')

#Indexing of string

#Positive indexing
name[0]
name[4]

#Negative indexing
name[-1]
name[-3]

#Slicing
name[0:4]
name[3:7]

#Stride
print(name[::2])
print(name[0:5:2])

#Concatenation
name+' Is the best'
#Replicate values of strings
name*2

#Escape sequences

# \n for New line
print(name + '\n is the best' )

# \t for Tab 
print(name + '\t is the best')

# r for raw string i.e. print backslash
print(name + r'\ is the data science lover')

#String operations/Methods

#upper
print(name.upper())

print('\n')

#replace
print(name)
print(name.replace('ganesh', 'mangesh'))
print(name.replace('solanke', 'kharabe'))

print('\n')

#find
print(name)
print(name.find('solanke'))

print('\n')

#length
print(len(name))

