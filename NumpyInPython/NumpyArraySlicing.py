import numpy as np

arr = np.array([['a','b','c'],['w','e','r'],['t','y','u']])
print(arr[0])


print([arr[0][1]])
print([arr[0:1]])  #print 0th row
print([arr[:2]])  #print 0th and 1st row
print([arr[:3]])   #print 0th 1st and 2nd row

print([arr[2]])  #print 3rd row

print([arr[:,2]])
print([arr[:],[2]])   #all rows second column

print(arr[0,1:3])  #print 0th row and column from 1 to 2
print(arr[0,1:])
print(arr[0,(1,2)])
print(arr[1:,(0,2)])
print(arr[1:3,(1,2)])
print("------------------------")
print(arr[1:,(0,)])
print(arr[1:,0:3])
print("------------------------")
print(arr[(0,2),(0,2)])  #this is interesting
print(arr[(0,2)[0:3]])

print("------------------------")
print(arr[:,-1])   #last column