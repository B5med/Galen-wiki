@echo off
chcp 65001 >nul
setlocal

set REPO=%~dp0
set ONEDRIVE=D:\OneDrive - mediclinic.cz\3R Resource\Galen
set PYTHON=python

echo.
echo ================================================
echo  FONS Galen wiki – ruční synchronizace
echo ================================================
echo.

:: 1. Stažení z Confluence
echo [1/3] Stahuji z Confluence...
cd /d "%REPO%"
%PYTHON% scripts\sync_confluence.py --out .
if errorlevel 1 (
    echo CHYBA: Sync selhal.
    pause
    exit /b 1
)

:: 2. Mirror do OneDrive
echo.
echo [2/3] Kopíruji do OneDrive...
%PYTHON% scripts\mirror_to_onedrive.py --src . --dst "%ONEDRIVE%"
if errorlevel 1 (
    echo CHYBA: Mirror selhal.
    pause
    exit /b 1
)

:: 3. Git commit + push
echo.
echo [3/3] Nahrávám na GitHub...
git add -A
git diff --cached --quiet
if errorlevel 1 (
    for /f "tokens=*" %%d in ('powershell -command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
    git commit -m "sync: %TODAY% (ruční spuštění)"
    git push
    echo Hotovo – změny nahrány na GitHub.
) else (
    echo Žádné změny – není co nahrávat.
)

echo.
echo ================================================
echo  Synchronizace dokončena.
echo ================================================
echo.
pause
