
import pandas as pd
from ordered_set import OrderedSet

# tup1 = tuple(range(1,11))
# set1 = OrderedSet(range(1,11))
# list1 = list(range(1,11))
#
# #converting list into series
# list2 = pd.Series(list1)
# print(list2)
# print(type(list2))
#
# #converting set into series
# set2 = pd.Series(data = set1)
# print(set2)
#
# #converting tuple into series
# tup2 = pd.Series(data = tup1)
# print(tup2)
#
# #create seperate list of index values for series like customizing
# index1 = ['a','b','c','d','e','f','g','h','i','j']
# print(pd.series(set2, index = index1))


dict1 = {'k1': 22, 'k2': 33, 'k3': 44}
#print(pd.Series(dict1))

series1 = pd.Series((1,2,3,4,5,6,7))
# print(list(series1))
# print(set(series1))
# print(tuple(series1))
# print(dict(series1))


# print(series1.head(5))
# print(series1[1:5])
# print("----------------------")
# print(series1.tail(5))
# print(series1[-5:])

series1[5] = 50

series1[9] = 100

#print(series1)

series1.pop(0)
#print(series1)

# seriesA = pd.Series([1,2,3,4,5])
# seriesB = pd.Series([6,7,8,9,10])
# seriesC = pd.concat([seriesA,seriesB], ignore_index=True)
#
# print(seriesC)

# sample = pd.Series([1,2,3,4,5,6,7,8,9,10])
#
# List1 = [['AA', 'BB', 'CC'], ['DD', 'EE', 'FF'], ['GG', 'HH', 'II']]
# dict1 = {'Kris': ['jordan', '12', '22'], 'memphesis' : ['asd', 22, 55] }
# print(pd.DataFrame(List1))
# print(pd.DataFrame(dict1))

data1 = [['akash', 25], ['nick', 33], ['joy', 34]]
#print(pd.DataFrame(data1))
df3 = pd.DataFrame(data1, columns=['Name', 'age'])
#print(df3)
#print(df3.head(3))
# print(df3[df3.age>25])
#
# df3.loc[4] = ['Aman', 22]
# print(df3)
#
# df3.loc[4, 'Name'] = 'asas'
# df3.loc[4, 'age'] = 22
#
#
#
#
# df3.drop(0)
#
# list1 = list(df3.values)
# print(list1)  #[array(['akash', 25], dtype=object), array(['nick', 33], dtype=object), array(['joy', 34], dtype=object), array(['asas', 22], dtype=object)]

A = pd.DataFrame(list(range(1,21)), columns=["A"])
B = pd.DataFrame(list(range(12,21)), columns=["B"])


df4 = pd.DataFrame(
    {
        'name' : ['vishakha', 'vishi', 'vishu', 'vish', 'wishu', 'wish'],
        'age'  : [29,21,24,25,26,28],
        'Gender': ['F', 'M', 'F', 'F', 'M', 'F']
}
)

print(df4[df4.age==20])
print(df4.sort_values(by='age', ascending=True))

l = []
for i in range(len(df4)):
    l.append(df4.loc[i,'age'])  #pick from age column, the ith value

print(l)

