#Conditions and Branching

#If 

age=15
if age>=25:
    print("Get married")
    
print("Go on")

print('\n')

#if-else
if age>=18:
    print("Adult")
else:
        print("Hello kid")
        
print("Go on")
    
print("\n")

#elif (i.e. else-if)
age=15
if age>18:
    print("Adult")
elif age==18:
    print("Wait a little bit")
else:
    print("Hang on kid")

    
print("\n")

#Logical operators: and, or, not
weight=130
if (weight<80) and (weight>60):
    print("Average")
elif weight>80:
    print("Overweight")
else:
    print("Underweight")

    
if (weight>120) or (weight<20):
    print("Health imbalanced")
    
print('\n')   
    
gender="female"
if not gender=='male':
    print("Female")
else:
    print("Male")
    
