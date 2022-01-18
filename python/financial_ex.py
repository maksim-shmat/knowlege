"""Pandas, Numpy and etc for finacial count."""

#1 Loading financial data

from pandas_datareader import data as web  # download info from web
import datetime as dt

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 1, 1)  # or end = dt.datetime.now()

df = web.DataReader('AAPL', 'yahoo', start, end)  # for Apple from yahoo

print(df['Close'])
print(df['Close']['2020-02-14'])
print(df['Close'][5])

# Saving and loading data
# CSV

df.to_csv('apple.csv')
df.to_csv('apple.csv', sep=';')

# Excel

#df.to_excel('apple.xlsx')  # Nope, no module openpy excel
# and for .ods?

# HTML

df.to_html('apple.html')

# JSON

df.to_json('apple.json')

# Loading date from files

import pandas as pd

df = pd.read_csv("apple.csv", sep=";")
# df.pd.read_excel("apple.xlsx")
df = pd.read_html("apple.html")
df = pd.read_json("apple.json")

# Graphical Visualization

import matplotlib.pyplot as plt

# Plotting Diagrams

df['Adj Close'].plot()
plt.show()

# Plotting style

from matplotlib import style

style.use('ggplot')
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price')
df['Adj Close'].plot()
plt.show()

# Comparing Stocks
