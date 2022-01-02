from frictionless import Resource
from pprint import pprint

# Load GeoJSON
data = Resource('../data/geojson/invalid-polygon.geojson')

# Print out data
pprint(data.read_rows())

# Write CSV to disk - generates _geom column with WKT geometry
data.write('../data/csv/temp-polygon.csv')
