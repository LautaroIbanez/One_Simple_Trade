# One Simple Trade - Backend (FastAPI)

This service fetches daily BTC market data, computes indicators (EMA20/EMA50, RSI14, MACD 12/26/9, ATR14, 30d volatility) and produces a daily BUY/HOLD/SELL recommendation with confidence and explanation.

## Prerequisites

- Python 3.11 or 3.12
- Poetry (install: `curl -sSL https://install.python-poetry.org | python3 -`)

## Install

```bash
poetry install
```

## Run

```bash
# With Poetry shell
poetry shell
uvicorn app.main:app --reload --port 8000

# Or directly
poetry run uvicorn app.main:app --reload --port 8000
```

## Endpoints
- GET `/health` — status and timestamp
- GET `/v1/market/ohlc` — BTC daily candles with indicators, includes source, latency_ms, as_of_utc
- GET `/v1/signal` — BUY/HOLD/SELL with confidence, explanation, model_version, timestamps, disclaimer, methodology link

## Testing

```bash
poetry run pytest -q --maxfail=1 --disable-warnings
poetry run ruff check .
poetry run mypy app
```

## Data Providers

The backend uses a pluggable provider pattern. Default: **CoinGecko**.

- `MarketDataProvider` (ABC): Base interface
- `CoinGeckoProvider`: Current implementation
- To add another provider: implement `MarketDataProvider` and configure in `MarketDataService`

All responses include `as_of_utc` (ms) and `latency_ms` computed per request.

## Disclaimer
Educational use only. Not financial advice. Signals are model outputs and not guaranteed.


