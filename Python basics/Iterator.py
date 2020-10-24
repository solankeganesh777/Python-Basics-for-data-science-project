#Python Iterators

list=[1,2,3,4,5,6,7,8]
myit=iter(list)
print(next(myit))
print(next(myit))
print(type(myit))

print("\n")
name="Ganesh"
myit=iter(name)
print(next(myit))
print(next(myit))
print(type(next(myit)))
print(next(myit))
print(next(myit))
print(next(myit))


print("\n")
#Creation of iterator
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=3:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
    
Myclass=MyNumbers()
myiter=iter(Myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
