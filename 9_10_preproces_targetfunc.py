import numpy as np 
import pandas as pd 
import pickle

def process_data_for_labels(ticker):
    hm_days = 7 # how many days in the future
    df = pd.read_csv('sp500_joined_closed.csv', index_col=0)
    tickers = df.columns.values
    df.fillna(0, inplace=True)

    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
    
    df.fillna(0, inplace=True)

    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02 # if stock changes by 2% within 7 days
    for col in cols:
        if col > requirement:
            return 1 # we should buy
        if col < -requirement:
            return -1 # sell
    return 0 # hold
