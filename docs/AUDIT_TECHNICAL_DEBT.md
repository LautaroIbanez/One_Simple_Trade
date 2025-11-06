# Auditoría de Deuda Técnica - One Simple Trade

**Fecha**: 2025-01-XX  
**Epic**: 0 - Reset Estratégico  
**Estado**: ✅ Completado (2025-01-XX)  
**Última actualización**: 2025-01-XX

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
- [x] Documentar rate limits de CoinGecko y agregar manejo de errores (2025-01-XX) - Limitaciones documentadas en metodología
- [x] Plan de migración a Binance documentado (conceptual) - Ver `docs/MIGRATION_PLAN.md` (2025-01-XX)
- [ ] Implementar `BinanceProvider` como alternativa - **DEFERIDO A FUTURA EPIC**
- [ ] Agregar health checks de proveedores - **DEFERIDO A FUTURA EPIC**
- [ ] Implementar fallback automático si proveedor principal falla - **DEFERIDO A FUTURA EPIC**

**Estado**: ✅ Limitaciones documentadas. Abstracción de proveedores implementada. Plan de migración conceptual creado. Implementación real de Binance deferida a futura epic.

**Prioridad**: ALTA (parcialmente resuelto - documentado, implementación real deferida)

---

### 2. Frontend scaffold funcional (CRÍTICO resuelto)

**Estado actual:**
- Existe código fuente en `frontend/src/` (App.tsx, main.tsx, tests).
- `pnpm-lock.yaml` está versionado en el repositorio.
- CI instala con `pnpm install --frozen-lockfile` y valida lint/tests/build.

**Impacto:**
- La CI/CD frontend valida un scaffold real y reproducible.

**Plan de acción:**
- [x] Crear estructura mínima funcional: `src/App.tsx`, `src/main.tsx`, `index.html` (2025-01-XX)
- [x] Componente mínimo que muestre estado de backend (2025-01-XX)
- [x] Test básico que valide renderizado (2025-01-XX)
- [x] Generar y versionar `pnpm-lock.yaml` (2025-11-06)
- [x] Verificar que build y tests pasen en CI con `--frozen-lockfile` (2025-11-06)

**Estado**: ✅ Scaffold funcional creado y validado en CI. Lockfile versionado.

**Prioridad**: ALTA (✅ RESUELTO)

---

### 3. Ops inexistente (MEDIO)

**Estado actual:**
- `ops/scripts/` solo contiene README con "TBD"
- No hay scripts de deployment
- No hay docker-compose
- No hay configuración de worker/background tasks
- No hay runbook operativo

**Plan de acción:**
- [x] Script básico de health check del backend (2025-01-XX) - `ops/scripts/health_check.sh` y `health_check.ps1`
- [x] Script conceptual de backup de datos (mock) (2025-01-XX) - `ops/scripts/data_backup_conceptual.sh`
- [x] docker-compose.yml mínimo para desarrollo local (2025-01-XX)
- [x] Runbook operativo básico (`docs/RUNBOOK.md`) (2025-01-XX)

**Estado**: ✅ Scripts básicos funcionales creados. docker-compose.yml configurado. Runbook operativo documentado.

**Prioridad**: MEDIA (✅ RESUELTO)

---

### 4. CI/CD no riguroso (MEDIO)

**Estado actual:**
- `mypy app || true` oculta errores de tipado
- Frontend CI no tiene código que validar
- Security audits no fallan la build

**Plan de acción:**
- [x] Remover `|| true` de mypy, hacer que falle la build si hay errores (2025-01-XX)
- [ ] Agregar threshold mínimo de cobertura de tests - **DEFERIDO** (requiere tests más completos)
- [ ] Hacer que security audits críticos fallen la build - **REQUIERE CORRECCIÓN**: Actualmente usa `|| echo`, debe ser riguroso

**Estado**: ✅ mypy riguroso. ✅ Security audit riguroso (2025-01-XX): Falla build con vulnerabilidades altas.

**Prioridad**: MEDIA (✅ RESUELTO)

---

### 5. Documentación idealizada (BAJO)

**Estado actual:**
- README describe arquitectura que no existe (frontend completo, scripts de ops)
- No hay documentación de limitaciones reales
- No hay runbook operativo

**Plan de acción:**
- [x] Actualizar README para reflejar estado real del proyecto (2025-01-XX)
- [x] Documentar qué NO existe aún (2025-01-XX)
- [x] Crear runbook operativo básico (2025-01-XX) - `docs/RUNBOOK.md`

**Estado**: ✅ README actualizado con estado real (✅/🔄/❌). Limitaciones documentadas. Runbook creado.

**Prioridad**: BAJA (✅ RESUELTO)

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

- [x] Documento de auditoría completo (este documento) ✅
- [x] Plan de migración a Binance documentado (conceptual) ✅
- [x] Frontend mínimo funcional con tests que pasan ✅ (requiere pnpm-lock.yaml en repo)
- [x] Scripts de ops básicos funcionales ✅
- [x] CI/CD riguroso sin `|| true` - ✅ mypy riguroso, ✅ security audit riguroso
- [x] Documentación que refleje realidad del proyecto ✅

## Acciones Pendientes (Bloqueantes para cerrar Epic 0)

1. ✅ **CI/CD security audit riguroso** - CORREGIDO (2025-01-XX): Security audit ahora falla build con vulnerabilidades altas
2. ✅ **pnpm-lock.yaml generado y agregado al repo** (2025-11-06)

**Estado final**: ✅ Epic 0 cerrada. Reproducibilidad garantizada en frontend con lockfile versionado.

---

## Notas

Este documento debe actualizarse conforme se resuelvan los hallazgos. Cada item resuelto debe marcarse con fecha y commit hash.

