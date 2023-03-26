class Employee:
    no_of_leaves = 8  # this is the property of the class student

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # self is that object jiski baat ki ja rahi hai, self wo instance hoga jispe yeh function lagaya ja raha hai
        print(f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}")


harry = Employee("Harryyyyyy", "400", "Hero")  #these arguments are going to init method means in the constructors
rohan = Employee("Rohannnn", "3333","Zero")

rohan.printdetails()
harry.printdetails()

print(harry.name)
print(rohan.name)

#Employee ko arguments dene k tarike ko constructots kehte hai, uske liye init function banana padta hai
