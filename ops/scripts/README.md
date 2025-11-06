# Operations Scripts

Utility scripts for deployment, data migration, and maintenance.

## Scripts Disponibles

### Health Check

- `health_check.sh` - Health check del backend (bash)
  - Uso: `bash ops/scripts/health_check.sh [URL]`
  - Por defecto verifica `http://localhost:8000/health`
  - Retorna código de salida 0 si backend está saludable, 1 si falla

- `health_check.ps1` - Health check del backend (PowerShell)
  - Uso: `.\ops\scripts\health_check.ps1 [-BackendUrl URL]`
  - Por defecto verifica `http://localhost:8000/health`

### Data Backup

- `data_backup_conceptual.sh` - Placeholder para backup de datos
  - **Estado**: Conceptual solamente
  - **Nota**: Backend actualmente usa cache en memoria, no hay datos persistentes para backup
  - Documenta plan futuro de backup cuando se implemente persistencia

## Scripts Futuros (No Implementados)

- `deploy.sh` - Deployment automation (TBD)
- `migrate.sh` - Database migrations (TBD - no hay base de datos aún)

## Uso

Ver `docs/RUNBOOK.md` para guía operativa completa.

