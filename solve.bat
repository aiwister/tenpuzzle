@echo off
where /q tenpuzzle
if %errorlevel% == 0 (
    tenpuzzle
) else (
    echo installing command...
    call (exit /b 0)
    where /q pip
    if %errorlevel% == 0 (
        pip install git+https://github.com/aiwister/tenpuzzle.git
        tenpuzzle
    ) else (
        echo Please install pip!
)
)
pause