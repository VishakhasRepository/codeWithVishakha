

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def setPropName(self, name):
        return name

    def setPropSalary(self, salary):
        return salary

    def __str__(self):
        return 'Employee(name=' + str(self.name) + ' ,salary=' + self.salary + ')'

    def __repr__(self):
        return 'Employee(name=' + str(self.name) + ' ,salary=' + self.salary + ')'

obj1 = Employee("asddd", "34")
print(obj1.__str__())
print(obj1.__repr__())

