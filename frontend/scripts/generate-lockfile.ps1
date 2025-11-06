# Script para generar pnpm-lock.yaml (PowerShell)
# Este archivo debe ejecutarse antes de commitear cambios en package.json

$ErrorActionPreference = "Stop"

Write-Host "Generando pnpm-lock.yaml..."

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$frontendPath = Split-Path -Parent $scriptPath
Set-Location $frontendPath

if (-not (Get-Command pnpm -ErrorAction SilentlyContinue)) {
    Write-Host "Error: pnpm no está instalado" -ForegroundColor Red
    Write-Host "Instalar con: npm install -g pnpm"
    exit 1
}

pnpm install --frozen-lockfile=false

Write-Host "✓ pnpm-lock.yaml generado" -ForegroundColor Green
Write-Host "Importante: Agregar pnpm-lock.yaml al repositorio antes de commitear"


