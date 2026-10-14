import pandas as pd

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
