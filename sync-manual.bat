@echo off
setlocal

set REPO=%~dp0
set ONEDRIVE=D:\OneDrive - mediclinic.cz\3R Resource\Galen
set PYTHON=python

echo.
echo ================================================
echo  FONS Galen wiki - rucni synchronizace
echo ================================================
echo.

cd /d "%REPO%"

echo [1/3] Stahuji z Confluence...
%PYTHON% scripts\sync_confluence.py --out .
if errorlevel 1 (
    echo CHYBA: Sync selhal.
    pause
    exit /b 1
)

echo.
echo [2/3] Kopiruji do OneDrive...
%PYTHON% scripts\mirror_to_onedrive.py --src . --dst "%ONEDRIVE%"
if errorlevel 1 (
    echo CHYBA: Mirror selhal.
    pause
    exit /b 1
)

echo.
echo [3/3] Nahravani na GitHub...
git add -A
git diff --cached --quiet
if errorlevel 1 (
    for /f "tokens=*" %%d in ('powershell -command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
    git commit -m "sync: %TODAY% (rucni spusteni)"
    git push
    echo Hotovo - zmeny nahrane na GitHub.
) else (
    echo Zadne zmeny - neni co nahravat.
)

echo.
echo ================================================
echo  Hotovo.
echo ================================================
echo.
pause
