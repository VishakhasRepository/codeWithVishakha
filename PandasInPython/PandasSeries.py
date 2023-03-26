import pandas as pd
import numpy as np


print(pd.Series())  #empty series with default data type as float
print(pd.Series([1,2,3,4,5]))  #list

print(pd.Series(np.array([1,2,3,4,5])))  #numpyArray
print(pd.Series((1,2,3,4)))   #tuple
print(pd.Series({"sd":"wer", "qww":"rtrt","rtrt":"xcxc"}))   #DIctionary
print("-------------")
print(pd.Series(20))
print(pd.Series(range(2,11,2)))

#can change the indexes also from numbers to albhabets

s = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd']) #labelled index only in pandas not possible in numpy
print(s['a'])


s2 = pd.Series([1,2,3,4], index = range(4,8))
print(s2)

#update the values in panda series
s[2] = 22
print(s)

#update the index in panda series from numerical to alphabets
s.index = ['a', 'b', 'c', 'd']
print(s)

s.rename(index={'b': 'bb'}, inplace = True)  #replacing a particular index with the particular value, here inplace means the index gets updated in current series only when inplace is not specified than value is not updated in current series
print(s)

s3 = s.rename(index={'d': 'dd'})
print(s3)

s.sort_values(ascending=False, inplace=True)
print(s)
s.sort_index()
print(s==2)
#mean and medium can also be added here
