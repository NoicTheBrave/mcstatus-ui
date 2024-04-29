@echo off

rem Check if Python 3 is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed. Please install Python 3 to run this script.
    exit /b 1
)

rem Run the Python script
python3 mcstatus-ui.py
