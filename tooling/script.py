from geovalidate import *

# Polygon with _geom column
geovalidate('../data-csv/example-polygon-invalid.csv', '../schema1.json')
print('---')

# Polygon with geompol column
# ~ geovalidate('../data-csv/example-polygon-invalid2.csv', '../schema1.json') # generates error
geovalidate('../data-csv/example-polygon-invalid2.csv', '../schema1.json', geomCol = 'geompol')
print('---')

# Polygon with geompol column and missing geometry
geovalidate('../data-csv/example-polygon-invalid3.csv', '../schema1.json', geomCol = 'geompol')
print('---')

# Point with _geom column
geovalidate('../data-csv/example-point-invalid.csv', '../schema2.json')
print('---')

# Mixed with _geom column
geovalidate('../data-csv/example-mixed-invalid.csv', '../schema2.json')
print('---')
