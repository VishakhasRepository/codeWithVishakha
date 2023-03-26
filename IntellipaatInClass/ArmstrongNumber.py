

# def isArmstrongNumber(num):
#      a = str(num)
#      sum = 0
#      for i in a:
#          sum = sum + pow(int(i),3)
#      if num == sum:
#          print("yes it is")
#      #print(sum)


def isArmstrongNumber(n):
    sum = 0
    while(n>0):
        r = n % 10
        sum = sum + pow(r, 3)
        n = n//10
    print(f"sum is", sum)
    if sum == n:
        print("yes it is")


print(isArmstrongNumber(371))


