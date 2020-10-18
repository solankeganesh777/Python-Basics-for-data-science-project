#Python Data Structure

#lists

l=['Ganesh', 28, 1992]
print(l)
print(type(l))

print('\n')

#Indexing
print(l[0])
print(l[-2])

print('\n')

#List Content: Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures.
tuple=('mangesh', 25)
l1=[l,tuple,'balasaheb', 48,'vaishali', 41]
print(l1)

print('\n')

#Slicing
print(l1[0:2])

print('\n')

#Extend operation
print(l1)
l1.extend(['mangesh', 22])
print(l1)

print('\n')

#Append operation
print(l1)
l1.append(['prathmesh',12])
print(l1)

print('\n')

#Lists are mutable:Elements in lists can be changed, unlike tuple
A=['gan',25,'man',22]
print(A)
A[0]='bal'
print(A)

print('\n')

#Delete element 
A=[4,5,8]
print(A)
del(A[1])
print(A)

print('\n')

#Split: Convert string to list
str="ganesh solanke"
print(str)
li=str.split()
print(li)

print('\n')

#We can use the split function to separate strings on a specific character. We pass the character we would like to split on into the argument, which in this case is a comma. The result is a list, and each element corresponds to a set of characters that have been separated by a comma
st='a,b,c,d'
print(st)
l=st.split(',')
print(l)

print('\n')

#Copy: After copying, both variable points to same list
A=['jalna', 21]
B=A
A[1]=22
print(A)
print(B)

print('\n')

#Clone list:To avoid pointing to same list by two variables after copying one variable to another
A=['jalna', 21]
B=A[:]
A[1]=22
print(A)
print(B)

print('\n')

#Concatenation
A=[1,'a']
B=[2,1,'d']
print(A+B)
