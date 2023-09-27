from collections import Counter
import numpy as np 
import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier


def process_data_for_labels(ticker):
    hm_days = 7 # how many days in the future
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
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

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                                df['{}_1d'.format(ticker)],
                                                df['{}_2d'.format(ticker)],
                                                df['{}_3d'.format(ticker)],
                                                df['{}_4d'.format(ticker)],
                                                df['{}_5d'.format(ticker)], 
                                                df['{}_6d'.format(ticker)],
                                                df['{}_7d'.format(ticker)],
                                                ))

    vals = df['{}_target'.format(ticker)].values
    str_vals = [str(i) for i in vals]
    print('Data Spread: ', Counter(str_vals)) # gives us the distribution of buy sell hold
    df.fillna(0, inplace=True)

    df = df.replace([np.inf, -np.inf], np.nan) # ex. % change from 0 to something is inf
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change() # % change from previous day
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    # Feature Sets and Target
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df

def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    #clf = neighbors.KNeighborsClassifier()

    # We can use 3 classifiers at the same time
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('nn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)

    predictions = clf.predict(X_test)
    print('Accuracy: ', confidence)
    print('Predicted spread: ', Counter(predictions))

do_ml('AAPL')

