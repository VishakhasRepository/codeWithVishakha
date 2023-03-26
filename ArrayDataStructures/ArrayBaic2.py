
from array import *

array1 = array('i', [1,2,3,4,5,6,2])
array2 = array('i', [1,2,3,4,5,7])
array2.extend(array1)
print(array2)

#Add items from list into array using fromList() method

list1 = [22,33,44,55]
arra3 = array('i', [1,2])
arra3.fromlist(list1)
print(arra3)

#use remove method
arra3.remove(22)
print(arra3)

#reverse an array
arra3.reverse()
print(arra3)

#get array buffer information
print(arra3.buffer_info())

#count the element , no of occurrence

print(array1.count(2))

#convert array to string using string method
strarray=array1.tobytes() #before it was toString method but now it is alias to tobytes() , converting array to string
print(strarray)

ints = array('i')
ints.frombytes(strarray)  #converting string into an array
print(ints)

#convert array to python list

array2.tolist()

#slicing a array
array[1:2]
