# Changelog

All notable changes to this project will be documented in this file.

## [Epic 0] - 2025-01-XX (REHECHO - Versión Rigurosa)

### Reset estratégico y baseline operable (con entregables verificables)

#### Auditoría y cleanup
- ✅ **Documento de auditoría real creado**: `docs/AUDIT_TECHNICAL_DEBT.md`
  - Hallazgos críticos documentados con severidad y esfuerzo estimado
  - Limitaciones reales de CoinGecko documentadas (OHLC sintetizado, solo diario)
  - Plan de migración a Binance documentado (conceptual) en `docs/MIGRATION_PLAN.md`
- ✅ Abstraída dependencia de CoinGecko en capa de proveedores intercambiables
  - Creada interfaz `MarketDataProvider` (ABC)
  - Implementado `CoinGeckoProvider` como proveedor por defecto
  - `MarketDataService` ahora acepta cualquier proveedor compatible
  - **Realidad**: Solo CoinGecko está implementado. Binance es plan conceptual.

#### Monorepo real
- ✅ Estructura reorganizada:
  - `backend/` - FastAPI Python service ✅ Funcional
  - `frontend/` - React/Vite TypeScript app ✅ Scaffold funcional creado
    - `src/App.tsx` - Componente básico que muestra estado del backend
    - `src/App.test.tsx` - Tests básicos creados
    - Requiere `pnpm install` para generar `pnpm-lock.yaml` y ejecutar
  - `shared/` - Tipos TypeScript compartidos (`api.ts`) ✅
  - `ops/` - Scripts de infraestructura ✅
    - `health_check.sh` y `health_check.ps1` - Scripts funcionales
    - `data_backup_conceptual.sh` - Placeholder documentado
  - `docker-compose.yml` - Configuración básica para desarrollo ✅

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

#### CI/CD riguroso
- ✅ GitHub Actions con matrices:
  - Backend: Python 3.11 y 3.12
  - Frontend: Node.js 20
- ✅ Pipeline ejecuta:
  - Linting (Ruff, ESLint)
  - Type checking (mypy, tsc) - **mypy sin `|| true`, falla build si hay errores**
  - Tests (pytest, vitest)
  - Builds (vite build)
  - Security audits (pip-audit, npm audit)
- ✅ Correcciones: Removido `|| true` de mypy, audit warnings no bloquean pero se reportan

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

