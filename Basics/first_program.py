import pandas as pd
import numpy as np

s1 = pd.Series([11,22,33,44,55])

print(s1)

s1.iloc[3]

s1.iloc[2]

# marks series

marks = pd.Series([88,56,69,60,65], index=['maths','eng','sci','geo','history'])

print(marks)

marks.loc['eng']

print(marks.at['eng'])

marks.at['eng'] = 91

marks.at['geo'] = 95
print(marks.at['geo'])

# accessories
accesseries = pd.Series(['laptop','mouse','keyboard'], index = [60000, 500, 1200])


print(accesseries)

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'City': ['Mumbai', 'Delhi', 'Pune']
}

df = pd.DataFrame(data)

print(df)

# create with dict

age = pd.Series({
  'ram':24,
  'krishna':34,
  'shiv':25
})

print(age)



# ---------------#

s = pd.Series(
  [10,33,56,67,72,79,12],
  index = ['A','B','C','D','E',''F','G']
)

print(s.loc['A'])
print(s.iloc[0])

print(s.at['A'])
print(s.iat[0])


s1 = pd.Series(
   [11,22,33,44,55],
   index = ['0', '1', '2', '3', '4']
)


print(s1)
s1.loc[ 3]
s1.iat[ 3]

sales = pd.DataFrame{
    'Product_Name':['laptop','mouse','keybord'],
    'Price':[12000,500,600]

}
print(sales)
df.iloc[2]

# Creating DataFeam

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'City': ['Mumbai', 'Delhi', 'Pune']
}

# reading null values

df = pd.DataFrame(data)

print(df)
# Reading csv file
df.isna()

for i in df:
print(df)

# finding mean
#see the correlation in heatmap

fig = plt.figure(figsize=(20,10))

ax = fig.add_subplot(1, 1, 1)
ax.set_title('Correlation Between Variable')

sns.heatmap(ibm4.corr(),vmin=-1,
            vmax=1,cmap='RdYlGn',annot=True,
            annot_kws={"fontsize":7}, fmt=",.2f")

plt.show()


### reserve for work
