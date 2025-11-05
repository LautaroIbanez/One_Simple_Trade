import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert isinstance(data["timestamp"], int)


@pytest.mark.asyncio
async def test_signal_endpoint_smoke(monkeypatch):
    # Avoid hitting external API by stubbing market data service
    import pandas as pd
    from app.services.market_data import _service

    async def fake_fetch(*args, **kwargs):
        df = pd.DataFrame({
            "timestamp": [1, 2, 3, 4, 5],
            "open": [100, 101, 102, 103, 104],
            "high": [101, 102, 103, 104, 105],
            "low": [99, 100, 101, 102, 103],
            "close": [100, 102, 104, 103, 105],
            "volume": [10, 10, 10, 10, 10],
        })
        return df, 5, 1

    monkeypatch.setattr(_service, "fetch_daily_ohlc", fake_fetch)

    r = client.get("/v1/signal")
    assert r.status_code == 200
    data = r.json()
    assert data["asset"] == "BTC"
    assert data["signal"] in {"BUY", "HOLD", "SELL"}
    assert 0.0 <= data["confidence"] <= 1.0


