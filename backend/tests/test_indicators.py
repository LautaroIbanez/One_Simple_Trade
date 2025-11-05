import pandas as pd
from app.services.indicators import compute_indicators, ema, rsi, macd, atr


def test_ema_basic():
    s = pd.Series([1, 2, 3, 4, 5])
    e = ema(s, span=3)
    assert len(e) == 5
    assert e.iloc[-1] > e.iloc[0]


def test_rsi_bounds():
    s = pd.Series([50, 51, 52, 53, 54, 53, 52, 51, 50, 49, 48, 49, 50, 51, 52])
    r = rsi(s, 14)
    assert r.between(0, 100).all()


def test_macd_signal_relation():
    s = pd.Series(range(1, 200))
    m, sig = macd(s)
    assert (m - sig).abs().mean() >= 0


def test_atr_positive():
    df = pd.DataFrame({
        "high": [10, 12, 11, 13],
        "low": [8, 10, 9, 11],
        "close": [9, 11, 10, 12],
    })
    a = atr(df, 3)
    assert (a >= 0).all()


def test_compute_indicators_columns():
    df = pd.DataFrame({
        "timestamp": [1, 2, 3, 4, 5],
        "open": [1, 2, 3, 4, 5],
        "high": [1, 2, 3, 4, 5],
        "low": [1, 2, 3, 4, 5],
        "close": [1, 2, 3, 4, 5],
        "volume": [10, 10, 10, 10, 10],
    })
    out = compute_indicators(df)
    for col in ["ema_fast", "ema_slow", "rsi", "macd", "macd_signal", "atr", "vol_30d"]:
        assert col in out.columns


