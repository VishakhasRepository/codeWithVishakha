def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))

str1 = "input()"
if "s" in str1:
    print("yes")



# class Student:
#     def fun1(self):
#         return input()
#
#     def message(self):
#         print(self.fun1())
#
# stu = Student()
# stu.message()


# double_num = lambda x : x*2
#
# print(double_num(3))

# def palindromeNumber(n):
#     print(n[::1])
#     return n[::-1] == n
#
#
# print(palindromeNumber("eye"))

class Super:
    def fun1(self):
        print("This is fun1 in super class")

class Modified_super(Super):
    #super().__init__(self)
    def fun1(self):
        print("THis is function1 in modified super class")

    def fun2(self):
        print("THis is the second function from modifies super class")

obj = Modified_super()
obj.fun1()

class poly:
    def hello(self, n):
        print("only one argument")

#     def hello(self, n, m):
#         print("this has two arguments")
#
# class poly2(poly):
#     def hello(self, n, m):
#         print("this has two arguments")
#
#
#
# obj1 = poly()
# obj1.hello(3)


class Encapsulaion:
    def __init__(self):
        self.originalVal = 10

    def value(self):
        return self.originalVal

    def setValue(self, newValue):
        self.originalVal = newValue


obj4 = Encapsulaion()
print(obj4.originalVal)
obj4.setValue(23)
print(obj4.originalVal)









