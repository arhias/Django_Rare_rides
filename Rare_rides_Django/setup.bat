@echo off
chcp 65001

py --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not found. Opening the Python download page...
    start https://www.python.org/downloads/
    echo Please download and install Python, then run the script again.
    pause
    exit /b
)

py -m pip --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo pip is not found. Installing pip...
    py -m ensurepip --upgrade
)

py -m django --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Django is not found. Installing Django...
    py -m pip install django
)

if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    py -m pip install -r requirements.txt
) else (
    echo requirements.txt not found. Creating it...
    echo django > requirements.txt
    py -m pip install -r requirements.txt
)

echo Applying database migrations...
py manage.py migrate

echo Starting Django server on port 8000...
start http://127.0.0.1:8000

py manage.py runserver 8000

pause
