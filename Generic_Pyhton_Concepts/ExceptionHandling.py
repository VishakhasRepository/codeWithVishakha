

num1 = (input("Enter num 1"))
num2 = (input("Enter num 2"))

try:
    print("The sum of these two numbers are - ", int(num1 + num2))
except Exception as e:
    print(e)

print("This line is very important")
