class Employee:
    def __init__(self, name):
        self.name = name
    def showDetails(self):
        print(f"The name of the employee is {self.name}")
emp1 = Employee("Kailash")
emp1.showDetails()