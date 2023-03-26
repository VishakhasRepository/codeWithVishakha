# Lambdas are like anonymous functions and it is also called one liner functions

minus_lambda = lambda x, y: x - y


# the above one liner is same as below
def minus_function(x, y):
    return x - y


print(minus_lambda(8, 7))
print(minus_function(8, 7))

print("--------------------------------------------------------------------------------------------------------")


def a_first(a):
    return a[1]


listOfList = [[2, 7], [5, 6], [7, 8]]
listOfList.sort(key=a_first)
print(listOfList)

# using lambda functions

#a_first = lambda a: a[1]
listOfList = [[2, 7], [5, 6], [7, 8]]
listOfList.sort(key=lambda a: a[1])   #this is the way to use lambda functions
print(listOfList)

