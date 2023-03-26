import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('BigMartSalesData.csv')
# print(df.count())
# print(df.info(show_counts=True))
#1463 + 2410 = 3873


#print((df['Item_MRP'].describe()))
outletsizemedian = df['Outlet_Size'] == 'Medium'
#print(df[outletsizemedian])


fil = (df['Item_MRP']>200) & (df['Item_Type'] == 'Dairy')
#print(df[fil])
#
# numOfRows = len(df['Item_MRP' == True].index)
#
# print(numOfRows)

#print(df['Item_Fat_Content'].min())
filter1 = (df['Item_Fat_Content'] == 'Low Fat') & (df['Outlet_Type'] == 'Supermarket Type3')

print(df[filter1])

filter2 = (df.Item_Type=='Baking Goods') & (df.Outlet_Type=='Grocery Store')


dfNew = df[filter2]
#print(dfNew['Item_Outlet_Sales'].sum())

filter3 = (df['Outlet_Establishment_Year'] == 1985) & (df['Outlet_Type'] == 'Supermarket Type3')

#print(df.Item_MRP.max())

#print(df[filter3].count())

#print(df[df.duplicated()])

#df.boxplot(column="Item_MRP",by="Item_Fat_Content")


#plt.show()

# a = {'ID': [1, 2, 3], 'Department': ['Content', 'Sales', 'Marketing', ]}
# print(pd.DataFrame(a))

#print(df['Item_Visibility'].describe())