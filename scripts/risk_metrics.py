"""Basic risk/return metrics for periodic return series.

A small, dependency-light module (numpy + pandas) used by the
``notebooks/finance-capitalstream`` notebooks. It provides annualised
return, annualised volatility, Sharpe ratio and maximum drawdown for one or
more return series.

Conventions
-----------
* ``returns`` are simple periodic returns, e.g. ``prices.pct_change()``.
* NaN and +/-inf values (the first row of ``pct_change``, divisions by zero
  in volume-type columns) are dropped per column before any calculation.
* The risk-free rate is an *annual* rate. It is converted to a per-period rate
  by geometric de-compounding: ``(1 + rf) ** (1 / periods_per_year) - 1``.

Example
-------
>>> import pandas as pd
>>> r = pd.Series([0.01, -0.02, 0.015, 0.005])
>>> round(max_drawdown(r), 4)
-0.02
"""
from __future__ import annotations

import numpy as np
import pandas as pd

__all__ = ["annualized_return", "annualized_volatility", "sharpe_ratio", "max_drawdown", "summary_stats"]


def _clean(returns: pd.Series) -> pd.Series:
    """Drop NaN/inf values and cast to float."""
    r = pd.to_numeric(returns, errors="coerce").astype(float)
    return r.replace([np.inf, -np.inf], np.nan).dropna()


def annualized_return(returns: pd.Series, periods_per_year: int) -> float:
    """Compound annual growth rate implied by the periodic returns."""
    r = _clean(returns)
    if r.empty:
        return float("nan")
    growth = float(np.prod(1.0 + r.to_numpy()))
    if growth <= 0:  # the series lost 100% or more at some point
        return -1.0
    return growth ** (periods_per_year / len(r)) - 1.0


def annualized_volatility(returns: pd.Series, periods_per_year: int) -> float:
    """Sample standard deviation of the returns, scaled by sqrt(periods_per_year)."""
    r = _clean(returns)
    if len(r) < 2:
        return float("nan")
    return float(r.std(ddof=1) * np.sqrt(periods_per_year))


def sharpe_ratio(returns: pd.Series, riskfree_rate: float, periods_per_year: int) -> float:
    """Annualised excess return over the risk-free rate, per unit of annualised volatility."""
    r = _clean(returns)
    rf_per_period = (1.0 + riskfree_rate) ** (1.0 / periods_per_year) - 1.0
    excess = r - rf_per_period
    vol = annualized_volatility(r, periods_per_year)
    if not np.isfinite(vol) or vol < 1e-12:  # constant series: std is float noise, not risk
        return float("nan")
    return annualized_return(excess, periods_per_year) / vol


def max_drawdown(returns: pd.Series) -> float:
    """Worst peak-to-trough decline of the compounded wealth path (a negative fraction)."""
    r = _clean(returns)
    if r.empty:
        return float("nan")
    wealth = (1.0 + r).cumprod()
    running_peak = np.maximum(wealth.cummax(), 1.0)  # start from an initial wealth of 1.0
    return float((wealth / running_peak - 1.0).min())


def summary_stats(returns: pd.DataFrame | pd.Series, riskfree_rate: float = 0.03,
                  periods_per_year: int = 252) -> pd.DataFrame:
    """One row of metrics per return series (one per column when given a DataFrame).

    Non-numeric columns are ignored. Columns with fewer than two usable
    observations get NaN metrics instead of raising an error.
    """
    frame = returns.to_frame() if isinstance(returns, pd.Series) else returns
    frame = frame.select_dtypes(include="number")
    rows = {}
    for col in frame.columns:
        r = frame[col]
        rows[col] = {
            "Annualized Return": annualized_return(r, periods_per_year),
            "Annualized Volatility": annualized_volatility(r, periods_per_year),
            "Sharpe Ratio": sharpe_ratio(r, riskfree_rate, periods_per_year),
            "Max Drawdown": max_drawdown(r),
        }
    return pd.DataFrame.from_dict(rows, orient="index")
