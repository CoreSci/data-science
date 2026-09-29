"""Fetch the Freddie Mac house price index for Texas from Quandl / Nasdaq Data Link.

Problem: pull a public economic time series into pandas with one API call.

Credentials: supplied by you. Set ``NASDAQ_DATA_LINK_API_KEY`` (template in
``data-science/notebooks/finance-capitalstream/.env.example``). The key is read
from the environment and is never printed or stored.

Adapted from: sentdex, "Data Analysis with Python and Pandas" tutorial series
(pythonprogramming.net), Quandl part.

Note: the ``FMAC/HPI_*`` datasets may no longer be offered on Nasdaq Data Link.
The script exits with a clear message if the request fails.

Run: ``python quandl_housing_index.py`` (``pip install quandl``).
"""
import os

import quandl

if __name__ == "__main__":
    api_key = os.environ.get("NASDAQ_DATA_LINK_API_KEY")
    if not api_key:
        raise SystemExit("Set NASDAQ_DATA_LINK_API_KEY first (see .env.example).")

    try:
        df = quandl.get("FMAC/HPI_TX", authtoken=api_key)
    except Exception as exc:  # network, auth or discontinued dataset
        raise SystemExit(f"Quandl request failed: {exc}")

    print(df.head())
