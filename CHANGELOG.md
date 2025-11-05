# Changelog

All notable changes to this project will be documented in this file.

## [Epic 0] - 2025-01-XX

### Reset estratégico y baseline operable

#### Auditoría y cleanup
- ✅ Abstraída dependencia de CoinGecko en capa de proveedores intercambiables
  - Creada interfaz `MarketDataProvider` (ABC)
  - Implementado `CoinGeckoProvider` como proveedor por defecto
  - `MarketDataService` ahora acepta cualquier proveedor compatible
  - Documentadas brechas: CoinGecko es dependencia externa, pero ahora intercambiable

#### Monorepo real
- ✅ Estructura reorganizada:
  - `backend/` - FastAPI Python service
  - `frontend/` - React/Vite TypeScript app (scaffold)
  - `shared/` - Tipos TypeScript compartidos (`api.ts`)
  - `ops/` - Scripts de infraestructura y deployment

#### Tooling disciplinado
- ✅ Backend:
  - Migrado de `requirements.txt` a Poetry (`pyproject.toml`)
  - Configurado Ruff para linting (reglas: E, F, I, N, W, UP, B, C4, SIM)
  - Configurado mypy para type checking (modo gradual, ignore pandas/scipy/numpy)
  - Pip-audit para seguridad de dependencias
- ✅ Frontend:
  - Configurado PNPM como package manager
  - ESLint con reglas TypeScript y React
  - Prettier para formateo consistente
  - Vitest para testing con cobertura

#### CI/CD mínimo pero serio
- ✅ GitHub Actions con matrices:
  - Backend: Python 3.11 y 3.12
  - Frontend: Node.js 20
- ✅ Pipeline ejecuta:
  - Linting (Ruff, ESLint)
  - Type checking (mypy, tsc)
  - Tests (pytest, vitest)
  - Builds (vite build)
  - Security audits (pip-audit, npm audit)

#### Documentación base
- ✅ README raíz con alcance, arquitectura y comandos
- ✅ CHANGELOG para tracking de cambios
- ✅ READMEs en backend/ y ops/scripts/

### Deuda técnica identificada
- CoinGecko es única fuente de datos (ahora intercambiable vía providers)
- OHLC sintetizado desde close prices (limitación documentada)
- Cache en memoria sin persistencia (TBD: Redis opcional)
- Tests unitarios sin mocks de red en algunos casos (mejorado en Epic 0)

---

## [Epic 1] - 2025-01-XX (Pre-Epic 0)

### Backend core (FastAPI + Señal diaria)

- ✅ Backend FastAPI con endpoints `/health`, `/v1/market/ohlc`, `/v1/signal`
- ✅ Integración CoinGecko para datos diarios de BTC
- ✅ Indicadores: EMA20/EMA50, RSI14, MACD 12/26/9, ATR14, volatilidad 30d
- ✅ Motor de señal BUY/HOLD/SELL con confianza y explicación
- ✅ Tests unitarios (8 tests pasando)
- ✅ Documentación metodológica (`docs/methodology.md`)

