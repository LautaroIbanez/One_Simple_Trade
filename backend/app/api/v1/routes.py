import time
from fastapi import APIRouter
from app.services.market_data import MarketDataService
from app.services.indicators import compute_indicators
from app.services.signal import decide_signal
from app.models.schemas import MarketOhlcResponse, IndicatorPoint, SignalResponse
from app.core.config import settings


router = APIRouter()


@router.get("/market/ohlc", response_model=MarketOhlcResponse)
async def get_market_ohlc() -> MarketOhlcResponse:
    df, as_of_utc, latency_ms = await MarketDataService.fetch_daily_ohlc()
    ind = compute_indicators(df)
    candles = [
        IndicatorPoint(
            timestamp=int(row.timestamp),
            close=float(row.close),
            ema_fast=float(row.ema_fast) if row.ema_fast == row.ema_fast else None,
            ema_slow=float(row.ema_slow) if row.ema_slow == row.ema_slow else None,
            rsi=float(row.rsi) if row.rsi == row.rsi else None,
            macd=float(row.macd) if row.macd == row.macd else None,
            macd_signal=float(row.macd_signal) if row.macd_signal == row.macd_signal else None,
            atr=float(row.atr) if row.atr == row.atr else None,
            vol_30d=float(row.vol_30d) if row.vol_30d == row.vol_30d else None,
        )
        for row in ind.itertuples(index=False)
    ]
    return MarketOhlcResponse(
        asset="BTC",
        quote="USD",
        timeframe="1d",
        source="CoinGecko",
        latency_ms=latency_ms,
        as_of_utc=as_of_utc,
        candles=candles,
    )


@router.get("/signal", response_model=SignalResponse)
async def get_signal() -> SignalResponse:
    df, as_of_utc, latency_ms = await MarketDataService.fetch_daily_ohlc()
    ind = compute_indicators(df)
    latest = ind.iloc[-1]
    signal, confidence, explanation = decide_signal(latest)

    def _nn(x):
        return float(x) if x == x else None  # convert NaN to None

    indicators_snapshot = IndicatorPoint(
        timestamp=int(latest.timestamp),
        close=_nn(latest.close) or 0.0,
        ema_fast=_nn(latest.ema_fast),
        ema_slow=_nn(latest.ema_slow),
        rsi=_nn(latest.rsi),
        macd=_nn(latest.macd),
        macd_signal=_nn(latest.macd_signal),
        atr=_nn(latest.atr),
        vol_30d=_nn(latest.vol_30d),
    )

    disclaimer = (
        "Educational use only. Not financial advice. No execution or exchange connectivity."
    )
    methodology_url = "https://example.com/docs/methodology"  # updated in docs

    return SignalResponse(
        asset="BTC",
        quote="USD",
        timeframe="1d",
        signal=signal,
        confidence=round(confidence, 3),
        explanation=explanation,
        model_version=settings.model_version,
        as_of_utc=as_of_utc,
        latency_ms=latency_ms,
        indicators_snapshot=indicators_snapshot,
        disclaimer=disclaimer,
        methodology_url=methodology_url,
    )


