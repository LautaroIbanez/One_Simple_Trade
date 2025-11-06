from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class HealthResponse(BaseModel):
    status: str
    timestamp: int


class IndicatorPoint(BaseModel):
    timestamp: int
    close: float
    ema_fast: Optional[float] = None
    ema_slow: Optional[float] = None
    rsi: Optional[float] = None
    macd: Optional[float] = None
    macd_signal: Optional[float] = None
    atr: Optional[float] = None
    vol_30d: Optional[float] = None


class MarketOhlcResponse(BaseModel):
    asset: str = Field(examples=["BTC"])
    quote: str = Field(examples=["USD"])
    timeframe: str = Field(examples=["1d"])
    source: str
    latency_ms: int
    as_of_utc: int
    candles: List[IndicatorPoint]


class SignalResponse(BaseModel):
    asset: str
    quote: str
    timeframe: str
    signal: Literal["BUY", "HOLD", "SELL"]
    confidence: float
    explanation: str
    model_version: str
    as_of_utc: int
    latency_ms: int
    indicators_snapshot: IndicatorPoint
    disclaimer: str
    methodology_url: str



