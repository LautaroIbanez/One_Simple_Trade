"""CoinGecko market data provider implementation."""
import time
from typing import List, Tuple
import httpx
import pandas as pd

from app.core.config import settings
from app.utils.cache import cache
from app.services.providers.base import MarketDataProvider


class CoinGeckoProvider(MarketDataProvider):
    """CoinGecko API provider for BTC market data."""

    @property
    def provider_name(self) -> str:
        return "CoinGecko"

    async def fetch_daily_ohlc(
        self, asset_id: str = "bitcoin", vs_currency: str = "usd", days: int = 730
    ) -> Tuple[pd.DataFrame, int, int]:
        """
        Fetch daily OHLC from CoinGecko Market Chart API.
        Returns DataFrame with columns: timestamp, open, high, low, close, volume
        Also returns as_of_utc (ms) and latency_ms
        """
        cache_key = f"cg_ohlc_{asset_id}_{vs_currency}_{days}"
        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        url = f"{settings.coingecko_base_url}/coins/{asset_id}/market_chart"
        params = {"vs_currency": vs_currency, "days": days, "interval": "daily"}
        started = time.time()
        async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()
        latency_ms = int((time.time() - started) * 1000)

        prices: List[Tuple[int, float]] = data.get("prices", [])
        volumes: List[Tuple[int, float]] = data.get("total_volumes", [])

        # Use close from prices and approximate OHLC as close-only candles
        df = pd.DataFrame(prices, columns=["timestamp", "close"]).sort_values("timestamp")
        vol_df = pd.DataFrame(volumes, columns=["timestamp", "volume"]).sort_values("timestamp")
        df = df.merge(vol_df, on="timestamp", how="left")
        # Synthesize OHL from close using previous close as open, high/low bounds as close
        df["open"] = df["close"].shift(1).fillna(df["close"])
        df["high"] = df[["open", "close"]].max(axis=1)
        df["low"] = df[["open", "close"]].min(axis=1)
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]

        as_of_utc = int(df["timestamp"].iloc[-1])
        result = (df.reset_index(drop=True), as_of_utc, latency_ms)
        cache.set(cache_key, result, settings.cache_ttl_seconds_market)
        return result

