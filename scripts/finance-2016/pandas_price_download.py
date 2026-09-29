"""Download a date range of daily prices into a DataFrame and plot the daily high.

Problem: the first step of any price analysis is getting a clean OHLCV table
into pandas.

Data: public Yahoo Finance prices for GOOG, 2010-01-01 to 2016-09-20, via
``yfinance``. The original tutorial used ``pandas.io.data.DataReader``, which
was removed from pandas years ago.

Adapted from: sentdex, "Data Analysis with Python and Pandas" tutorial series
(pythonprogramming.net), introduction part.

Run: ``python pandas_price_download.py`` (needs internet access).
"""
import datetime

import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib import style

if __name__ == "__main__":
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2016, 9, 20)

    df = yf.Ticker("GOOG").history(start=start, end=end)
    if df.empty:
        raise SystemExit("No price data returned (network or ticker problem).")
    print(df)

    style.use('fivethirtyeight')

    df['High'].plot()
    plt.title('GOOG daily high, 2010-2016')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    if plt.get_backend().lower() == "agg":
        plt.savefig('GOOG_high.png', dpi=100, bbox_inches='tight')
    else:
        plt.show()
