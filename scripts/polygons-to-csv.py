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

# Empty rows
n_rows = data2.shape[0]
empty_data = pd.DataFrame([[n_rows, 'No geometry', None], [n_rows + 1, 'No geometry', None]], columns=['fid', 'label','_geom'], index=['x', 'y'])

# Append
data3 = data2.append(empty_data)

# Write
data3.to_csv('../invalid-polygon.csv', index = False)
