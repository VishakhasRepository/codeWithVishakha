import pandas as pd


titanic = pd.read_csv("train.csv")


def update_age(row):
    row_Age = row.fare + 22
    return row

titanic = titanic.apply(update_age, axis = 'columns')
#print(titanic)

#apply method is useful for passing a lambda function or any other function

df1 = pd.DataFrame(
    {
        'StudentID' : [1,2,3],
        'Name' : ['Hari', 'Prasad', 'Raj']
    }
)

df2 = pd.DataFrame(
    {
        'StudentID' : [1,3,5],
        'Marks' : [99, 84, 33]
    }
)

df3 = pd.DataFrame(
    {
        'StudentID' : [5,6,7],
        'Name' : ['Praveen', 'Naveen', 'Ashish']
    }
)


print(pd.concat([df1, df3]))

df1.set_index('StudentID', inplace = True)
df2.set_index('StudentID', inplace = True)
print(df1.join(df2, on = 'StudentID', how= 'inner', lsuffix = '_df1', rsuffix = '_df2'))  #returns the matched records

print(pd.merge(df1, df2, on='StudentID'))
