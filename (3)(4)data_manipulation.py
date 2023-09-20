import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style  
import matplotlib.dates as mdates 
import pandas as pd 
import pandas_datareader as pdr
import yfinance as yf
yf.pdr_override()
style.use('ggplot')

import mplfinance as mpf
df= pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)
print(df.head())

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_ohlc['volume'] = df['Volume'].resample('10D').sum()

print(df_ohlc.head())

mpf.plot(df_ohlc, type='candle', style='charles',
            title='TSLA 10D Resample',
            ylabel='Price ($)',
            ylabel_lower='Volume',
            figratio=(25,10),
            figscale=1,
            mav=50,
            volume=True
            )

plt.show()


# from mplfinance.original_flavor import candlestick_ohlc 
# import mplfinance
# 100 moving average: the average of the past 100 days
# min_periods allows the first 99 days to be included, since they don't have previous days to calculate with
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# print(df.head())

# Resample Data into 10-day data
# open high low close: 
# df_ohlc = df['Adj Close'].resample('10D').ohlc()
# df_vol = df['Volume'].resample('10D').sum()

# print(df_ohlc.head())

# reset df_ohlc so date is a column
# df_ohlc.reset_index(inplace=True)
# print(df_ohlc.head())

# convert date to mdates
# df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
# print(df_ohlc.head())


# Graphing with pure matplotlib NOT matplotlib + pandas
# Subplots are referred to as axis
# Grid size: a 6x1, 6 rows 1 col
# ax1 = plt.subplot2grid((6, 1), (0,0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6, 1), (5,0), rowspan=1, colspan=1, sharex=ax1) # sharex will make the axis zoom together

# candlestick wants date, open, high, low, close
# candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')


# X is the date, Y is the volume, fills between those two and starts from 0
# ax2.fill_between(df_vol.index.map(mdates.date2num), df_vol.values, 0)


# index is the date
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

