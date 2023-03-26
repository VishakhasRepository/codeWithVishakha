# Create a function named ‘factor’ that can only accept 1 argument. The function should
# return the factorial of that number.

#using recursion
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

#print(fact(7))

#without recursion
def factorial(y):
    fact = y
    while y != 1:
        fact = fact*(y-1)
        y = y-1
    return fact

print(factorial(7))




