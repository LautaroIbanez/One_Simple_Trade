# Epic 0 — Reset estratégico y baseline operable

## Objetivo

Reorganizar la base del proyecto para que todas las features siguientes sean viables y mantenibles. Establecer disciplina en tooling, CI/CD y documentación.

## Entregables

### ✅ Auditoría y cleanup

**Inventariado:**
- Dependencia hardcodeada de CoinGecko en múltiples lugares
- Estructura de proyecto plana sin separación clara frontend/backend
- Tooling inconsistente (requirements.txt, sin linting/type checking)
- Sin CI/CD estructurado

**Acciones realizadas:**
- Abstraída dependencia de CoinGecko en capa de proveedores intercambiables
  - `MarketDataProvider` (ABC) como interfaz base
  - `CoinGeckoProvider` como implementación por defecto
  - `MarketDataService` ahora acepta cualquier proveedor compatible
- Documentadas brechas: CoinGecko es dependencia externa, pero ahora intercambiable

### ✅ Monorepo real

Estructura reorganizada:
```
one-simple-trade/
├── backend/          # FastAPI service
│   ├── app/         # Código de aplicación
│   ├── tests/       # Tests unitarios
│   └── pyproject.toml
├── frontend/        # React/Vite app
│   └── package.json
├── shared/          # Código compartido
│   └── types/       # TypeScript types
├── ops/             # Scripts de infraestructura
└── docs/            # Documentación
```

### ✅ Tooling disciplinado

**Backend:**
- Migrado de `requirements.txt` a Poetry (`pyproject.toml`)
- Ruff configurado para linting (reglas: E, F, I, N, W, UP, B, C4, SIM)
- mypy configurado para type checking (modo gradual)
- pip-audit para seguridad de dependencias

**Frontend:**
- PNPM como package manager
- ESLint con reglas TypeScript y React
- Prettier para formateo consistente
- Vitest para testing con cobertura

### ✅ CI/CD mínimo pero serio

GitHub Actions con matrices:
- Backend: Python 3.11 y 3.12
- Frontend: Node.js 20

Pipeline ejecuta:
- Linting (Ruff, ESLint)
- Type checking (mypy, tsc)
- Tests (pytest, vitest)
- Builds (vite build)
- Security audits (pip-audit, npm audit)

### ✅ Documentación base

- README raíz con alcance, arquitectura y comandos
- CHANGELOG para tracking de cambios
- READMEs en backend/ y ops/scripts/
- Documentación de metodología existente preservada

## Deuda técnica identificada

1. **CoinGecko como única fuente de datos**: Ahora intercambiable vía providers, pero sigue siendo dependencia externa
2. **OHLC sintetizado desde close prices**: Limitación documentada en metodología
3. **Cache en memoria sin persistencia**: TBD: Redis opcional para producción
4. **Tests unitarios**: Algunos casos sin mocks de red (mejorado en Epic 0)

## Criterios de aceptación cumplidos

- ✅ Código funcional y probado (8 tests pasando)
- ✅ Estructura de monorepo clara
- ✅ Tooling configurado y documentado
- ✅ CI/CD ejecutando en matrices múltiples
- ✅ Documentación base completa

## Próximos pasos

- Epic 2: Frontend minimalista (React/Vite, UI oscura, señal diaria, historial)
- Epic 3: Backtesting y reporting
- Epic 4: Mejoras cuantitativas

