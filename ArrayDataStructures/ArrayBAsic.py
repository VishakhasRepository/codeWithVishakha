#Array has specific type
#definite size cannot be modified
#arrays represented in physical memory - all in sequential order-  1 d, 2d, multi D

from array import *  #array can be defined in python by impodting array module
arrayName =  array('i', [1,2,3,4,55])  #int array
arrayName2 =  array('d', [1.3,2.2,3.3,4.4,5.6])  #double array
print(arrayName)
print(arrayName2)
arrayName.insert(6, 6) #inserting in the end - constant time - O(1)
print(arrayName)

arrayName.insert(0, 3) #insering in begining/middle/array is full- time consuming operation - O(N) time complexity
print(arrayName)
print(arrayName[2])

#travering an array is also O(N) and printing a element is O(1)
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)


print(searchInArray(arrayName, 55))  #reuturns index of the value present in array