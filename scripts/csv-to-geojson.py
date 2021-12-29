from frictionless import Resource
from pprint import pprint

# Load CSV
data = Resource('../data/example-mixed-invalid.csv')

# Print out data
pprint(data.read_rows())

# Write GeoJSON to disk - requires _geom column with WKT geometry
data.write('../outputs/example-mixed-invalid.geojson')
