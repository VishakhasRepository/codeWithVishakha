import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('employees .csv')

#print(data.shape)

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#print(list(data.columns))

features = ['lastEvaluation', 'numberOfProjects', 'workAccident', 'left', 'promotionInLast5years', 'dept']

for i,j in enumerate(features):
    plt.subplot(3,2, i+1)
    #sns.countplot(x = j, data=data,  hue= 'left' )
    plt.subplots_adjust(hspace=1.0, wspace=1.0)
    sns.countplot(x=j, data=data, hue='left')
    plt.xticks(rotation = 90)
    plt.subplot(3, 2, i + 1)

plt.show()





