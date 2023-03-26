numbers = ["3", "4", "5"]
# numbers[2] = numbers[2] + 1  #not possible this concatenation

# How to convert integer string list into numbers list

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])  # inside range function, it should be integer

numbers[2] = numbers[2] + 1
print(numbers[2])

# So everytime running for loop is not a good idea when we can do same kind of conversion in one line using map function

numbers = list(map(int, numbers))  # convert map into list
numbers[2] = numbers[2] + 1
print(numbers[2])


def square(a):
    return a * a


res = list(map(square, numbers))
print(res)

# using lambda
res = list(map(lambda x: x * x, numbers))
print(res)


# now using a list of functions using lambdas
def cube(a):
    return a * a * a


def square2(a):
    return a * a


func = [square, cube]  # passing functions in list
num = [1, 2, 3, 5, 7, 8, 33]
for i in num:
    res2 = list(map(lambda x: x(i), func))   #interesting one
    print(res2)