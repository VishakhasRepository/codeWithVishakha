import numpy as np

def numpyFunc(tupVar1, num):
    a = np.full(tupVar1,num)
    return a

#print(numpyFunc((3,3),5))


def sumNumpyArrays(arr1, arr2):
    return arr1+arr2

a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
b1=np.array([[2,4,6],[3,2,1],[6,5,4]])
#print(sumNumpyArrays(a1,b1))

#convert 1d array to 2d np array
# a2=np.array([1,22,3,42,5,6])
# print(a2.reshape(2,3))
# a2.sort()
# print(a2)
# print(a2[2:])

ss = np.arange(2,11).reshape(3,3)
#print(ss)

ss2 = np.array([1,2,3,4], dtype=float)
#print(ss2)
ss3 = np.array([10,20,30])
ss4 = np.array([40,50,60,70,80,90])

#print(np.append(ss3,ss4))

#add two arrays in two ways

ss6 = np.array([1,2,3])
ss7 = np.array([4,5,6])
ss8 = np.sum([[1,2,3],[4,5,6]], axis=0)
print(ss8)
ss9 = np.add(ss6,ss7)
print(ss9)

arr4= np.arange(10,100,10).reshape(3,3)
print(arr4[0])  #first row
print(arr4)
print(arr4[2,2])  #last element

