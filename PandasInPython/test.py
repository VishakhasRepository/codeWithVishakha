class Employee:
    def __init__(self, salary):
        self.salary = salary
obj=Employee(50000)
obj.people=10
print((obj.__dict__))
print(obj.people+len(obj.__dict__))