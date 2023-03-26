class Employee:
    no_of_leaves = 8  # this is the property of the class student

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"Name is {self.name}. Salary is {self.salary} and roles is {self.role}")


class Player:

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        print(f"Name is {self.name}. Game is {self.game}")


class CoolProgrammer(Employee, Player):
    language = "c++"

    def printlanguage(self):
        print(self.language)



karanInstance = Player("Karan", "cricket")
karanInstance.printdetails()
divyeInstance = CoolProgrammer("Divye", "222", "sdasdsad")
divyeInstance.printlanguage()


