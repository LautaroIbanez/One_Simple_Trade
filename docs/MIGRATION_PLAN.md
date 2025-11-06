# Plan de Migración: CoinGecko → Binance (Conceptual)

## Objetivo

Proporcionar una alternativa a CoinGecko usando Binance API, que ofrece:
- OHLC real (no sintetizado)
- Datos intraday disponibles
- Rate limits documentados
- Mayor confiabilidad para datos históricos

## Estado: PLAN CONCEPTUAL (No implementado)

⚠️ **Esta es una planificación, no una implementación real.**

## Comparación de APIs

| Feature | CoinGecko | Binance |
|---------|-----------|---------|
| OHLC real | ❌ (solo close) | ✅ Completo |
| Granularidad | Diaria | Diaria, 1h, 4h, etc. |
| Rate limit | No documentado | 1200 requests/min |
| Autenticación | No requerida | No requerida (pública) |
| Historial | 730 días | Ilimitado (kline) |

## Implementación Propuesta

### 1. Crear `BinanceProvider`

```python
# backend/app/services/providers/binance.py (NO EXISTE AÚN)
class BinanceProvider(MarketDataProvider):
    base_url = "https://api.binance.com/api/v3"
    
    async def fetch_daily_ohlc(self, asset_id, vs_currency, days):
        # Binance usa símbolos como "BTCUSDT"
        symbol = f"{asset_id.upper()}{vs_currency.upper()}"
        interval = "1d"  # daily
        limit = min(days, 1000)  # Binance max 1000 klines
        
        # Endpoint: GET /api/v3/klines
        # Params: symbol, interval, limit, startTime, endTime
        ...
```

### 2. Ventajas de Binance

- **OHLC real**: No necesitamos sintetizar
- **Mejor precisión**: ATR y volatilidad más precisos
- **Datos intraday**: Posibilidad de señales intradía en el futuro

### 3. Desventajas

- **Símbolo diferente**: "BTCUSDT" vs "bitcoin/usd"
- **Límite de 1000 klines**: Necesitamos paginación para >1000 días
- **Requiere conversión de timestamps**: Binance usa ms, CoinGecko también pero formato diferente

## Pasos de Implementación (Futuro)

1. **Fase 1**: Implementar `BinanceProvider` básico
2. **Fase 2**: Agregar paginación para historial largo
3. **Fase 3**: Comparar resultados CoinGecko vs Binance
4. **Fase 4**: Hacer Binance provider por defecto (opcional)
5. **Fase 5**: Mantener CoinGecko como fallback

## Estado Actual

- ❌ `BinanceProvider` no existe
- ❌ No hay tests comparativos
- ❌ No hay estrategia de migración gradual

## Notas

Este plan es conceptual. La implementación real requerirá:
- Testing exhaustivo de la API de Binance
- Validación de que los datos son consistentes
- Decisión sobre cuál usar por defecto
- Plan de rollback si hay problemas


