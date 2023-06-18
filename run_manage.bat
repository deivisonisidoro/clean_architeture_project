@echo off

:: Get the absolute path of the script's directory
for %%I in ("%~dp0") do set "SCRIPT_DIR=%%~fI"

:: Set the Python path to the project root directory
set PYTHONPATH=%SCRIPT_DIR%

:: Run the manage.py script
python "%SCRIPT_DIR%\infrastructure\django_core\manage.py" %*
