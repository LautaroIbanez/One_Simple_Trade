import time
import pandas as pd


def _score_from_indicators(row: pd.Series) -> tuple[float, list[str]]:
    explanations: list[str] = []
    score = 0.0

    # Trend: EMA fast vs slow
    if row["ema_fast"] > row["ema_slow"]:
        score += 0.4
        explanations.append("Uptrend: EMA20 above EMA50")
    elif row["ema_fast"] < row["ema_slow"]:
        score -= 0.4
        explanations.append("Downtrend: EMA20 below EMA50")

    # Momentum: MACD vs signal
    if row["macd"] > row["macd_signal"]:
        score += 0.3
        explanations.append("Positive momentum: MACD above signal")
    elif row["macd"] < row["macd_signal"]:
        score -= 0.3
        explanations.append("Negative momentum: MACD below signal")

    # RSI: avoid extremes
    if 45 <= row["rsi"] <= 60:
        score += 0.15
        explanations.append("RSI neutral-positive (45-60)")
    elif row["rsi"] < 35:
        score -= 0.15
        explanations.append("RSI oversold risk (<35)")
    elif row["rsi"] > 70:
        score -= 0.2
        explanations.append("RSI overbought risk (>70)")

    # Risk adjustment: higher ATR and volatility reduce confidence
    risk_penalty = 0.0
    if pd.notna(row.get("vol_30d")) and row["vol_30d"] > 0:
        risk_penalty += min(row["vol_30d"] / 1.0, 0.3)  # cap
    if pd.notna(row.get("atr")) and row["atr"] > 0:
        risk_penalty += min(row["atr"] / max(row["close"], 1e-6), 0.3)
    score -= risk_penalty * 0.5  # reduce signal magnitude
    if risk_penalty > 0:
        explanations.append("Volatility adjustment applied")

    return score, explanations


def decide_signal(latest_row: pd.Series) -> tuple[str, float, str]:
    score, reasons = _score_from_indicators(latest_row)

    if score >= 0.25:
        signal = "BUY"
    elif score <= -0.25:
        signal = "SELL"
    else:
        signal = "HOLD"

    # Confidence is the absolute score scaled to [0,1]
    confidence = float(max(0.0, min(1.0, abs(score))))
    explanation = "; ".join(reasons) or "Mixed signals"
    return signal, confidence, explanation



