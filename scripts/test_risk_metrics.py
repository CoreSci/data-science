"""Unit tests for risk_metrics.py, checked against hand-computable cases.

Run: ``python -m pytest data-science/scripts/test_risk_metrics.py``
"""
import math

import numpy as np
import pandas as pd
import pytest

import risk_metrics as rm


def test_annualized_return_constant_growth():
    # 1% per period for 12 periods per year -> (1.01**12 - 1) per year
    r = pd.Series([0.01] * 24)
    assert rm.annualized_return(r, 12) == pytest.approx(1.01 ** 12 - 1)


def test_volatility_scales_with_sqrt_time():
    r = pd.Series([0.01, -0.01] * 50)
    assert rm.annualized_volatility(r, 252) == pytest.approx(r.std(ddof=1) * math.sqrt(252))


def test_zero_volatility_gives_nan_sharpe():
    assert math.isnan(rm.sharpe_ratio(pd.Series([0.01] * 10), 0.03, 252))


def test_sharpe_positive_for_returns_above_riskfree():
    rng = np.random.default_rng(0)
    r = pd.Series(rng.normal(0.001, 0.01, 1000))
    assert rm.sharpe_ratio(r, 0.0, 252) > 0


def test_max_drawdown_known_path():
    # wealth: 1.1, 0.88, 0.968 -> peak 1.1, trough 0.88 -> -20%
    r = pd.Series([0.10, -0.20, 0.10])
    assert rm.max_drawdown(r) == pytest.approx(-0.20)


def test_drawdown_counts_initial_capital():
    # first period already loses 10% of the starting capital
    assert rm.max_drawdown(pd.Series([-0.10, 0.05])) == pytest.approx(-0.10)


def test_summary_stats_handles_nan_inf_and_non_numeric():
    df = pd.DataFrame({
        "Close": [np.nan, 0.01, -0.02, 0.03],
        "Volume": [np.nan, np.inf, 0.5, -0.2],
        "Label": ["a", "b", "c", "d"],
    })
    out = rm.summary_stats(df, riskfree_rate=0.03, periods_per_year=252)
    assert list(out.index) == ["Close", "Volume"]
    assert list(out.columns) == ["Annualized Return", "Annualized Volatility", "Sharpe Ratio", "Max Drawdown"]
    assert out.notna().all().all()


def test_summary_stats_accepts_series():
    out = rm.summary_stats(pd.Series([0.01, 0.02, -0.01], name="x"))
    assert list(out.index) == ["x"]
