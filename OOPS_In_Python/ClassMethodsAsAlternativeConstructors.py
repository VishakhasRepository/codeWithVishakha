class Employee:
    no_of_leaves = 8  # this is the property of the class student

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
        #list3 = string.split("-")
        #print(list3)
        #return cls(list3[0], list3[1], list3[2])
        return cls(*string.split("-"))  #using kwargs


harry = Employee("Harryyyyyy", "400", "Hero")
rohan = Employee("Rohannnn", "3333", "Zero")
karan = Employee.from_dash("Karan-222-gunda")  #this is alternative tpe of constructor of one parameter
print(karan.name)
print(karan.no_of_leaves)
