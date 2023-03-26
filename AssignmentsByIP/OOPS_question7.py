# Q7. Create a program in python to demonstrate Polymorphism.
# 1. Make use of private and protected members using python name mangling techniques.


class MainClass:
    def __init__(self, name, name2, procName):
        self.__name = name    #private variable
        self.__name2 = name2  #private variable
        self._procName = procName  #protected variable


class ChildClass1(MainClass):
    def __init__(self, name, name2, procName):
        super().__init__(name, name2, procName)
        self.name = name

    def displayProtectedVariable(self):
        return self._procName


childCLass = ChildClass1("Intellipaat", "Intellipaat2", "protectedName")

print(childCLass.name)  #overriding the name variable in subclass
print(childCLass._MainClass__name2)  #accessing the private variable
print(childCLass._MainClass__name)  #accessing the private variable
print(childCLass.displayProtectedVariable())   #accessing the protected variable







