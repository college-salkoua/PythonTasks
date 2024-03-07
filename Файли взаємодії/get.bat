@echo off
rem Run git pull
git pull

rem Change directory to src
cd ../src

rem Run python parser.py
python parse.py

rem Pause to see the output
pause
