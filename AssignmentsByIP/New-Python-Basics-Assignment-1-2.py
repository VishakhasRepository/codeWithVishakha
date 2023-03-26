
#Solution1
import math


class Calculator:
    def pythonAsCalculator(self):
        n,r,p = 10,5,100
        amount = p * pow((1+r/100), n)
        return amount

calc = Calculator()
#print(calc.pythonAsCalculator())

#Answer is b --> 162.89

#Solution2
a = 10
b = 20
str = "There are {} students in the class, with {} who play at least one sport."
#print(str.format(b,a))  #this will work

#Answer is  d

#Solution3

Sampleoutput = "It goes without saying, “Time is Money”, and none can deny it."
#print("It goes without saying, “Time is Money”, and none can deny it.")

#Answer is d

#Solution4
x = lambda a,b: a//b
#print(x(10,3))
#Answer is  b

#Solution5
A = 10
B = 12
#print("Smaller") if A == B else print("Greater") if A < B else print("True")
#Answer is  c


#Solution6
import os
import numpy as np
my_list1 = [2,7,3,5,4,6]
#print(my_list1)
#arr_1 = numpy.array(my_list1, dtype = int)
#print(arr_1)
#Answer is  c


#Solution7
str1 = "Machine Learning"
#print(str1[8:13])
#Answer is  not present in options


#Solution8
list1 = [i+4 for i in range(10, 26)]
#print(list1)
#print(list1.index(18))
#Answer is  not present in options


#Solution9
num1 = 5**4
num2 = pow(5,4)
#print(num1, num2)

#Answer is a

#Solution10
#Trying to access a variable which has not been defined
#Answer is a


#Solution11
#Answer is c


#Solution12
#A file or directory is requested but does not exist in the working directory
#Answer is b


#Solution13
Z = "ID-5632"
#print(type(Z))
#Answer is b


#Solution14
#Answer is d


#Solution15
#Answer is a,c,d


#Solution16
Country = {"India":"Delhi", "China":"Beijing", "Japan":"Tokyo", "Qatar":"Doha", "France":"Marseilles"}
#Country["France"] = "Paris"
#Country.update(France = "Paris")
#Country.__setitem__("France", "Paris")
#print(Country)


#Solution17

tuple_1 = (1,5,6,7,8)
tuple_2 = (8,9,4)
print(tuple_2 + tuple_1)
print(sum(tuple_1))
#tuple_1[3] = 45

#Answer is d


#Solution18
S = {1,2,3,4,4,4,5,6}
print(type(S))
print(len(S))


#Solution19 Write a function which finds all pythagorean triplets of triangles whose sides are no greater than a natural number N.
#a2 + b2 = c2
naturalNumberLimit = 100
for i in range(1, naturalNumberLimit):
    for j in range(i, naturalNumberLimit):
        k = math.sqrt(i*i + j*j)
        if k.is_integer() and k<naturalNumberLimit:
            print(i,j,int(k))













