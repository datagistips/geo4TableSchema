from f_geovalidate import *

# Read CLI arguments
dataPath = sys.argv[1]
schemaPath = sys.argv[2]

geomCol = None
if len(sys.argv) > 3:
    geomCol = sys.argv[3]

# Geovalidate
if geomCol is None:
    geovalidate(dataPath, schemaPath)
else :
    geovalidate(dataPath, schemaPath, geomCol)
