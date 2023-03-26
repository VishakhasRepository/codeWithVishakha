import pandas as pd

df = pd.read_csv('cars.csv')
# print(df.tail())
# print(df.head())
# print(df.describe())
# print(df.info(show_counts=True))  #this tells about the null values if presnet in any column
#
# print(df.mean(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.std(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.min(numeric_only=True))
# #display number of non null record in each column
# print(df.count())

# cleaning the dataset
# drop unnecessary columns
#renaming a column
#df1 = df.rename(columns={'mpg':'mpg2'})

#treating null values

#df.mpg = df['mpg'].fillna(df.mpg.mean())

#drop unwanted columns
#df.drop(columns='brand')

#finding corrleation matrix, no corr for string values

#print(df[['mpg', 'cylinders', 'hp','weightlbs']].corr())

#changing the data type
df.mpg = df.mpg.astype(float)

#manipulating a dataset
#pandas provides functionality to of slicing in pandas dataframes using iloc function


#get the fourth column of the dataframe

#print(df.iloc[:5,4])

#view record on the name of the attribute also, here loc is location

#print(df.loc[:,'mpg'])

#first 7 records from qsec to mpg column
#print(df.loc[:6,'mpg': 'hp'])

#set specific value to the entire collumn
# df['mpg'] = 1
# print(df)

#use lambda functions
x = lambda y : y*2

#df['mpg'] = df['mpg'].apply(x)


#sorting the data in aascending order
#df.sort_values('cylinders', ascending=True)

#filterig the data
print(df['mpg']> 22)

filter1 = (df['mpg'] > 17) & (df['cylinders'] > 3)
print(df[filter1])


