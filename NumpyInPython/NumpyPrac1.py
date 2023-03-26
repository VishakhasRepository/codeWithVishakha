import numpy as np

# a = np.arange(24)
# print(a.ndim)
# b = a.reshape(6, 2, 2)
# print(b)
# print(b.ndim)
# print(b.shape)  #(6,2,2)
# c = np.arange(1,10,2)
# print(c)
#
# print(np.eye(3))
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
#
# print(np.multiply(a1,b1))
#
# print(np.exp(a1))
# print(np.sqrt(a1))
# print(np.sin(a1))
# print(np.cos(a1))
# print(np.log(a1))

df = np.arange(1,10).reshape(3,3)
print(df)
maxvalue1 = df.max(axis = 0)  #maximum values across columns
maxvalue2 = df.min(axis = 1)  #maximum values across rows
print(maxvalue1)
print(maxvalue2)

print(maxvalue1-maxvalue2)