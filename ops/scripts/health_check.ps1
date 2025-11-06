# Health check script for backend API (PowerShell)
# Usage: .\health_check.ps1 [URL]

param(
    [string]$BackendUrl = "http://localhost:8000"
)

$endpoint = "$BackendUrl/health"

Write-Host "Checking backend health at $endpoint..."

try {
    $response = Invoke-RestMethod -Uri $endpoint -Method Get -ErrorAction Stop
    Write-Host "✓ Backend is healthy" -ForegroundColor Green
    Write-Host "Status: $($response.status)"
    Write-Host "Timestamp: $($response.timestamp)"
    exit 0
} catch {
    Write-Host "✗ Backend health check failed" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
    exit 1
}


