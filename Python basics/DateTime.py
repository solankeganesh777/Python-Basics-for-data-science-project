#Python DateTime

import datetime
print(dir(datetime))

print(datetime.datetime.today())
print(datetime.datetime.now().year)
print(datetime.datetime.today().strftime("%Y")) 
print(datetime.datetime.today().strftime("%B")) 
print(datetime.datetime.today().strftime("%m")) 

print("\n")
#Creating Date objects
import datetime

x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(2020, 5, 17,12,58,59)

print(x) 
print(y)

print("\n")
#strftime method
print(datetime.datetime.today().strftime("%Y")) 
print(datetime.datetime.today().strftime("%B")) 
print(datetime.datetime.today().strftime("%m"))
print(datetime.datetime.today().strftime("%d")) 
print(datetime.datetime.today().strftime("%w")) 
print(datetime.datetime.today().strftime("%H"))
