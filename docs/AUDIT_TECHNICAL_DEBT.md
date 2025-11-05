# Auditoría de Deuda Técnica - One Simple Trade

**Fecha**: 2025-01-XX  
**Epic**: 0 - Reset Estratégico  
**Estado**: En progreso

## Hallazgos Críticos

### 1. Dependencia única de CoinGecko (CRÍTICO)

**Estado actual:**
- Backend acoplado a CoinGecko como única fuente de datos
- `CoinGeckoProvider` es la única implementación real de `MarketDataProvider`
- No existe plan de migración ni implementación alternativa

**Limitaciones identificadas:**
- **OHLC sintetizado**: CoinGecko solo proporciona precios de cierre (`close`). Open/High/Low se sintetizan desde `close` usando heurísticas simples:
  ```python
  df["open"] = df["close"].shift(1).fillna(df["close"])
  df["high"] = df[["open", "close"]].max(axis=1)
  df["low"] = df[["open", "close"]].min(axis=1)
  ```
  Esto puede subestimar o sobreestimar rangos intraday reales, afectando cálculos de ATR y volatilidad.

- **Datos diarios únicamente**: CoinGecko Market Chart API solo ofrece granularidad diaria. No hay datos intraday disponibles.

- **Rate limiting desconocido**: No hay manejo explícito de rate limits de CoinGecko. Cache TTL de 300s ayuda, pero no garantiza protección contra throttling.

- **Sin fallback**: Si CoinGecko falla, el sistema no tiene alternativa.

**Plan de acción:**
- [ ] Documentar rate limits de CoinGecko y agregar manejo de errores
- [ ] Implementar `BinanceProvider` como alternativa (ver `docs/MIGRATION_PLAN.md`)
- [ ] Agregar health checks de proveedores
- [ ] Implementar fallback automático si proveedor principal falla

**Prioridad**: ALTA

---

### 2. Frontend vacío (CRÍTICO)

**Estado actual:**
- Solo archivos de configuración (package.json, tsconfig.json, etc.)
- No existe código fuente en `frontend/src/`
- No hay componentes, tests, ni assets
- `pnpm-lock.yaml` no existe (nunca se ejecutó `pnpm install`)

**Impacto:**
- CI/CD frontend no puede validar nada real
- Tooling configurado pero sin uso

**Plan de acción:**
- [ ] Crear estructura mínima funcional: `src/App.tsx`, `src/main.tsx`, `src/index.html`
- [ ] Componente mínimo que muestre "Hello World" o estado de carga
- [ ] Test básico que valide renderizado
- [ ] Generar `pnpm-lock.yaml` ejecutando `pnpm install`
- [ ] Verificar que build y tests pasen en CI

**Prioridad**: ALTA

---

### 3. Ops inexistente (MEDIO)

**Estado actual:**
- `ops/scripts/` solo contiene README con "TBD"
- No hay scripts de deployment
- No hay docker-compose
- No hay configuración de worker/background tasks
- No hay runbook operativo

**Plan de acción:**
- [ ] Script básico de health check del backend
- [ ] Script conceptual de backup de datos (mock)
- [ ] docker-compose.yml mínimo para desarrollo local
- [ ] Runbook operativo básico (`docs/RUNBOOK.md`)

**Prioridad**: MEDIA

---

### 4. CI/CD no riguroso (MEDIO)

**Estado actual:**
- `mypy app || true` oculta errores de tipado
- Frontend CI no tiene código que validar
- Security audits no fallan la build

**Plan de acción:**
- [ ] Remover `|| true` de mypy, hacer que falle la build si hay errores
- [ ] Agregar threshold mínimo de cobertura de tests
- [ ] Hacer que security audits críticos fallen la build

**Prioridad**: MEDIA

---

### 5. Documentación idealizada (BAJO)

**Estado actual:**
- README describe arquitectura que no existe (frontend completo, scripts de ops)
- No hay documentación de limitaciones reales
- No hay runbook operativo

**Plan de acción:**
- [ ] Actualizar README para reflejar estado real del proyecto
- [ ] Documentar qué NO existe aún
- [ ] Crear runbook operativo básico

**Prioridad**: BAJA

---

## Métricas de Deuda Técnica

| Categoría | Severidad | Esfuerzo estimado | Prioridad |
|-----------|-----------|-------------------|-----------|
| Dependencia CoinGecko | CRÍTICA | 8h | ALTA |
| Frontend vacío | CRÍTICA | 4h | ALTA |
| Ops inexistente | MEDIA | 4h | MEDIA |
| CI/CD no riguroso | MEDIA | 2h | MEDIA |
| Documentación idealizada | BAJA | 2h | BAJA |

**Total esfuerzo estimado**: ~20 horas

---

## Criterios de Aceptación para Epic 0

- [ ] Documento de auditoría completo (este documento)
- [ ] Plan de migración a Binance documentado (conceptual)
- [ ] Frontend mínimo funcional con tests que pasan
- [ ] Scripts de ops básicos funcionales
- [ ] CI/CD riguroso sin `|| true`
- [ ] Documentación que refleje realidad del proyecto

---

## Notas

Este documento debe actualizarse conforme se resuelvan los hallazgos. Cada item resuelto debe marcarse con fecha y commit hash.

