@echo off

::Point
C:\python39\python geovalidate.py data/csv/invalid-point.csv schema-point.json
echo ---

:: Polygon
rem throws an error
C:\python39\python geovalidate.py data/csv/invalid-polygon.csv schema-polygon.json
echo ---

rem specifies geompol geometry column
C:\python39\python geovalidate.py data/csv/invalid-polygon.csv schema-polygon.json geompol
echo ---

rem bounds specified as a polygon
C:\python39\python geovalidate.py data/csv/invalid-polygon.csv schema-polygon-with-geombounds.json geompol
echo ---

:: Point & Polygon
C:\python39\python geovalidate.py data/csv/invalid-mixed.csv schema-mixed.json

pause