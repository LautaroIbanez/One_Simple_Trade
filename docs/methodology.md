# One Simple Trade — Methodology

Version: 1.0.0

## Data
- Source: CoinGecko Market Chart (daily). Endpoint: `https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=730&interval=daily`
- Fields: close (used), volume. Open/High/Low are synthesized from close to maintain simple consistency. Timestamps are milliseconds UTC.
- Latency measured per request.

## Indicators
- EMA fast/slow: EMA(20), EMA(50)
- RSI: Wilder’s RSI(14)
- MACD: (12,26) with signal 9
- ATR: 14 (using synthesized OHLC); used as risk proxy
- 30d annualized volatility: std(returns, 30) * sqrt(365)

## Signal Rules
We compute a score in [-inf, inf] and map to BUY/HOLD/SELL.
- Trend: +0.4 if EMA20 > EMA50, -0.4 if EMA20 < EMA50
- Momentum: +0.3 if MACD > Signal, -0.3 if MACD < Signal
- RSI band: +0.15 if 45 ≤ RSI ≤ 60; -0.15 if RSI < 35; -0.2 if RSI > 70
- Risk adjustment: subtract 0.5 * (min(vol_30d/1.0, 0.3) + min(ATR/close, 0.3))

Decision:
- BUY if score ≥ 0.25
- SELL if score ≤ -0.25
- otherwise HOLD

Confidence: |score| clipped to [0,1].

## Assumptions and Limitations
- Close-only market data from CoinGecko; OHLC synthesized for ATR. This simplifies but can under/overestimate intraday ranges.
- Daily timeframe; no intraday signals.
- No transaction costs/slippage modeled in the live signal. Backtests will include simple fee assumption.
- Model is heuristic, not optimized by ML; easy to audit.

## Disclaimers
- Educational use only. Not investment advice. Past performance is not indicative of future results.
- We do not execute trades or connect to exchanges.


