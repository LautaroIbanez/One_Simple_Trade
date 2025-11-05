# Runbook Operativo - One Simple Trade

## Estado Actual

⚠️ **PROYECTO EN DESARROLLO** - Este runbook documenta operaciones básicas. Muchas features están en estado conceptual.

## Prerequisitos

- Python 3.11+ con Poetry instalado
- Node.js 20+ con PNPM instalado
- Docker y Docker Compose (opcional, para desarrollo)

## Desarrollo Local

### Backend

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload --port 8000
```

**Verificar salud:**
```bash
curl http://localhost:8000/health
# O con script:
bash ops/scripts/health_check.sh
# O en PowerShell:
.\ops\scripts\health_check.ps1
```

**Endpoints disponibles:**
- `GET /health` - Estado del servicio
- `GET /v1/market/ohlc` - Datos OHLC con indicadores
- `GET /v1/signal` - Señal diaria BUY/HOLD/SELL

### Frontend

```bash
cd frontend
pnpm install  # Primera vez
pnpm dev
```

Frontend corre en `http://localhost:5173` y hace proxy a backend en `http://localhost:8000`.

### Docker Compose (Desarrollo)

```bash
docker-compose up
```

**Nota**: Los Dockerfiles son básicos y para desarrollo. No están optimizados para producción.

## Testing

### Backend

```bash
cd backend
poetry run pytest -q --maxfail=1 --disable-warnings
poetry run ruff check .
poetry run mypy app
```

### Frontend

```bash
cd frontend
pnpm test
pnpm lint
pnpm format:check
pnpm build
```

## Troubleshooting

### Backend no responde

1. Verificar que está corriendo en puerto 8000
2. Ejecutar health check: `bash ops/scripts/health_check.sh`
3. Revisar logs de uvicorn
4. Verificar que CoinGecko API está accesible (puede tener rate limits)

### Frontend no se conecta al backend

1. Verificar que backend está corriendo en `http://localhost:8000`
2. Verificar proxy en `vite.config.ts`
3. Revisar consola del navegador para errores CORS

### Tests fallan

1. **Backend**: Verificar que todas las dependencias están instaladas (`poetry install`)
2. **Frontend**: Verificar que `pnpm install` se ejecutó y generó `pnpm-lock.yaml`
3. Verificar que no hay servicios externos bloqueados (CoinGecko puede tener rate limits)

## Limitaciones Conocidas

- **Datos**: Solo CoinGecko, OHLC sintetizado (ver `docs/methodology.md`)
- **Cache**: En memoria, se pierde al reiniciar
- **Sin persistencia**: No hay base de datos, todo es en memoria
- **Sin autenticación**: Endpoints públicos (por diseño)

## Monitoreo

Actualmente no hay monitoreo en producción. Para desarrollo:
- Backend logs: Salida de uvicorn
- Frontend logs: Consola del navegador
- Health checks: Scripts en `ops/scripts/`

## Próximos Pasos (No Implementados)

- [ ] Logging estructurado
- [ ] Métricas (Prometheus/Grafana)
- [ ] Alertas
- [ ] Backup de datos persistentes
- [ ] Rate limiting en backend
- [ ] Health checks más robustos

## Contacto

Para problemas operativos, revisar:
- `docs/AUDIT_TECHNICAL_DEBT.md` - Deuda técnica conocida
- `docs/MIGRATION_PLAN.md` - Plan de migración a Binance
- `CHANGELOG.md` - Historial de cambios

