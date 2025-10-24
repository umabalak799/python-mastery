#how to create class

class Details:
    Name = "Tom"
    Age = 26

    def info(self):
        print(f"{self.Name} is {self.Age} years old")

#how to create Objects:

obj1 = Details()
print(obj1.Name)   #access data (attributes)
print(obj1.Age)

#calling the method of the class using that object.
obj1.info()

#constructor:
class Details:
    def __init__(self, n, o):     # __init__ is a constructor, self refers to the current object that is created, n and 0 is the values of the objects 
        self.name = n             #self.name and self.occ stores the values inside the object
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Details("Tom", "Developer")   #this is object 
a.info()
