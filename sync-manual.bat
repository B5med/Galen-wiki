@echo off
setlocal enabledelayedexpansion

set REPO=%~dp0
set ONEDRIVE=D:\OneDrive - mediclinic.cz\3R Resource\Galen
set PYTHON=python
set GIT_AUTHOR_NAME=Vojtech Benada
set GIT_AUTHOR_EMAIL=vojtech.benada@mediclinic.cz
set GIT_COMMITTER_NAME=Vojtech Benada
set GIT_COMMITTER_EMAIL=vojtech.benada@mediclinic.cz

echo.
echo ================================================
echo  FONS Galen wiki - rucni synchronizace
echo ================================================
echo.

cd /d "%REPO%"

echo [0/5] Synchronizace s GitHub (pull --rebase --autostash)...
git pull --rebase --autostash
if errorlevel 1 (
    echo.
    echo CHYBA: git pull --rebase selhal - vyres konflikty rucne.
    echo Pripadne: git rebase --abort  (a pak: git stash pop)
    pause
    exit /b 1
)

echo.
echo [1/5] Stahuji z Confluence...
%PYTHON% scripts\sync_confluence.py --out .
if errorlevel 1 (
    echo CHYBA: Sync selhal.
    pause
    exit /b 1
)

echo.
echo [2/5] Konverze do Markdown (GalenMD)...
%PYTHON% scripts\convert_to_markdown.py --out .
if errorlevel 1 (
    echo CHYBA: Konverze selhal.
    pause
    exit /b 1
)

echo.
echo [3/5] Generovani rejstriku (_Index.md)...
%PYTHON% scripts\generate_index.py --out .
if errorlevel 1 (
    echo CHYBA: Generovani rejstriku selhalo.
    pause
    exit /b 1
)

echo.
echo [4/5] Nahravani na GitHub...
git add -A
git diff --cached --quiet
if errorlevel 1 (
    for /f "tokens=2 delims==" %%d in ('wmic os get LocalDateTime /value 2^>nul') do set DT=%%d
    set TODAY=!DT:~0,4!-!DT:~4,2!-!DT:~6,2!
    git commit -m "sync: !TODAY! (rucni spusteni)"
    git push
    if errorlevel 1 (
        echo.
        echo CHYBA: git push selhal - vzdaleny repozitar ma novejsi zmeny.
        echo Spust: git pull --rebase ^&^& git push
        pause
        exit /b 1
    )
    echo Hotovo - zmeny nahrane na GitHub.
) else (
    echo Zadne zmeny - neni co nahravat.
)

echo.
echo [5/5] Zrcadleni GalenMD na OneDrive...
%PYTHON% scripts\mirror_to_onedrive.py --src . --dst "%ONEDRIVE%"
if errorlevel 1 (
    echo CHYBA: Mirror selhal.
    pause
    exit /b 1
)

echo.
echo ================================================
echo  Hotovo.
echo ================================================
echo.
pause
