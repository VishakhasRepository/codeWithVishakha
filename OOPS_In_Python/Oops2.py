class Employee:
    no_of_leaves = 8  #this is the property of the class stuent
    pass


harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.role = "Instructor"
harry.salary = 455
rohan.name = "Rohan"
rohan.role = "Student"
rohan.salary = 4554

print(rohan.no_of_leaves, harry.no_of_leaves, Employee.no_of_leaves)

# what if we want to change the no. of leaves then we need to change it via Employee class only
Employee.no_of_leaves = 33
rohan.no_of_leaves = 455  #this will not change employee no of leaes, this has created new instance for rohan
print(Employee.no_of_leaves)
print(rohan.no_of_leaves)
print(rohan.__dict__)  #this shows that which all classs varibles are made
