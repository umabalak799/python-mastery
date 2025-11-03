class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name} ")

#this one below is inheritance class which is inherited from Employee class
class Programmer(Employee):
    def showLanguages(self):
        print("The default language is Python")
        
e = Programmer("Das", 405)
e.showDetails()
e.showLanguages()
        