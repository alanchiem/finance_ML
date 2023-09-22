import bs4 as bs
import datetime as dt 
import os
import pandas as pd 
from pandas_datareader import data as pdr
import pickle 
import requests 
import yfinance as yf
yf.pdr_override()

# Objective: Take the Adj Close of all stocks and combine them into big df with companies as the columns

def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame() # empty df

    for count, ticker in enumerate(tickers[:100]): # only gonna do first 100
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns= {'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.tail())
    main_df.to_csv('sp500_joined_closes.csv')

compile_data()