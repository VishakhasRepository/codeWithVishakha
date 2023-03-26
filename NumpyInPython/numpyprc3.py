import numpy as np

# arr = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
# print(arr)
# print(arr.shape)
# print(arr.size)
# print(arr.ndim) #provides dimensions
# print(arr.dtype)
# print(arr.data)  #Buffer containing Actual Elements of the array, address or memory location
# print(arr.itemsize) #Size of bytes of each element of the array


# list1 = [1,2,3,4,5]
# tup1 = (1,2,3,4)
# dict1 = {'key1': 'asdf', 'key2': 'werw'}
# set1 = {1, 2, 3, 4}
# print(np.array(list1))
# print(np.array(tup1))
# print(np.array(dict1.items()))
# print(np.array(list(set1)))

#print(np.arange(1,10).reshape(3,3))
#print(np.full((4,4),'k'))
# print(np.full((4,4),'k'))
# print(np.full((2,2),''))
# print(np.empty([2,2]))
# print(np.array(()))  #empty array
#
# print(np.linspace(12,15,5, dtype=int).reshape(2,2))

arr2 = np.arange(1,10).reshape(3,3)
# #[startrow:end+1_row, startcolumn:end+1_column]
# print(arr2[:,:])
# #print(arr2[-3:,-3:])
# #print(arr2[1:2,])
# print(arr2[2:,2:])
#
# for i in arr2.flat:
#     for j in i:
#      print(j)

arr3 = np.arange(1,10).reshape(3,3)
arr4 = np.arange(1,10).reshape(3,3)
# print(arr3)
#print(arr3[::-1])
#print(np.flip(arr3))
#print(arr3[::-1])
# print(arr3.transpose())
# print(arr3.T())  #transpose of an array
# #flatten a array
# arr4 = arr3.ravel()
# arr5 = arr3.flatten()
# print(arr4)
# print(arr5)

onedarray = np.array([1,2,3,4])
twodarray = np.array([[1,2,3,4],[2,3,7,8]])
threedarray = np.array([[[1,2,3,4],[5,6,7,8], [12,33,44,55]]])
#print(np.vstack(onedarray))
#print(np.hstack(onedarray))

# print(np.column_stack(twodarray))
# print(np.vstack(twodarray))
# print(np.row_stack(twodarray))
# print(np.hstack(twodarray))
#print(arr3)
#print(np.hsplit(arr3, np.array([2,2])))
#print(np.hsplit(arr3, 2))
#print(np.vsplit(arr3, np.array([2,2]))
#print(np.vsplit(arr3, 2))
# print(np.array_split(arr3, 1))

#t is a popular function in Python used to modify the dtype of the NumPy array we've been provided with
#print(arr3.astype(float))
a = [1,2,3,4]
#Type conversion using atleast_1d
# print(np.atleast_1d(a))
# print(np.atleast_2d(a))
# print(np.atleast_3d(a))
# print(np.matrix(a))
# print(np.where(arr3>6, 'ss', (np.where(arr3>3), 'rr', 'yy')))
# print(np.where(arr3>6, arr3+2, arr3-4 ))

#print(np.concatenate(twodarray))
#print(np.diagonal(arr3))
#print(np.dsplit(threedarray, 2))

# print(np.reshape(arr3, (9,1)))
# print(np.resize(twodarray, (4,2)))
#print(np.repeat(twodarray, 2))

#squeeze() function is used when we want to remove single-dimensional entries from the shape of an array
srr = np.array([1,2,3,4,5])
#print(np.squeeze(srr, axis=None))
# srr3d = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
# print(np.swapaxes(srr3d, axis1=0, axis2=2))
# print(np.take(srr, indices= 1, axis=None, out=None, mode='raise'))
# print(np.ndarray.item(srr, 2))

# print(np.mean(twodarray))
# print(np.var(twodarray))
# print(np.std(twodarray))
# print(np.cov(twodarray))

alg1 = np.array([[13,7],[5,6]])
alg2 = np.array([[1,2],[5,6]])

# print(np.cross(alg1,alg2, axis=1))
# print(np.dot(alg1,alg2))
# print(np.outer(alg1,alg2))
# print(np.vdot(alg1,alg2))



# print(np.argmax(alg1))
# print(np.argmin(alg1))
# print(np.argsort(alg1))
# print(np.min(alg1))
# print(np.max(alg1))
# print(np.searchsorted(alg1, 0, sorter=None))  #not working
# print(np.sort(alg1))

#print(arr3)
# print(np.concatenate(arr3 , [10]))
# print(np.insert(arr3 , (0), 10))
# print(np.append(arr3, 10))
#print(np.insert(arr3,  10)) #insert in between?

#update an element
# arr3[2,1] = 22
# print(arr3)


#print(np.choose([2, 0, 1], choices=arr3))
#print(np.compress([1, 1], arr3, axis=0))
#print(np.cumprod(arr3))
#print(np.cumsum(arr3))
#print(np.inner(np.array([1,2,3]),np.array([10,1,0])) )
# a = np.empty([3, 3])
# print(a.fill(7))
# print(a)
# arr = np.array([1 + 3j, 5 + 7j, 9 + 11j])
# print(np.imag(arr))
#print(np.prod(arr3))




