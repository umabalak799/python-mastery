class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def barks(self):
        print("Dog barks")
class Puppy(Dog):
    def runs(self):
        print("Puppy runs")
        
p = Puppy()
p.runs()
p.barks()
p.eat()

print(Puppy.mro())