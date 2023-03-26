import numpy as np
import pandas as pd

def range_series(range1=1, range2=10) :

    return pd.Series(np.arange(range1, range2))

# print(range_series(5,10))
# print(range_series())
# print(range_series(5))

def takesArrayOfSameDimension(arr1, arr2):
    return np.add(arr1,arr2)

z  =  np.array([1,2,3])
z1 =  np.array([1,2,3])
#print(takesArrayOfSameDimension(z, z1))

def create_dataframe(l1, l2):  #interesting question
    return pd.DataFrame(np.transpose(l1), columns=l2)

keys = ['key1', 'key2']
values = [['value1', 'vvv'], ['value2', 'value3']]
#print(create_dataframe(values, keys))

df1 = pd.DataFrame([1,2,3])
df2 = pd.DataFrame([1,2,3])
#concatenate

#print(pd.concat([df1, df2]))

df3 = pd.read_csv('cars.csv')
# print(df3)
# print(df3.describe())
# print(df3.shape)
# print(df3.size)
#slicing in dataframe
#print(df3.iloc[20:200, 2:15])

# print(df3.iloc[-1:,]) #last row
#
# print(df3.tail(10))
# print(df3.tail(100))
print(df3.corr())
#print(df3.corr()[1:2]['mpg'])
df4 = df3.corr()['mpg']

#second highest corr value with respect tp mpg column
df5 = df4.sort_values(ascending=False)[1:2]
#this gives the column name
print(df5.index[0])


