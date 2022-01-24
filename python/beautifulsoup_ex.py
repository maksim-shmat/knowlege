"""Beautifulsoup4 webscrapping examples."""

# ON the Internet, man!

import bs4 as bs
import requests

def load_sp500_tickers():
    link = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(link)

    soup = bs.BeautifulSoup(response.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text[:-1]
        tickers.append(ticker)

    return tickers

# Serializing Tickers
# IT IS IN A NEW FILE MAN!
import pickle

with open("sp500tickers.pickle", 'wb') as f:
    pickle.dump(tickers, f)

# Loading share prices

import os
import datetime as dt
import pandas_datareader as web

def load_prices(reload_tickers=False):
    if reload_tickers:
        tickers=load_sp500_tickers()
    else:
        if os.path.exists('sp500tickers.pickle'):
            with open('sp500tickers.pickle', 'rb') as f:
                tickers = pickle.load(f)

        if not os.path.exists('companies'):
            os.makedirs('companies')

start = dt.datetime(2016, 1, 1)
end = dt.datetime(2019, 1, 1)

for ticker in tickers:
    if not os.path.exists('companies/{}.csv'.format(ticker)):
        print("{} is loading...".format(ticker))
        df = web.DataReader(ticker, 'yahoo', start, end)
        df.to_csv('companies/{}.csv'.format(ticker))
    else:
        print("{} already downloaded!".format(ticker))

# Compiling data
# take the data out in csv files and combine it to one data frame

with open('sp500tickers.pickle', 'rb') as f:
    tickers = pickle.load(f)

main_df = pd.DataFrame()
print("Compiling data...")

for ticker in tickers:
    df = pd.read_csv('companies/{}.csv'.format(ticker))
    df.set_index('Date', inplace=True)

df.rename(columns={'Adj Close': ticker}, inplace=True)
df.drop(['Open', 'High', 'Low', 'Close'], 1, inplace=True)

if main_df.empty:
    main_df = df
else:
    main_df = main_df.join(df, how='outer')

main_df.to_csv('sp500_data.csv')
print("Data compiled!")

# save our main data frame into a new csv file

load_prices(reload_tickers=True)
compile_data()

# Visualizing data

sp500 pd.read_csv('sp500_data.csv')
sp500['MSFT'].plot()
plt.show()

# Correlations with Pandas corr()

correlation = sp500.corr()
print(correlation)

# Visualizing correlations with matplotlib

plt.matshow(correlation)
plt.show()

# Next. Regression Lines

import numpy as np

start = dt.datetime(2016, 1, 1)
end = dt.datetime(2019, 1, 1)

apple = web.DataReader('AAPL', 'yahoo', start, end)
data = apple['Adj Close']

x = data.index.map(mdates.date2num)

fit = np.polyfit(x, data.values, 1)
fit1d = np.poly1w(fit)

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(data.index.fit1d(x), 'r')
plt.show()

# Setting the time frame

rstart = dt.datetime(2018, 7, 1)
rend = dt.datetime(2019, 1, 1)

fit_data = data.reset_index()
post1 = fit_data[fit_data.Date >= rstart].index[0]
post2 = fit_data[fit_data.Date <= rend].index[-1]

fit_data = fit_data.iloc[pos1:pos2]

dates = fit_data.Date.map(mdates.date2num)

fit = np.polyfit(dates, fit_data['Adj Close'], 1)
fit1d = np.poly1d(fit)

plt.gtid()
plt.plot(data.index, data.values, 'b')
plt.plot(fit_data.Date, fit1d(dates), 'r')
plt.show()

# Next. Predicting Share Prices
