@echo off
cls
echo AUSL Build Script
set pypth=%1
set pyexe=%pypth%\python.exe -m nuitka --standalone --onefile --follow-imports AUSL.py
echo PYPATH: "%pyexe%"
start %pyexe%
pause
