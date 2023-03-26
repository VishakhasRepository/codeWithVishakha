import switch as switch

operator = input("Which operator you wanted to use?")
print(operator)
num1 = int(input("Write first number"))
num2 = int(input("Write second number"))

if operator == "*" and num1 == 45 and num2 == 3:
    print("555")
elif operator == "+" and num1 == 56 and num2 == 9:
    print("77")
elif operator == "/" and num1 == 56 and num2 == 6:
    print("4")
else:
    if operator == "+":
        print(num1+num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
