list1 = []
for i in range(1, 101):
    list1.append(i)
list1.remove(33)

print(list1)

def findMissingNumber(list2):
    for i in range(1, 101):
        if i not in list2:
            print("The missing number is - " + str(i))

print(findMissingNumber(list1))

#how to find missing number by using sum of all the values

def findMissingNumberPart2(lis3, n):
    sum1 = 100*101/2
    sum2 = sum(lis3)
    y = sum1 - sum2
    print(y)

print(findMissingNumberPart2(list1, 2))




