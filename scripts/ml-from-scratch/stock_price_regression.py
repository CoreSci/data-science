"""Forecast a stock's adjusted close ~1% of the history ahead with regression models.

Problem: can simple engineered features (daily high-low range %, open-to-close
change %, volume) plus today's price predict the price a few weeks out?

How it works: build the features, shift the target back by ``forecast_out``
rows (1% of the history), scale, hold out 20%, then compare the R^2 of a
linear regression with support-vector regressors using linear, poly, rbf and
sigmoid kernels.

Data: public daily prices for GOOGL from Yahoo Finance (``yfinance``, split and
dividend adjusted). The original tutorial used Quandl's ``WIKI/GOOGL`` dataset,
which has since been discontinued.

Adapted from: sentdex, "Practical Machine Learning with Python" tutorial series
(pythonprogramming.net), regression parts.

Run: ``python stock_price_regression.py`` (needs internet access for yfinance).
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  # was sklearn.cross_validation (removed)


def load_prices(ticker: str = "GOOGL") -> pd.DataFrame:
    """Adjusted OHLCV history, with columns named as in the original WIKI dataset."""
    raw = yf.Ticker(ticker).history(period="max", auto_adjust=True)
    if raw.empty:
        raise SystemExit(f"No price data returned for {ticker!r} (network or ticker problem).")
    return raw.rename(columns={"Open": "Adj. Open", "High": "Adj. High", "Low": "Adj. Low",
                               "Close": "Adj. Close", "Volume": "Adj. Volume"})


if __name__ == "__main__":
    df = load_prices()
    print(df.head())

    df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

    df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
    print(df.head())

    forecast_col = 'Adj. Close'
    df.fillna(value=-99999, inplace=True)          # treat gaps as outliers rather than dropping rows
    forecast_out = int(math.ceil(0.01 * len(df)))  # predict 1% of the history ahead

    df['label'] = df[forecast_col].shift(-forecast_out)
    df.dropna(inplace=True)

    X = np.array(df.drop(['label'], axis=1))       # axis must be a keyword in pandas >= 2
    y = np.array(df['label'])
    X = preprocessing.scale(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print(f"forecast horizon: {forecast_out} trading days")
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)
    print("linear regression R^2:", round(clf.score(X_test, y_test), 4))

    for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        clf = svm.SVR(kernel=k)
        clf.fit(X_train, y_train)
        confidence = clf.score(X_test, y_test)
        print(f"SVR ({k}) R^2:", round(confidence, 4))
