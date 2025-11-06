from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "One Simple Trade - Backend"
    model_version: str = os.environ.get("MODEL_VERSION", "1.0.0")
    coingecko_base_url: str = "https://api.coingecko.com/api/v3"
    # Cache TTLs in seconds
    cache_ttl_seconds_market: int = int(os.environ.get("CACHE_TTL_MARKET", "300"))
    request_timeout_seconds: int = int(os.environ.get("REQUEST_TIMEOUT", "20"))


settings = Settings()



