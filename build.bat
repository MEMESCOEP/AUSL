@echo off
cls
echo AUSL Build Script
set pypth=%1
set pyexe=%pypth%\python.exe -m nuitka --standalone --onefile --follow-imports %pypth%\AUSL_latest\AUSL.py
echo PYPATH: "%pyexe%"
%pyexe%
