@echo off
title Oprogramowanie ANTY-idiotowe
echo Czy chcesz wlaczyc notatnik? [Wpisz tak lub nie]
set /p "odp="
if %odp%==tak start msedge.exe
if NOT %odp%==tak goto menu1

:menu1
cls
echo Czy jestes pewny/a ze nie chcesz go wlaczyc? [Wpisz tak lub nie]
set /p "odp1="
if %odp1$==tak exit
if NOT $odp1%==tak goto menu2

:menu2
cls 
echo Wiec chcesz wlaczyc notanik? [Wpisz tak lub nie]
set /p "odp2="
if %odp2%==tak start notepad.exe
if NOT %odp2%==tak exit
