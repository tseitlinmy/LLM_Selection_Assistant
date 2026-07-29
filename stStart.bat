@echo off
setlocal enabledelayedexpansion
REM This ensures that the !count! variable updates correctly inside the loop.
REM %~nx0: Dynamically displays the actual name and extension of your batch file in the help menu, no matter what you rename the file.

:: Check if the first parameter is empty
if "%~1"=="" (
    goto :ShowHelp
) else (
    goto :Start
)

:ShowHelp
echo ====================================================
echo                   SCRIPT HELP
echo ====================================================
echo Usage: %~nx0 <script path>
echo.
echo Description: 
echo   This script launches specified script in Streamlit
echo ====================================================
goto :End

:Start
python -m streamlit run %1

:End
endlocal