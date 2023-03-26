import numpy as np

# def funcNumpy(n,m, arr1):
#     return arr1[0:2,1:].reshape(n,m)
#
#
# arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
# print(funcNumpy(2,2,arr2))

# def funcNumpy2(n,m, arr1):
#     return arr1[1:,1:].reshape(n,m)
#
#
# arr2 = np.array([[1,2,3],[1,2,3],[4,5,6]])
# print(funcNumpy2(2,2,arr2))

arr2 = np.array([1,1,1])
def func2(arr3):
    stdev = np.std(arr3)
    mea = np.mean((arr3))
    dict1 = {}
    dict1['mean'] = mea
    dict1['std_dev'] = stdev
    return dict1


print(func2(arr2))