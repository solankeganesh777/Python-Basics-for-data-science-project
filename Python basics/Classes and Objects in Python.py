#Classes and Objects in Python

#Imported library to draw the ibjects
import matplotlib.pyplot as plt
%matplotlib inline  

#class
class Circle(object):
    #Constructor
    def __init__(self,radius=3,color='red'):
        self.radius=radius
        self.color=color
        
    #Method
    def add_radius(self,r):
        self.radius=self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 

#Create Object
RedCircle=Circle(4,'red')

# Find out the methods can be used on the object RedCircle
print(dir(RedCircle))

print('\n')

print(RedCircle.radius)
print(RedCircle.color)
RedCircle.drawCircle()
RedCircle.color='green'
RedCircle.add_radius(5)
RedCircle.drawCircle()

print('\n')

class Rectangle(object):
    def __init__(self,color,height,width):
        self.color=color
        self.height=height
        self.width=width
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
BlueRectangle=Rectangle('Blue',2,3)
BlueRectangle.drawRectangle()
RedRectangle=Rectangle('Red',1,1)
RedRectangle.drawRectangle()

print(RedRectangle.height)
print(RedRectangle.width)
print(RedRectangle.color)
