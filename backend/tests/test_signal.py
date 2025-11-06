import pandas as pd
from app.services.signal import decide_signal


def test_decide_signal_outputs():
    row = pd.Series({
        "ema_fast": 110,
        "ema_slow": 100,
        "macd": 1.5,
        "macd_signal": 1.0,
        "rsi": 55,
        "atr": 2,
        "close": 100,
        "vol_30d": 0.5,
    })
    signal, confidence, explanation = decide_signal(row)
    assert signal in {"BUY", "HOLD", "SELL"}
    assert 0.0 <= confidence <= 1.0
    assert isinstance(explanation, str) and len(explanation) > 0



