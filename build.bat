@echo off
echo "AUSL Build Script"
SET pypth = %1
set pyexe = %pypth% + python.exe
start %pyexe% -m nuitka --standalone --onefile --follow-imports AUSL.py
