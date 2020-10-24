#Python Inheritance

#Parent class/Base class
class Cars:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def printCarDetails(self):
        print(self.brand)
        print(self.model)
        
        
car1=Cars('RR',"Discovery")
car1.printCarDetails()

#Child class/Derived class
class SUV(Cars):
    pass

car2=SUV('Jaguar','xj')
car2.printCarDetails()

print("\n")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Ganesh", "Solanke")
x.printname() 

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 


x = Student("Mangesh", "Solanke", 2019)
x.welcome()
x.printname()
