import asyncio
from typing import Tuple

import pandas as pd

from app.services.market_data import MarketDataService
from app.services.providers.base import MarketDataProvider


class StubProvider(MarketDataProvider):
    @property
    def provider_name(self) -> str:
        return "StubProvider"

    async def fetch_daily_ohlc(
        self, asset_id: str, vs_currency: str, days: int
    ) -> Tuple[pd.DataFrame, int, int]:
        # Minimal deterministic frame to validate wiring
        df = pd.DataFrame(
            {
                "timestamp": [1_000, 2_000],
                "open": [10.0, 11.0],
                "high": [10.5, 11.5],
                "low": [9.5, 10.5],
                "close": [10.2, 11.2],
                "volume": [1000.0, 1100.0],
            }
        )
        return df, 2_000, 0


def test_market_data_service_accepts_custom_provider():
    service = MarketDataService(provider=StubProvider())
    assert service.provider_name == "StubProvider"

    df, as_of_utc, latency_ms = asyncio.get_event_loop().run_until_complete(
        service.fetch_daily_ohlc(asset_id="bitcoin", vs_currency="usd", days=2)
    )

    assert list(df.columns) == [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]
    assert len(df) == 2
    assert as_of_utc == 2_000
    assert latency_ms == 0


