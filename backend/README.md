# One Simple Trade - Backend (FastAPI)

This service fetches daily BTC market data, computes indicators (EMA20/EMA50, RSI14, MACD 12/26/9, ATR14, 30d volatility) and produces a daily BUY/HOLD/SELL recommendation with confidence and explanation.

## Install

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload --port 8000 --app-dir backend
```

## Endpoints
- GET `/health` — status and timestamp
- GET `/v1/market/ohlc` — BTC daily candles with indicators, includes source, latency_ms, as_of_utc
- GET `/v1/signal` — BUY/HOLD/SELL with confidence, explanation, model_version, timestamps, disclaimer, methodology link

## Testing

```bash
pytest -q --maxfail=1 --disable-warnings backend
```

## Data Source
- CoinGecko Market Chart (`https://api.coingecko.com/api/v3/coins/bitcoin/market_chart`)

All responses include `as_of_utc` (ms) and `latency_ms` computed per request.

## Disclaimer
Educational use only. Not financial advice. Signals are model outputs and not guaranteed.


