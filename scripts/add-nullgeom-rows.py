from frictionless import Resource
from pprint import pprint
import pandas as pd

# Read data and rename _geom to geompol
data = pd.read_csv('../invalid-polygon.csv')

# Empty rows
empty_data = pd.DataFrame([[None, None, None], [None, None, None]], columns=['fid', 'label','_geom'], index=['x', 'y'])

# Append
data2 = data.append(empty_data)

# Write
data2.to_csv('../invalid-polygon2.csv')
