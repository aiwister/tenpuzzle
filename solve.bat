@echo off
where /q z
if %errorlevel% == 0 (
    tenpuzzle
) else (
    echo installing command...
    where /q git
    if %errorlevel% == 0 (
        git 
    ) else (
        echo Please install Git!
)
)
pause