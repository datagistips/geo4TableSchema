from geovalidate import *

# Schema
schema = '../schema.json'

# Data
fileName = '../data/example-polygon-invalid.geojson'
fileName = '../data/example-point-invalid.geojson'
fileName = '../data/example-mixed-invalid.csv'
fileName = '../outputs/example-point-invalid.csv'
fileName = '../outputs/example-polygon-invalid.csv'

# Geovalidate
geovalidate(fileName, schema)
        

