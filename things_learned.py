''' 
Sep 19, 2023

When installing pandas-reader, it had a time out error.
Use the following to fix:
    sudo pip3 install --default-timeout=100 pandas-reader

From a youtube comment by eugenefdscodes
https://www.youtube.com/watch?v=2BrpKpWwT2A&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ
python3.10 -m pip install yfinance

Use can use df.tail() to get the last items

Sep 20, 2023

Since matplotlib.finance has been deprecated
python3.10 -m pip install mplfinance 

You can do this to access old mplfinance 
from mplfinance.original_flavor import candlestick_ohlc 
BUT
mplfinance.plot() # defaults to ohlc




'''