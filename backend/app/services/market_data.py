"""Market data service with pluggable providers."""
from app.core.config import settings
from app.services.providers.coingecko import CoinGeckoProvider
from app.services.providers.base import MarketDataProvider


class MarketDataService:
    """Service for fetching market data using pluggable providers."""

    def __init__(self, provider: MarketDataProvider | None = None):
        """Initialize with a provider (defaults to CoinGecko)."""
        self.provider = provider or CoinGeckoProvider()

    async def fetch_daily_ohlc(
        self, asset_id: str = "bitcoin", vs_currency: str = "usd", days: int = 730
    ):
        """Fetch daily OHLC data using the configured provider."""
        return await self.provider.fetch_daily_ohlc(asset_id, vs_currency, days)

    @property
    def provider_name(self) -> str:
        """Return the current provider's name."""
        return self.provider.provider_name


# Global service instance (default provider: CoinGecko)
_service = MarketDataService()


