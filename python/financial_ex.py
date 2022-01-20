"""Pandas, Numpy and etc for finacial count."""
'''
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

#2 Loading date from files

import pandas as pd

df = pd.read_csv("apple.csv", sep=";")
# df.pd.read_excel("apple.xlsx")
df = pd.read_html("apple.html")
df = pd.read_json("apple.json")

#3 Graphical Visualization

import matplotlib.pyplot as plt
import pandas as pd

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
'''
#4 Comparing Stocks
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas_datareader import data as web
import datetime as dt

style.use('ggplot')

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2021, 1, 1)

apple = web.DataReader('AAPL', 'yahoo', start, end)
facebook = web.DataReader('FB', 'yahoo', start, end)

apple['Adj Close'].plot(label='APPL')
facebook['Adj Close'].plot(label='FB')
plt.ylabel('Adjusted Close')
plt.title('Share Price')
plt.legend(loc='upper left')
plt.show()

# Subplots for more different data

apple = web.DataReader('AAPL', 'yahoo', start, end)
amazon = web.DataReader('AMZN', 'yahoo', start, end)

plt.subplot(211)
apple['Adj Close'].plot(color='blue')
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price')

plt.subplot(212)
amazon['Adj Close'].plot()
plt.ylabel('Adjusted Close')
plt.title('AMZN Share Price')

plt.tight_layout()

plt.show()

# Candlestick charts

from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

apple = apple[['Open', 'High', 'Low', 'Close']]
apple.reset_index(inplace=True)
apple['Date'] = apple['Date'].map(mdates.date2num)  # convert datetime to a number

# Plotting Data

ax = plt.subplot()
candlestick_ohlc(ax, apple.values, width=5, colordown='r', colorup='g')
ax.grid()
ax.xaxis_date()
plt.show()

#5 Plotting Multiple Days
