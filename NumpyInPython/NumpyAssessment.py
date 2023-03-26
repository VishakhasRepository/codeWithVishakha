import numpy as np

from scipy.signal import argrelextrema

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[(4<arr)&(arr<7)] * -1)

# a=np.array([2,10,12,20,55])
#
# b=np.array([5,10,33,66,99])
#
# aa = np.add(a,b)
# print(aa)
# bb = np.multiply(aa,a)
# print(bb)
#
# a1 = np.array([9, 8, 7, 1, 3, 1, 2], ndim=3)
#
# print(a1)

# x = np.array([55,67,87,75,11])
# x2 = np.array([11,75,87,67,55])
#
# y = np.array([32,22,11,15,99])
# y2 = np.array([99,15,11,22,32])
#
# print(np.corrcoef(y2, x2))
# print(np.corrcoef(x, y))



# x = np.array([1,78,87,99])
#
# y = np.array([37,45,55,23,43,56])
#
# z = np.array([21,2,93,53,87,99])
#
# x, y, z = np.ix_(x,y,z)
#
# print(x)
#
# a4 = np.array([22, 33, 45, 67, 89, 11, 111, 23, 45])
#
# print(np.sum(a4))
# print(np.min(a4))
# print(np.max(a4))
# print(np.std(a4))
#
# a5 = np.array([1, 3, 7, 1, 2, 6, 0, 1])
# print(argrelextrema(a5, np.greater))
#
# a7 = np.array([2, 7, 5])

# a = np.array([2, 7, 5])
#
# b1= np.zeros((a.size,a.max()+1))
# b= np.zeros((a.size,a.var()+1))
# b[np.arange(a.size),a] = 1
#
# print(b)
#
# np.random.seed(10)
#
# a = np.random.randint(2,12, [7,5])
# print(np.min(a)/np.max(a))

a = ([69.85714286, 69.71428571, 69.57142857, 69.42857143, 69.28571429,

       69.14285714])

print(np.average(a))

