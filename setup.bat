@echo off
REM Student ID Card Generator System - Setup Script for Windows

echo.
echo ================================================
echo Student ID Card Generator System - Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

echo Python and Node.js found!
echo.

REM Setup Backend
echo Setting up Backend...
cd backend

if exist venv (
    echo Activating existing virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo Installing Python dependencies...
pip install -r requirements.txt -q

echo.
echo Backend setup complete!
echo.

REM Setup Frontend
cd ..\frontend
echo Setting up Frontend...

if exist node_modules (
    echo Node modules already exist, skipping npm install...
) else (
    echo Installing npm dependencies...
    call npm install
)

echo.
echo Frontend setup complete!
echo.

echo.
echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo.
echo 1. Start Backend:
echo    - Open Command Prompt in 'backend' folder
echo    - Run: venv\Scripts\activate.bat
echo    - Run: python app.py
echo.
echo 2. Start Frontend:
echo    - Open Command Prompt in 'frontend' folder
echo    - Run: npm run dev
echo.
echo 3. Access Application:
echo    - Backend API: http://localhost:8000
echo    - Frontend: http://localhost:5173
echo    - API Docs: http://localhost:8000/docs
echo.
echo 4. Default Credentials:
echo    - Username: admin
echo    - Password: admin123
echo.
echo ================================================
echo.
pause
