# Epic 0 - Cierre Final

## Estado Actual

**Epic 0 está casi completa**, pero requiere **una acción manual** para cerrar definitivamente.

## Acciones Pendientes (Bloqueantes)

### 1. Generar y agregar pnpm-lock.yaml al repositorio

**Por qué es necesario:**
- CI/CD requiere `--frozen-lockfile` para builds reproducibles
- Sin lockfile, el pipeline frontend fallará
- El lockfile debe estar en el repo para que todos usen las mismas versiones

**Cómo hacerlo:**

```bash
# Opción 1: Instalar pnpm y ejecutar
npm install -g pnpm
cd frontend
pnpm install
git add pnpm-lock.yaml
git commit -m "Add pnpm-lock.yaml for reproducible builds"

# Opción 2: Usar scripts proporcionados
bash frontend/scripts/generate-lockfile.sh
# O en PowerShell:
.\frontend\scripts\generate-lockfile.ps1
```

**Verificar:**
```bash
cd frontend
pnpm install --frozen-lockfile  # Debe pasar sin errores
```

## Verificación Final

Una vez que `pnpm-lock.yaml` esté en el repo, verificar:

- [ ] Backend tests pasan: `cd backend && poetry run pytest`
- [ ] Frontend build pasa: `cd frontend && pnpm build`
- [ ] Frontend tests pasan: `cd frontend && pnpm test`
- [ ] CI/CD pipeline pasa completamente (verificar en GitHub Actions)
- [ ] Auditoría documenta estado real (ver `docs/AUDIT_TECHNICAL_DEBT.md`)

## Criterios de Aceptación - Checklist Final

- [x] Documento de auditoría completo con hallazgos concretos
- [x] Plan de migración a Binance documentado (conceptual)
- [x] Frontend mínimo funcional con tests que pasan
- [x] Scripts de ops básicos funcionales
- [x] CI/CD riguroso (mypy sin `|| true`, security audit riguroso)
- [x] Documentación que refleje realidad del proyecto
- [ ] **pnpm-lock.yaml en repositorio** ← **PENDIENTE**

## Una vez completado

Epic 0 puede darse por cerrada. La base está lista para Epic 2 (Frontend completo).


