#Functions

def add(a):
    """
    This code performs addition
    """
    b=a+1
    print(a,'After incrementing', b)
    return(b)

print(add(2))


print('\n')
#Obtain help about functioin
help(add)


def mul(a,b):
    print("multiplication is", a*b)
mul(2,3)
mul(2,'ganesh')

print('\n')

#If-else statements and loops in functions
def health(weight):
    if weight>100:
        return("Overweight, Unhealthy")
    elif weight<30:
        return("Underweight, Unhealthy")
    else:
        return("Good health")

print(health(120))

def PrintTable(n):
    for i in range(1,11):
        print(i*n)
PrintTable(2)

print('\n')
#Custom function with default argument values
def goodRating(rating=4):
    if rating<5:
        print("Rating is low", rating)
    else:
        print("Rating is quite good", rating)

print(goodRating())
print(goodRating(10))

print('\n')

#Global variables
# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)
