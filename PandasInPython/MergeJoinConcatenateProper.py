import pandas as pd

player = ['player1', 'player2', 'player3']
point = [45, 67, 34]
title = ['Game1', 'Game2', 'Game3']

df1 = pd.DataFrame({'player': player, 'point': point, 'title': title})
df11 = pd.DataFrame({'players': player, 'points': point, 'titles': title}, index=[1,2,3])
#print(df11)



player = ['player4', 'player5', 'player6']
point = [2, 4, 6]
title = ['Game1', 'Game2', 'Game6']

df2 = pd.DataFrame({'player': player, 'point': point, 'title': title})
df22 = pd.DataFrame({'player': player, 'point': point, 'title': title}, index=[2,3,4])
#print(df22)



# print(df1.merge(df2, on='title', how='inner'))
# print(df1.merge(df2, on='title', how='right'))
# print(df1.merge(df2, on='title', how='left'))
# print(df1.merge(df2, on='title', how='outer'))

#for joins--> index paramenter should be provided n the dataframe and column name of both the dataframes should be different
print(df11.join(df22, how='inner'))
print(df11.join(df22, how='right'))
print(df11.join(df22, how='left'))
print(df11.join(df22, how='outer'))


#print(pd.concat([df1,df2], ignore_index=True))

