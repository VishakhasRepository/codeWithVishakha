
import numpy as np

twoDimArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(twoDimArray)

#Insertion ,  time complexity of a two dim is O(mn)
twoDimArray[0,0]

newTwoDimArray = np.insert(twoDimArray, 0, [[2,4,6]], axis = 0)  #when axis = 1 then this will add as column , if 0 then row
print(newTwoDimArray)

#add in the end using append function

newTwoDimArray2 = np.append(twoDimArray, [[2,4,6]], axis = 0)
print(newTwoDimArray2)

#accesing a elemt in 2 dim array
#def access(array, rowIndex, colIndex) :

#Difference between a list and array in terms of complexity

#to access a element - array takes O(1) time complexity
#but a list takes O(N) time complexity because to access a element it has to traverse