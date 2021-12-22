# - faire notebook jupyter

import geopandas as gpd
import json

# Data
df = gpd.read_file('../data/example-point-valid.geojson')
df = gpd.read_file('../data/example-point-invalid.geojson')

# Schema
f = open('../schema.json')
schema = json.load(f)
geoFields = [elt for elt in schema['fields'] if elt['type'] == 'geojson']
geoFields = geoFields[0]

# Bounds
refBb = geoFields['constraints']['bounds']

# Bounds
def controlXmin(xmin, refXmin) :
    ok = True
    if xmin < refXmin:
        print('KO xmin')
        ok = False
    return(ok)

def controlYmin(ymin, refYmin) :
    ok = True
    if ymin < refYmin:
        print('KO ymin')
        ok = False
    return(ok)

def controlXmax(xmax, refXmax) :
    ok = True
    if xmax > refXmax:
        print('KO xmax')
        ok = False
    return(ok)

def controlYmax(ymax, refYmax) :
    ok = True
    if ymax > refYmax:
        print('KO ymax')
        ok = False
    return(ok)
    
def ControlBounds(bb, refbb):
    okXmin = controlXmin(bb[0], refBb[0])
    okYmin = controlYmin(bb[1], refBb[1])
    okXmax = controlXmax(bb[2], refBb[2])
    okYmax = controlYmax(bb[3], refBb[3])
        
    ok = (okXmin & okYmin & okXmax & okYmax)
    
    print(ok)
    
    return(ok)
    
# Unique
def controlUnique(i, df):
    ok = True
    for j in range(df.geometry.count()):
        if j != i:
            if df.geometry[j] == df.geometry[i]:
                print('KO ', i, ' equals ', j)
                ok = False
    
    return(ok)
    
# Overlaps
def controlOverlaps(i, df):
    ok = True
    for j in range(df.geometry.count()):
        if i != j:
            if df.geometry[i].intersects(df.geometry[j]):
                print('KO ', i, ' overlaps ', j)
                ok = False
    
    return(ok)
    
# Geometry types
def controlGeomType(geomType,refGeomType):
    ok = geomType.lower() == refGeomType.lower()
    return(ok)

# CRS
def controlCRS(crs, refCrs):
    print(crs, refCrs)
    ok = crs.lower() == refCrs.lower()
    return(ok)
    
# Process
for i in range(df.geometry.count()):
    print(i)
    
    print('>> CRS')
    okCRS = controlCRS(df.crs.srs, geoFields['crs'])
    
    print('>> GEOMETRY TYPE')
    okGeomType = controlGeomType(df.geometry[i].geom_type, geoFields['geomtype'])
    
    print('>> BOUNDS')
    okBounds = ControlBounds(df.geometry[i].bounds, refBb)
    
    print('>> UNIQUE')
    if geoFields['constraints']['unique'] :
     okUnique = controlUnique(i, df)
     
    print('>> OVERLAPS')
    if geoFields['constraints']['overlaps'] is False :
     okUnique = controlOverlaps(i, df)
    

