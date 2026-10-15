@echo off
setlocal
cd /d "%~dp0"

echo Creating in: %cd%
echo.
set "name="
set /p "name=Client / project name: "

if not defined name goto noname
if exist "%name%" goto exists

rem ---- YOUR LAYOUT: edit the folder names below if you want different ones ----
mkdir "%name%\01_ASSETS\Images"
if errorlevel 1 goto failed
mkdir "%name%\01_ASSETS\Logos"
mkdir "%name%\01_ASSETS\Fonts"
mkdir "%name%\01_ASSETS\References"
mkdir "%name%\02_OPEN FILE"
mkdir "%name%\03_RENDER\Preview"
mkdir "%name%\03_RENDER\Mockup"
mkdir "%name%\03_RENDER\Final"
mkdir "%name%\04_PACKAGE"
rem ----------------------------------------------------------------------------

echo.
echo Done! Project folder is ready.
goto end

:noname
echo.
echo No name entered, nothing created.
goto end

:exists
echo.
echo That project already exists. Nothing was changed.
goto end

:failed
echo.
echo Could not create the folder. Avoid these characters in the name: \ / : * ? ^< ^> ^|
goto end

:end
echo.
pause
