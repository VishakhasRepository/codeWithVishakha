import datetime

class Employee:

    def __init__(self, EmployeeID=None, Gender=None, Salary=None, PerformanceRating=None):
        self.EmployeeID = EmployeeID
        self.Gender = Gender
        self.Salary = Salary
        self.PerformanceRating = PerformanceRating

    def get(self):
        self.EmployeeID = input("Enter the EmployeeID: ")
        self.Gender = input("Enter the Gender: ")
        self.Salary = input("Enter the Salary: ")
        self.PerformanceRating = int(input("Enter the performance rating (0 to 5): "))
        assert 0 <= self.PerformanceRating <= 5  #this throws assertion error if performance rating is more than 5


class JoiningDetail:

    def __init__(self, doj=None):
        self.DateOfJoining = doj

    def getDOJ(self):
        self.DateOfJoining = input("Enter the date of joining in DD/MM/YY format: ")


class Information(Employee, JoiningDetail):
    instances = []

    def __init__(self, *args):
        Employee.__init__(self, *args)
        JoiningDetail.__init__(self)
        self.__class__.instances.append(self)

    @classmethod
    def readData(cls):
        length = min(len(cls.instances), 3)
        top3 = sorted(cls.instances, key=lambda x: x.PerformanceRating, reverse=True)[:length]
        print("|--Top 3 Employees--|")
        for Employee in sorted(top3, key=lambda x: x.DateOfJoining):
            print("\nEmployeeID: ", Employee.EmployeeID)
            print("Gender: ", Employee.Gender)
            print("Salary: ", Employee.Salary)
            print("PerformanceRating: ", Employee.PerformanceRating)
            print("Date joined: ", Employee.DateOfJoining)


#Employees = {}

#information1 = Information('1', 'm', '10', 5)
information2 = Information('2', 'f', '5', 2, datetime.date(2001, 10, 12))
information3 = Information('3', 'm', '100', 1, datetime.date(1998, 10, 1))
information4 = Information('4', 'm', '100', 4, datetime.date(1991, 10, 1))

Information.readData()



# num = int(input("Enter the number of Employees :"))
# for i in range(num):
#     Employees[i] = Information()
#     print(f"\n|--Supply data for employee #{i + 1}--|")
#     Employees[i].get()
#     Employees[i].getDOJ()


