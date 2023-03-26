# Q8. Given a list of 50 natural numbers from 1-50. Create a function that will take every element
# from the list and return the square of each element. Use the python map and filter methods to
# implement the function on the given list.
import math


def sqr_natural_numbers(x):
       return x*x

def filter_natural_numbers(i):
    if i > 0:
        return i

list1 = [i for i in range(51)]

list2 = filter(filter_natural_numbers, list1)  #used filter function here

result = list(map(sqr_natural_numbers, list2)) #used map function here

print(result)



