a = 3
b = 7
c = sum((a, b))  # built in functions
print(c)


# userdefined functions

def multi_functions():
    """
    This is a doc string of functions returns multiple of two numbers
    """
    a = 3
    b = 4
    c = 3 * 4
    print(c)


multi_functions()
print(multi_functions.__doc__)
