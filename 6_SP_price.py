import bs4 as bs
import datetime as dt 
import os # to create new directories
import pandas as pd 
from pandas_datareader import data as pdr
import pickle 
import requests 
import yfinance as yf
yf.pdr_override()

def save_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    # right-click and view source
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    # we dont want to include the header row
    for row in table.findAll('tr')[1:]: 
        # we want 1st col (ticker), 2nd col would be (company name)
        ticker = row.findAll('td')[0].text.strip()  # strip removes the white space
        tickers.append(ticker)
    # write bytes
    with open("sp500tickers.pickle", "wb") as f: 
        pickle.dump(tickers, f)
    # print(tickers)
    return tickers

def get_data_from_yahoo(reload_sp500=False): 
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f: # read bytes
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2022, 12, 31)

    # grab only the first 100 instead of 500
    for ticker in tickers[:100]:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = pdr.get_data_yahoo(ticker, start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()