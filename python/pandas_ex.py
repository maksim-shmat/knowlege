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

#5 
