class Employee:
    no_of_leaves = 8  # this is the property of the class student

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # self is that object jiski baat ki ja rahi hai, self wo instance hoga jispe yeh function lagaya ja raha hai
        print(f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}")


    @classmethod  #class methods can only access class variables,aisa method jo instance bhi access kar sake nad only class ko input le and args  and self ko na le then class method
    def change_no_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves  #can change the number of leaves of employee classs using cls variable



harry = Employee("Harry", "400", "Hero")  #these arguments are going to init method means in the constructors
rohan = Employee("Rohan", "3333","Zero")

rohan.printdetails()
harry.printdetails()

print(harry.name)
print(rohan.name)

#Employee ko arguments dene k tarike ko constructots kehte hai, uske liye init function banana padta hai


Employee.change_no_leaves(23)  #class can change its variables
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
harry.change_no_leaves(22)
print(harry.no_of_leaves)  #class instance variable can also access class variables
print(Employee.no_of_leaves)

