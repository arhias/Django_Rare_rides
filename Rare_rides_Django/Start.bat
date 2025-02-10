@echo off
chcp 65001

python --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python не знайдено. Відкриваю сторінку для завантаження Python...
    start https://www.python.org/downloads/ 
    echo Будь ласка, завантажте та встановіть Python, а потім запустіть скрипт знову.
    pause
    exit /b
)

python -m pip --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo pip не знайдено. Встановлюю pip...
    python -m ensurepip --upgrade
)

python -m django --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Django не знайдено. Встановлюю Django...
    pip install django
)

if exist requirements.txt (
    echo Встановлюю залежності з requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt не знайдено. Створюю його...
    echo django > requirements.txt
    pip install -r requirements.txt
)
echo Застосовую міграції бази даних...
python manage.py migrate

echo Запускаю Django сервер на порту 8080...
start http://127.0.0.1:8080

python manage.py runserver 8080

pause
