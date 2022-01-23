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

