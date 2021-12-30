# if overlaps and unique, print (also unique)

from frictionless import Resource
import geopandas as gpd
import pandas as pd
import json
import pathlib
import tempfile
import math

# Schema
def getGeoSchemaFields(schema):
    f = open(schema)
    schema = json.load(f)
    geoSchemaFields = [elt for elt in schema['fields'] if elt['type'] == 'geojson']
    geoSchemaFields = geoSchemaFields[0]
    return(geoSchemaFields)
    

# Bounds
def controlXmin(xmin, refXmin) :
    ok = (xmin >= refXmin)
    return(ok)

def controlYmin(ymin, refYmin) :
    ok = (ymin >= refYmin)
    return(ok)

def controlXmax(xmax, refXmax) :
    ok = (xmax <= refXmax)
    return(ok)

def controlYmax(ymax, refYmax) :
    ok = (ymax <= refYmax)
    return(ok)

# Unique
def controlUnique(geom1, geom2):
    ok = (geom1 != geom2)
    return(ok)
    
# Overlaps
def controlOverlaps(geom1, geom2):
    ok = (geom1.overlaps(geom2) is False)
    return(ok)
    
# Geometry types
def controlGeomType(geomType, refGeomType):
    ok = geomType.lower() == refGeomType.lower()
    return(ok)

# CRS
def controlCRS(crs, refCrs):
    ok = crs.lower() == refCrs.lower()
    if not ok:
        print('%s CRS is required but %s is found'%(refCrs, crs))
    return(ok)
    
# Valid
def controlValid(geom):
    ok = geom.is_valid
    return(ok)
    
# Area
def controlArea(geom, crs, minArea):
    ok = (gpd.GeoSeries(geom).set_crs('EPSG:4326').to_crs('EPSG:3857').area > minArea).all()
    return(ok)
    
# Absence
def controlPresence(data, geomCol):
    ok = True
    n = data[data[geomCol].isnull()].shape[0]
    print(n)
    if n > 0:
        ok = False
        print('%d entities without geometries were found :')
        for i in range(data.shape[0]):
            value = data[geomCol][i]
            if isinstance(value, float):
                if math.isnan(value):
                    print('#%d'%i)
        print('They will be skipped')
    return(ok)
    
def readData(fileName, geomCol = '_geom'):
    fileExtension = pathlib.Path(fileName).suffix
    
    if fileExtension == '.csv' :
        print('File %s is CSV (it will first be converted to GeoJSON in order to be processed.\n'%fileName)
        
        # Filter data
        data = pd.read_csv(fileName)
        data = data[data['geompol'].notnull()]
        
        # Write CSV
        tempDir = tempfile.gettempdir()
        tempCSV = pathlib.Path(tempDir)/(pathlib.Path(fileName).stem+'.csv')
        data.to_csv(tempCSV)
        
        # Rename CSV
        if geomCol != '_geom':
            # Rename
            data = pd.read_csv(tempCSV).rename(columns = {geomCol:'_geom'})
            
            # Write CSV
            tempDir = tempfile.gettempdir()
            tempCSV = pathlib.Path(tempDir)/(pathlib.Path(fileName).stem+'.csv')
            data.to_csv(tempCSV)
            
        # Read CSV
        data = Resource(tempCSV)
            
        # Write GeoJSON
        tempDir = tempfile.gettempdir()
        tempGeoJSON = pathlib.Path(tempDir)/(pathlib.Path(fileName).stem+'.geojson')
        data.write(tempGeoJSON)
        
        # Read Data
        data = gpd.read_file(tempGeoJSON)
    else:
        print('File %s is GeoJSON\n'%fileName)
        
        # Read Data
        data = gpd.read_file(fileName)
    
    return(data)
        
# Process
def geovalidate(fileName, schema, geomCol='_geom'):
    
    # Schema
    geoSchemaFields = getGeoSchemaFields(schema)
    
    # Check if geometry exists
    okPresence = controlPresence(pd.read_csv(fileName), geomCol)
    
    # Data
    data = readData(fileName, geomCol)
    
    # Control
    for i in range(data.geometry.count()):
        if 'crs' in geoSchemaFields.keys():
            okCRS = controlCRS(data.crs.srs, geoSchemaFields['crs'])
            if not okCRS:
                print('#%d : wrong %s CRS. Must be %s'%(i, data.crs.srs, geoSchemaFields['crs']))
        
        if 'geomtype' in geoSchemaFields.keys(): 
            okGeomType = controlGeomType(data.geometry[i].geom_type, geoSchemaFields['geomtype'])
            if not okGeomType:
                print("#%d : '%s' is found but '%s' geometry type is required"%(i, data.geometry[i].geom_type, geoSchemaFields['geomtype']))
            
        okValid = controlValid(data.geometry[i])
        if not okValid:
            print('#%d : Geometry is not valid'%i)
        
        if 'constraints' in geoSchemaFields.keys():
            if 'bounds' in geoSchemaFields['constraints'].keys():
                bb = data.geometry[i].bounds
                refbb = geoSchemaFields['constraints']['bounds']
                
                okXmin = controlXmin(bb[0], refbb[0])
                if not okXmin:
                    print('#%d : xmin (%f) is inferior to xmin bounds (%f)'%(i, bb[0], refbb[0]))
                
                okYmin = controlYmin(bb[1], refbb[1])
                if not okYmin:
                    print('#%d : ymin (%f) is inferior to ymin bounds (%f)'%(i, bb[1], refbb[1]))
                
                okXmax = controlXmax(bb[2], refbb[2])
                if not okXmax:
                    print('#%d : xmax (%f) is superior to xmax bounds (%f)'%(i, bb[2], refbb[2]))
                
                okYmax = controlYmax(bb[3], refbb[3])
                if not okYmax:
                    print('#%d : ymax (%f) is superior to ymax bounds (%f)'%(i, bb[3], refbb[3]))
                
            if 'minArea' in geoSchemaFields['constraints'].keys(): 
                okArea = controlArea(data.geometry[i], data.crs.srs, geoSchemaFields['constraints']['minArea'])
                if not okArea:
                    print('#%d : Area bigger than %d square meters'%(i, geoSchemaFields['constraints']['minArea']))
                
            if 'unique' in geoSchemaFields['constraints'].keys():
                if geoSchemaFields['constraints']['unique'] :
                    for j in range(data.geometry.count()):
                        if j != i:
                            okUnique = controlUnique(data.geometry[i], data.geometry[j])
                            if not okUnique:
                                print('#%d : Duplicate found : %d equals %d'%(i,i,j))
            
            if 'overlaps' in geoSchemaFields['constraints'].keys():
                if not geoSchemaFields['constraints']['overlaps'] :
                    for j in range(data.geometry.count()):
                        if i != j:
                            okOverlaps = controlOverlaps(data.geometry[i], data.geometry[j])
                            if not okOverlaps:
                                print('#%d : %d overlaps %d'%(i, i, j))