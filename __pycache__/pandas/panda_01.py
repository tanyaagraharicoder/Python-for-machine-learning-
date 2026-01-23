import numpy as np

import pandas as pd


dict1={
    "name": ['alice', 'bob', 'charlie', 'david'],
    "marks": [85, 92, 78, 90],
    "city": ['new york', 'los angeles', 'chicago', 'houston']
}


df= pd.DataFrame(dict1)
print(df)

#  if i want to export this data frame to a csv file
df.to_csv('student_data.csv', index=False)

#  give  statistical analyze of data frame - 

print(df.describe())

#  to read a csv file and convert it to data frame
tanya= pd.read_csv('train.csv')
tanya.index=['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth']
print(tanya.head())  #  by default it will print first 5 rows
ser= pd.Series(np.random.rand(34))
print(ser)

newdf= pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
print(newdf)
print(type(newdf))
newdf[0][0]="tanya"
print(newdf.head())
print(newdf.index)

print(newdf.T)

print(newdf.sort_index(axis=1, ascending=False))

print( type(newdf[0]))

print(newdf.describe())

# loc
print(tanya.loc['fifth'])
# iloc
print(tanya.iloc[4])



 # (334, 5)
print(newdf.size)   # 1670
print(newdf.ndim)   # 2
print(newdf.dtypes)
print(newdf.values)
print(newdf.head())
print(newdf.tail())
print(newdf.info())
print(newdf.describe())
print(newdf.mean())
print(newdf.median())
print(newdf.std())










