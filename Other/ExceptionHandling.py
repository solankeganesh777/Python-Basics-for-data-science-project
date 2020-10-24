#Python Exception Handling: (Try-Except-Finally)

try:
    print(x)
except:
    print("X is not defined, so error occured and except block is executed")
    
print("\n")
#Multiple Exceptions
try:
    print(5/0)
except NameError:
    print("X not defined")
except:
    print("Something another error")

    
print("\n")
#Else in multiple exception:else keyword to define a block of code to be executed if no errors were raised
try:
    print(2)
except NameError:
    print("X is not defined")
else:
    print("Nothing went wrong")
    
print("\n")
#Finally: will be executed regardless if the try block raises an error or not
try:
    print(x)
except NameError:
    print("X is not defined")
finally:
    print("Good Bye, Try-Except is finished")
    
print("\n\n")
#Raise Exception: We can choose to throw an exception if a condition occurs

x=-1
if x<0:
    raise Exception("No numbers allowed less than 0")
