import numpy
import pandas as pd

df = pd.DataFrame(
    {
        'Name' : ['Hari', 'Raj'],
        'Age' : [39,23]
    }

)

print(df.Age)
print(df.Name)

titanic = pd.read_csv("train.csv")
print(titanic.head())   #print top 5
print(titanic.tail())  #print last 5

print(titanic.head(7))
print(titanic.shape)
print(titanic.info())
print(titanic.columns)
print(titanic.age.max())
print(titanic.age.min())
print(titanic.age.mean())
print(titanic.age.median())
print(titanic.describe())
print(titanic.survived)  #this way also and the below way also
print(titanic['survived'])
print(titanic['survived'][7])  #accesing a specific element using an index value
print(titanic.iloc[0:3, 1:3])  #rows selection and column selection , index based selection, end index is excluded
print("-------------")
print(titanic.loc[0:4, 'name'])  #label based selection, last index is also included
print(titanic.loc[0:4, ['name', 'survived']])  #label based selection, last index is also included

print(titanic.sort_values(by='pclass', ascending = False))
print(titanic.embarked=="S")
print(titanic[titanic["embarked"]=="S"])
print(titanic[(titanic["fare"] > 50) & (titanic["embarked"]=="S")])
print(titanic[titanic["fare"]>50].fare.mean())

print(titanic[(titanic["fare"] > 50) & (titanic["embarked"]=="S")][["name", "fare", "embarked"]])   #here double brackets
print(titanic[(titanic["fare"] > 50) & (titanic["embarked"]=="S")][["name", "fare", "embarked"]].fare)   #here double brackets

print(titanic.corr())
print(numpy.corrcoef(titanic.parch.to_numpy(), titanic.survived.to_numpy()))

#to_csv
titanic[['name', 'age']].to_csv('filtered.csv', index = False)

#Cleaning in data frames
print("----------------------")

print(titanic[titanic.age.isna()])  #where age is null
titanic.age.fillna(8)

print(titanic.age)
print("-----------------------------------------------------------------------------------")
titanic.age.fillna(titanic.age.mean(), inplace = True)
titanic.rename(columns= {'age', 'agee'})  #rename the column name

#change the datatype of a column
titanic.pclass = titanic.pclass.astype(float)

def update_age(x):
    return x**2

titanic.age = titanic.age.map(lambda x : update_age(x))
