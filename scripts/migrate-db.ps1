Write-Host "[biomedical-ai] $PSCommandPath"
Set-Location backend; alembic upgrade head
