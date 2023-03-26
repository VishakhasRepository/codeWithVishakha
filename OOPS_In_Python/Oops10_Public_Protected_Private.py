

class Employee:
    no_of_leaves = 8   #public variable
    _protecVar = 33    #this is protected variable starts with underscore, base class and derived class can use protected variable
    __privateVar = 77  #private variable starts from double underscore

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}")

    @classmethod
    def change_no_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_dash(cls, string):
        # list3 = string.split("-")
        # print(list3)
        # return cls(list3[0], list3[1], list3[2])
        return cls(*string.split("-"))  # using kwargs

    @staticmethod
    def print_something(Stringaa):
        print(f"Harry is good {Stringaa}")


emp = Employee("Karan", "222", "gunda")
print(emp._protecVar)
print(emp._Employee__privateVar)   #this is how a private variable is accessed using _Employee, this is namemangling



