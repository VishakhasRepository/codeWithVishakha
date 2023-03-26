# Pattern printing
""" Take a integer for the number of lines, take a input as 1 or 0 as a boolean value from a user"""
try:

    n = int(input("How many lines you want to print\n"))
    booleanValue = bool(int((input("Type 1 or 0\n"))))
    print(booleanValue)
    if booleanValue:
        while (n > 0):
            print(n * "*")
            n = n - 1
    else:
        y = 1
        while (n > 0):
            print(y * "*")
            y = y + 1
            n = n - 1
except Exception as e:
    print("Invalid input")
