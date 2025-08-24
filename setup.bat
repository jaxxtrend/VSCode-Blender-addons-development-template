@echo off
echo Blender Add-on Development Template Setup (Windows)
echo =====================================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.10 or later from https://python.org
    pause
    exit /b 1
)

echo Creating Python virtual environment...
python -m venv .venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Install VS Code extensions:
echo    - Python (by Microsoft)
echo    - Blender Development (by Jacques Lucke)
echo.
echo 2. Update Blender path in .vscode\settings.json:
echo    - Edit 'blender.blenderExecutable.path'
echo    - Set it to your Blender executable path
echo.
echo 3. Open VS Code in this directory:
echo    code .
echo.
echo 4. Start developing your Blender add-on!
echo.
pause