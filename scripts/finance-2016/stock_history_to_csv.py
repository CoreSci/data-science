"""Save a ticker's daily price history to CSV for offline modelling.

Problem: keep a local, model-ready price file (unix date, close, high, low,
open, volume) so experiments don't re-download data on every run.

How it works: download 10 years of daily prices and write a header row plus
one row per day to ``stock_model.csv``, appending if the file already exists.

Data: public Yahoo Finance prices (default ``SOXX``) via ``yfinance``. The
original version parsed Yahoo's ``chartapi`` CSV endpoint, which has since been retired.

Adapted from: extends the data-download step of sentdex's "Matplotlib
tutorial series" (pythonprogramming.net) into a CSV exporter.

Run: ``python stock_history_to_csv.py [TICKER] [PERIOD]``, e.g. ``SOXX 10y``
(``PERIOD`` is one of 1d, 1y, 5y, 10y, max). Needs internet access.
"""
from __future__ import annotations

import sys

import yfinance as yf


def append_csv_row(file: str, row: tuple) -> None:
    """Append one comma-separated row to ``file``."""
    with open(file, 'a') as write_file:
        write_file.write(','.join(str(v) for v in row) + "\n")


if __name__ == "__main__":
    stock = sys.argv[1] if len(sys.argv) > 1 else "SOXX"
    period = sys.argv[2] if len(sys.argv) > 2 else "10y"

    history = yf.Ticker(stock).history(period=period)
    if history.empty:
        raise SystemExit(f"No price data returned for {stock!r} (network or ticker problem).")

    header = "date", "closep", "highp", "lowp", "openp", "volume"
    append_csv_row("stock_model.csv", header)

    stock_data = []
    for ts, bar in history.iterrows():
        stock_tuple = (int(ts.timestamp()), bar["Close"], bar["High"], bar["Low"], bar["Open"], bar["Volume"])
        stock_data.append(stock_tuple)
        append_csv_row("stock_model.csv", stock_tuple)
    print(f"wrote {len(stock_data)} rows for {stock} to stock_model.csv")
