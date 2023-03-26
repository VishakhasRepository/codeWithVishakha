# 0 1 1 2 3 5 8 13

#using recursion --->may face difficulty in backtrace
def fibonacci_function(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci_function(m - 1) + fibonacci_function(m - 2)


num = int(input("Enter number - "))
print(fibonacci_function(num))
