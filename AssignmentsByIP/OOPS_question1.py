# Q1. Write a Python program to demonstrate multiple inheritance.
# 1. Employee class has 3 data members EmployeeID, Gender (String), Salary and
# PerformanceRating(Out of 5) of type int. It has a get() function to get these details from
# the user.
# 2. JoiningDetail class has a data member DateOfJoining of type Date and a function
# getDoJ to get the Date of joining of employees.
# 3. Information Class uses the marks from Employee class and the DateOfJoining date
# from the JoiningDetail class to calculate the top 3 Employees based on their Ratings
# and then Display, using readData, all the details on these employees in Ascending
# order of their Date Of Joining.


import datetime


class Employee:

    def __init__(self, employeeID: str, gender: str, salary: str, per_rating: int):
        self.employeeID = employeeID
        self.gender = gender
        self.salary = salary
        self.per_rating = per_rating

    def get_employeeId(self):
        return self.employeeID

    def get_gender(self):
        return self.gender

    def get_salary(self):
        return self.salary

    def get_per_rating(self):
        if self.per_rating <= 5:
            return self.per_rating


class JoiningDetail():
    def __init__(self, dateOfJoining):
        self.dateOfJoining = dateOfJoining

    def get_date_of_joining(self):
        return self.dateOfJoining


class Information(Employee, JoiningDetail):

    def __init__(self, employeeID: str, gender: str, salary: str, per_rating: int, dateOfJoining):
        Employee.__init__(self, employeeID, gender, salary, per_rating)
        JoiningDetail.__init__(self, dateOfJoining)

    def dispalyData(self):
        print(self.dateOfJoining)
        print(self.per_rating)


objects_list = [('1', 'm', '10', 5, datetime.date(2000, 10, 30)),
             ('2', 'f', '5', 2, datetime.date(2001, 10, 12)),
             ('3', 'm', '100', 10, datetime.date(1998, 10, 1)),
             ('4', 'm', '100', 4, datetime.date(1991, 10, 1)),
             ('5', 'f', '100', 3, datetime.date(1996, 10, 1))]

information1 = Information('1', 'm', '10', 5, datetime.date(2000, 10, 30))
information2 = Information('2', 'f', '5', 2, datetime.date(2001, 10, 12))
information3 = Information('3', 'm', '100', 10, datetime.date(1998, 10, 1))
information4 = Information('4', 'm', '100', 4, datetime.date(1991, 10, 1))
information1.dispalyData()
information2.dispalyData()
information3.dispalyData()
information4.dispalyData()





