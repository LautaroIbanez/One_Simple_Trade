"""Base interface for market data providers."""
from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd


class MarketDataProvider(ABC):
    """Abstract base class for market data providers."""

    @abstractmethod
    async def fetch_daily_ohlc(
        self, asset_id: str, vs_currency: str, days: int
    ) -> Tuple[pd.DataFrame, int, int]:
        """
        Fetch daily OHLC data.

        Returns:
            Tuple of (DataFrame with columns: timestamp, open, high, low, close, volume,
                     as_of_utc_ms, latency_ms)
        """
        pass

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider's display name."""
        pass


