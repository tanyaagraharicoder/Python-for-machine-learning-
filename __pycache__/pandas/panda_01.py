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





