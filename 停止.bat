@echo off
chcp 65001 >nul
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8787 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"
echo [stop] Interview Copilot 已停止
timeout /t 1 >nul
