#!/bin/bash
# Health check script for backend API
# Usage: ./health_check.sh [URL]

BACKEND_URL="${1:-http://localhost:8000}"
ENDPOINT="${BACKEND_URL}/health"

echo "Checking backend health at ${ENDPOINT}..."

response=$(curl -s -w "\n%{http_code}" "${ENDPOINT}")
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" -eq 200 ]; then
    echo "✓ Backend is healthy (HTTP ${http_code})"
    echo "Response: ${body}"
    exit 0
else
    echo "✗ Backend health check failed (HTTP ${http_code})"
    echo "Response: ${body}"
    exit 1
fi


