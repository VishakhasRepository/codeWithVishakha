class Employee:
    no_of_leaves = 8  # this is the property of the class student

    def __init__(self, aname, asalary, arole):  #this is a kind of dunder method, starts with double underscore and ends with double underscore
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}")

    def __add__(self, other):    #this method is doing operator overloading, this mehtod is also a dunder method, predefined method in pyhthon
        return self.salary + other.salary

    def __truediv__(self, other):   #these are predefined methods in python
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', '{self.salary}', '{self.role}'s)"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}"

    #if str special method is not present then still it is called then repr is called inpalce of str



emp1 = Employee("Vishi", 234, "Python Developer")
emp2 = Employee("Vishi2", 456, "Java Developer No")

print(emp2+emp1)  #this prints 690
print(emp2/emp1)
print(str(emp2))
print(repr(emp2))
