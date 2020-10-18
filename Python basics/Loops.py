#Loops

#Range object: Ordered list
print(range(3))

print('\n')

#For loop
year=['1992','1996','1967','1970']
n=len(year)

for i in range(n):
    print(year[i])

print('\n')
for j in range(8):
    print(j)

print('\n')
for i in range(1,4):
    print(i)
    
print('\n')
#Enumerate function
colours=['red','green','yellow']
print(list(enumerate(colours)))

for i, colours in enumerate(colours):
    print(i, colours)
    
print('\n')
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)
        
print('\n')
#While loop
year=[2001,2002,2003,2005]
i=0
date=0

while(date !=2003):
    date=year[i]
    i=i+1
    print(date)
    
