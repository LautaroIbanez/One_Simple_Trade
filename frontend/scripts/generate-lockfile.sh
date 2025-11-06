#!/bin/bash
# Script para generar pnpm-lock.yaml
# Este archivo debe ejecutarse antes de commitear cambios en package.json

set -e

echo "Generando pnpm-lock.yaml..."
cd "$(dirname "$0")/.."

if ! command -v pnpm &> /dev/null; then
    echo "Error: pnpm no está instalado"
    echo "Instalar con: npm install -g pnpm"
    exit 1
fi

pnpm install --frozen-lockfile=false

echo "✓ pnpm-lock.yaml generado"
echo "Importante: Agregar pnpm-lock.yaml al repositorio antes de commitear"


