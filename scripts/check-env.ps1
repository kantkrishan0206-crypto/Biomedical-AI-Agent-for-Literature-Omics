Write-Host "[biomedical-ai] $PSCommandPath"
foreach ($bin in @("git","node","pnpm","python","py","docker","kubectl","helm","psql","redis-cli")) { if (Get-Command $bin -ErrorAction SilentlyContinue) { Write-Host "ok $bin" } else { Write-Host "missing $bin" } }
