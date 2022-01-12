"""Pandas about."""

#1

import pandas as pd

series = pd.Series([10, 20, 30, 40],
                   ['A', 'B', 'C', 'D'])
print(series)
print(series['C'])
print(series[1])

#2 Converting Dictionaries

myDict = {'A':10, 'B':20, 'C':30}

series = pd.Series(myDict, index=['C', 'A', 'B'])
print(series)

#3 Pandas data frame, lake a Excel or db

data = {'Name': ['Anna', 'Bob', 'Charles'],
        'Age': [24, 32, 35],
        'Height': [176, 187, 175]}

df = pd.DataFrame(data)
print(df)
print(df['Name'][1])
print(df[['Name', 'Height']])

#3 Data frame functions

# df.T - Transposes the rows and columns of the data frame.
# df.dtypes - Returns data types of the data frame
# df.ndim - Returns the number of dimensions of the data frame
# df.shape - Returns the shape of the data frame
# df.size - Returns the number of elements in the data fraeme
# df.head(n) - Returns the first n rows of the data frame (default is five)
# df.tail(n) - Returns the last n rows of the data frame (default is five)

#4 Statistical functions
import numpy as np
import pandas as pd

data = {'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona',
                  'Gerald', 'Henry', 'Indra'],
        'Age': [24, 32, 35, 45, 22, 54, 55, 43, 25],
        'Height': [176, 187, 175, 182, 176, 189, 165, 187, 167]}

df  = pd.DataFrame(data)
print(df)
print(df['Age'].mean())
print(df['Height'].median())
print(df.mean())
print(df['Age'].apply(np.sin))
print()
print(df['Age'].apply(lambda x: x*100))
print()

# Lambda

df = df[['Age', 'Height']]
print(df.apply(lambda x: x.max() - x.min())) # oldest/youngest, tallest/tiniest

# count() - Count the number of non-null elements
# sum() - Returns the sum of values of the selected columns
# mean() - Returns the arithmetic mean of values of the selected columns
# median() - Returns the median of values of the selected columns
# model() - Returns the value that occurs most often in the columns selected
# std() - Returns standard deviation of the values
# min() - Returns the minimum value
# max() - Returns the maximum value
# abs() - Returns the absolute values of the elements
# prod() - Returns the product of the selected elements
# describe() - Returns data frame with all statistical values summarized

#5  Iterating

for x in df['Age']:
    print(x)
    
# Statistical functions

# iteritems() - Iterator for key-value pairs
# iterrows() - Iterator for the rows (index, series)
# itertuples() - Iterator for the rows as named tuples

for key, value in df.iteritems():
    print("{}: {}".format(key, value))

for index, value in df.iterrows():
    print(index, value)

#6 Sort by index

df = pd.DataFrame(np.random.rand(10, 2),
        index = [1, 5, 3, 6, 7, 2, 8, 9, 0, 4],
        columns = ['A', 'B'])

print(df.sort_index())

#7 Inplace parameter

df = df.sort_index()
df.sort_index(inplace=True)

#8 Sort by Columns

data = {'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'Industria'],
        'Age': [24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height': [176, 187, 175, 182, 176, 189, 165, 187, 167]}

df = pd.DataFrame(data)
df.sort_values(by=['Age', 'Height'], inplace = True)  # not sort names
print(df)

#9 Joining and Merging

names = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan'],
})
ages = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Age': [20, 30, 40, 50, 60]
})

df = pd.merge(names, ages, on='id')  # merge
df.set_index('id', inplace=True)

print(df)

# Joins

# left - Uses all keys from left object and merges with right
# right - Uses all keys from right object and merges with left
# outer - Uses all keys from both objects and merges them
# inner - Uses only the keys which both objects have and merges them (default)

names = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona'],
})

ages = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 7],
    'Age': [20, 30, 40, 50, 60, 70]
})

heights = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'Height': [123, 433, 432, 332, 53, 222]
})

df1 = pd.merge(names, ages, on='id', how='inner')
df1.set_index('id', inplace=True)
print(df1)

df2 = pd.merge(names, ages, on='id', how='left')  # left joint
df2.set_index('id', inplace=True)
print(df2)

df3 = pd.merge(names, ages, on='id', how='right')  # right joint
df3.set_index('id', inplace=True)
print(df3)

df4 = pd.merge(ages, heights, on='id', how='outer')  # outer joint
df4.set_index('id', inplace=True)
print(df4)

print(df4.loc[df4['Age'] == 20])
print(df4.loc[(df4['Age'] == 40)&(df4['Height']>180)])
print(df3.loc[df3['Age'] > 30]['Name'])

#10 Read data from files

df = pd.read_csv('jill.csv')
df.set_index('id', inplace=True)
print(df)

#11 Save data frame into a csv-file

data = {'Name': ['Anni', 'Bobser', 'Charles', 'Danzel', 'Evaluatus', 'Fifi',
                 'Geraldinio', 'Henry_Morgan', 'Indiana'],
        'Age': [24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height': [176, 187, 175, 182, 176, 189, 165, 176, 156]}

df = pd.DataFrame(data)
df.to_csv('jillian.csv')  # save into file

#12 Plotting data
