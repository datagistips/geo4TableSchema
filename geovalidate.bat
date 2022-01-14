@echo off

:: POINT ::
C:\python39\python geovalidate.py invalid-point.csv schema-point.json
echo ---


:: POLYGON ::

rem _geom column
C:\python39\python geovalidate.py invalid-polygon.csv schema-polygon.json
echo ---

rem geompol column
C:\python39\python geovalidate.py invalid-polygon2.csv schema-polygon.json geompol
echo ---

rem bounds specified as a polygon
C:\python39\python geovalidate.py invalid-polygon2.csv schema-polygon-with-geombounds.json geompol
echo ---


:: POINT & POLYGON ::

C:\python39\python geovalidate.py invalid-mixed.csv schema-mixed.json

pause