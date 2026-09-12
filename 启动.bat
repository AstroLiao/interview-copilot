@echo off
chcp 65001 >nul
cd /d %~dp0
where uv >nul 2>nul
if %errorlevel%==0 (
  if not exist .venv (
    echo [init] 创建虚拟环境...
    uv venv .venv
    uv pip install -r requirements.txt --python .venv
  )
  set PY=.venv\Scripts\python.exe
) else (
  if not exist .venv (
    echo [init] 创建虚拟环境...
    python -m venv .venv
    .venv\Scripts\pip install -r requirements.txt
  )
  set PY=.venv\Scripts\python.exe
)
echo [start] Interview Copilot 启动中: http://localhost:8787
%PY% server.py
pause
