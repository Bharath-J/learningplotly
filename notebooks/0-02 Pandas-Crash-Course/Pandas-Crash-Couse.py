import numpy as np
import pandas as pd

df = pd.read_csv('salaries.csv')
print(df[['Name','Salary']])

print(df['Salary'].min())
print(df['Salary'].mean())

#Filtering
ser_of_bool = df['Age']>30
print(ser_of_bool)
print(df[ser_of_bool])

#Unique
print(df['Age'].unique())

#nunique
print(df['Age'].nunique())

#column names
print(df.columns)

#info --> reports how many entries, columns etc
print(df.info())

#describe --> reports stat summary
print(df.describe())

mat = np.arange(0,10).reshape(5,2)
print(mat)

df2 = pd.DataFrame(data=mat, columns=['A', 'B'])
print(df2)
