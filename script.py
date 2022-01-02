from geovalidate import *

# Invalid point layer with '_geom' column
# ~ geovalidate('data/csv/invalid-point.csv', 'schema1.json')
print('---')

# Invalid polygon layer with 'geompol' column
# ~ geovalidate('data/csv/invalid-polygon.csv', 'schema1.json') # generates error
# ~ geovalidate('data/csv/invalid-polygon.csv', 'schema1.json', geomCol = 'geompol')

# Schema with WKT Bounds
geovalidate('data/csv/invalid-polygon.csv', 'schema-with-geombounds.json', geomCol = 'geompol')

# ~ print('---')

# Polygon
# ~ geovalidate('../data-csv/invalid-polygon.csv', '../schema1.json', geomCol = 'geompol')
# ~ print('---')

# Mixed with _geom column
# ~ geovalidate('../data-csv/example-mixed-invalid.csv', '../schema2.json')
# ~ print('---')
