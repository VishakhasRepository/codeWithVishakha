# creating a first class in python

class Student:
    pass


harry = Student()  # here Student() is a object
larry = Student()  # here Student() is a object

# instance variables of class student, harry and larry are instance of student class
harry.name = "Vishakha"
larry.name = "Larry"
harry.std = 8
larry.std = 88
larry.subjects = ["Eng", "Hindi"]

print(larry.std, harry.name)
