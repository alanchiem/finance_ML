import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf # This means that whenever you’re using a function from pandas_datareader, yfinance will swoop in and solve it instead. 
yf.pdr_override()

style.use('ggplot') 

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2023, 8, 17)
# df = pdr.DataReader("TSLA", start, end)
# print(df.tail()) 
# df.to_csv('TSLA.csv')

df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
# print(df.head())

# Visualization

df['Adj Close'].plot()
plt.show()

print(df[['Open', 'High']].head())