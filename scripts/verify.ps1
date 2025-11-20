Param(
    [switch]$RecreateVenv
)

$ErrorActionPreference = "Stop"

Write-Host "[verify] Starting verification..." -ForegroundColor Cyan

if ($RecreateVenv -and (Test-Path ".venv")) {
    Write-Host "[verify] Removing existing .venv" -ForegroundColor Yellow
    Remove-Item -Recurse -Force .venv
}

if (-not (Test-Path ".venv")) {
    Write-Host "[verify] Creating venv" -ForegroundColor Cyan
    python -m venv .venv
}

Write-Host "[verify] Activating venv" -ForegroundColor Cyan
. .\.venv\Scripts\Activate.ps1

Write-Host "[verify] Upgrading pip and installing package + pytest" -ForegroundColor Cyan
python -m pip install --upgrade pip
pip install -e .
pip install pytest

Write-Host "[verify] Running tests" -ForegroundColor Cyan
pytest -q

Write-Host "[verify] Done." -ForegroundColor Green
