from frictionless import Resource
from pprint import pprint
import pandas as pd

# Load GeoJSON
data = Resource('../data/geojson/invalid-polygon.geojson')

# Print out data
pprint(data.read_rows())

# Write CSV to disk - generates _geom column with WKT geometry
data.write('../invalid-polygon.csv')

# Read data and rename _geom to geompol
data2 = pd.read_csv('../invalid-polygon.csv')

# Rename
data3 = data2.rename(columns={"_geom": "geompol"})

# Write
data3.to_csv('../invalid-polygon2.csv')
