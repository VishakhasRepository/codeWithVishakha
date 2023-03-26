import pandas as pd


df = pd.read_csv('Factory_Salary.csv')

# a = [1,2,3,4]
# a2 = pd.Series(a)
# #add into series
# s2 = pd.Series([0], index=['a'])
# print(s2.append(a2))
#
#
# #update a series
# a2[2] = 'ass'
# #delete
# a2.pop('a')
# print(s2)

#delete
#print((del s2['a']))
# tup1 = (1,2,3,4)
# print(pd.Series(tup1).append(2))

# dict1 = {1:2, 3:4, 4:5}
# print(pd.Series(dict1))
#
# set1 = {1,2,3,4}
# print(pd.Series(list(set1)))

#Access the elements of the series using position and indexing
s = [1,2,3,4,5,6]
pds = pd.Series(s)
# print(pds[2:3])
# print(pds.index)
# print(pds.loc[1:3])

#add
# s1.add(s2)
#subtract
# s1.subtract(s2)

print(pds.tolist())
print(pds.to_dict())
print(tuple(pds))
print(set(pds))














