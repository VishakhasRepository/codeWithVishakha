

import numpy as np

arr = np.array([1,2,3,4,5])

def findNumber(arr, number):
    for i in arr:
        if number == i:
            print("yes")

#findNumber(arr, 3)


#Findthe missing number in given array

def missingNumber(myList, totalCount):
    for i in range(totalCount-1):
        if (i+1) != myList[i]:
            return i+1

#print(missingNumber([1,2,3,4,6], 6))


#We can find the missing number using sum also

def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)  #used formula = n(n+1)/2  to get the sum of all integers
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)


#Find the duplicate number on any given integer array list , duplicates must be removed

myList = [1,1,2,2,3,4,5]
def removeDuplicates(myList):
    newList = []
    for i in myList:
        if i not in newList:
            newList.append(i)
    return newList


#print(removeDuplicates(myList))


#find all pairs of integer whose sum is equal to a given number

list1 = [2,4,3,5,6,-2,4,7,8,9]
def pairSum(myList, sum):
    dem = []
    for i in range(0, len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                dem .append(str(myList[i]) + "+" + str(myList[j]))
    return dem





print(pairSum(list1,7))