class Employee:
    change_salary = 5
    name = "vishakha"
    age = "28"

    def __init__(self, achange_salary, achange_name, achange_age):
        self.change_salary = achange_salary
        self.name = achange_name
        self.age = achange_age



    @classmethod
    def getparams(cls, achange_salary):
        cls.change_salary = achange_salary

    @classmethod
    def use_as_alterantive_constructor(cls, param):
        return cls(*param.split('-'))


obj1 = Employee.use_as_alterantive_constructor("344-vishakha-30")

print(obj1.change_salary)

