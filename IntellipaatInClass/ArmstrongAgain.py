
def ifArmStrongNumber(x):
    sum = 0
    while x> 0:
        rem = x % 10  #1
        sum = sum + pow(rem, 3)
        x = int(x / 10)
    return sum


print(ifArmStrongNumber(371))
