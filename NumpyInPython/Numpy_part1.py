import numpy as np

# print(np.array([1,2,3,4,5]))
# print(np.zeros((3,4)))
# print(np.arange(10,20,2))
# print(np.linspace(10,20,12))
# print(np.full((3,3), 6))  #all the values initialized to 6
# print(np.random.random((2,3)))

# a = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(a.shape)
#
# a.shape = (5,2)  #changing the size of the array
# print(a)

# b = np.arange(24)
# print(b.ndim)
# c = b.reshape(2,4,3)  #any number whose product is 24
# print(c)
#
# print(b.size)  #24
# d = np.arange(24, dtype=float)
# print(d.dtype)
# print(d)
#
# print(np.sum([20,30]))
# print(np.sum([[20,30],[2,5]], axis=0)) #addition for all column values
# print(np.sum([[20,30],[2,5]], axis=1)) #addition for all row values
# print(np.sum([[20,30],[2,5]])) #addition for all  values
# print(np.subtract(10,20))
# print(np.multiply(10,20))
# print(np.divide(10,20))
# a1 = np.array([2,4,6])
# b1 = np.array([4,5,6])
# print(np.multiply(a1,b1)) #sum,subtract,divide,multiply all operations are possible

# print(np.exp(a1))
# print(np.sqrt(a1))
# print(np.sin(a1))
# print(np.cos(a1))
# print(np.log(a1))

#Array wise comparison

arr1 = [1,2,4]
arr2 = [4,5,6]
arr3 = [7,8,9]

# print(np.equal(arr1,arr2))  #compares with each other elements
# print(np.array_equal(arr1,arr2))  #Array wise comparison
#
# #Aggregate function
#
# print(np.sum(arr1))
# print(np.min(arr1))
# print(np.mean(arr1))
# print(np.median(arr1))
# print(np.corrcoef(arr1))
# print(np.std(arr1))


#numpy broadcasting
#when the arrays are not with equal elements

# arr4 = np.array([1,2,4])
# arr5 = np.array([[1,2,4],[1,2,3],[4,5,6]])
# print(arr4+arr5)

#Concatenation of array
# arr11 = np.array([1,2,4])
# arr22 = np.array([4,5,6])
# print(np.concatenate((arr11,arr22)))
# print(np.vstack((arr11,arr22)))
# print(np.hstack((arr11,arr22)))
# print(np.column_stack((arr11,arr22)))

x = np.arange(16).reshape(4,4)
# print(x, "\n\n")
#
# print(np.hsplit(x,2))
# print(x, "\n\n")
# print(np.vsplit(x,2))

print(x, "\n\n")
print(np.hsplit(x,np.array([3])))
print("\n\n")
print(np.hsplit(x,np.array([2,3])))









