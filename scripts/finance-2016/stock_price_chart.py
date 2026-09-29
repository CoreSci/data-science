"""Plot 10 years of a stock's closing price with a customised date axis.

Problem: fetch historical prices from the internet and render a readable time
series: rotated date labels, grid, and tuned margins.

How it works: download the daily history, unpack date and OHLCV columns, and
draw the close on a single subplot.

Data: public Yahoo Finance prices via ``yfinance``. The original tutorial read
Yahoo's ``chartapi`` CSV endpoint, which Yahoo retired in 2017, and its date
converter used ``matplotlib.dates.strpdate2num``, which was removed in
Matplotlib 3.3. Both are replaced here without changing the chart.

Adapted from: sentdex, "Matplotlib tutorial series" (pythonprogramming.net),
"getting data from the internet" and customisation parts.

Run: ``python stock_price_chart.py [TICKER]`` (default GOOG; needs internet access).
"""
from __future__ import annotations

import sys

import matplotlib.pyplot as plt
import yfinance as yf


def graph_data(stock: str) -> None:
    """Download ~10 years of daily prices for ``stock`` and plot the close."""
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    history = yf.Ticker(stock).history(period="10y")
    if history.empty:
        raise SystemExit(f"No price data returned for {stock!r} (network or ticker problem).")
    date = history.index
    closep, highp, lowp, openp, volume = (history[c].to_numpy() for c in ("Close", "High", "Low", "Open", "Volume"))

    ax1.plot(date, closep, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{stock}: daily close, last 10 years')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    if plt.get_backend().lower() == "agg":
        fig.savefig(f"{stock}_close.png", dpi=100)
        print(f"saved {stock}_close.png ({len(history)} rows)")
    else:
        plt.show()


if __name__ == "__main__":
    graph_data(sys.argv[1] if len(sys.argv) > 1 else 'GOOG')
