# if overlaps and unique, print (also unique)

from frictionless import Resource
import geopandas as gpd
import pandas as pd
import json
import pathlib
import os
import tempfile
import math
import sys


# Schema
def readSchema(filePath):
    f = open(filePath)
    schema = json.load(f)
    return(schema)
    
def getGeoFields(schema):
    geoFields = [elt for elt in schema['fields'] if elt['type'] == 'wkt']
    geoFields = geoFields[0]
    return(geoFields)
    

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
def getMultiGeomType(refGeomType):
    if refGeomType in ['point', 'multipoint']:
        refGeomTypes = ['point', 'multipoint']
    if refGeomType in ['linestring', 'multilinestring']:
        refGeomTypes = ['linestring', 'multilinestring']
    if refGeomType in ['polygon', 'multipolygon']:
        refGeomTypes = ['polygon', 'multipolygon']
        
    return(refGeomTypes)
    
def getMultiGeomTypes(refGeomTypes):
    res = [getMultiGeomType(elt) for elt in refGeomTypes]
    res = [item for sublist in res for item in sublist]
    return(res)
    
def controlGeomType(geomType, refGeomType):
    geomType = geomType.lower()
    
    if isinstance(refGeomType, str):
        refGeomType = refGeomType.lower()
        refGeomTypes = getMultiGeomType(refGeomType)
        ok = (geomType in refGeomTypes)
    elif isinstance(refGeomType, list):
        refGeomTypes = [elt.lower() for elt in refGeomType]
        refGeomTypes = getMultiGeomTypes(refGeomTypes)
        ok = (geomType in refGeomTypes)
            
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
    
# Do geometries exist for all lines ?
def getEmptyGeomRows(data, geomCol):
    ok = True
    n = data[data[geomCol].isnull()].shape[0]
    emptyGeomRows = list()
    if n > 0:
        ok = False
        for i in range(data.shape[0]):
            value = data[geomCol][i]
            if isinstance(value, float):
                if math.isnan(value):
                    emptyGeomRows.append(i)
        print('%d entities without geometries were found : %s. They will be skipped\n'%(len(emptyGeomRows), ', '.join([str(elt) for elt in emptyGeomRows])))
    return(emptyGeomRows)
    
# Does the geometry column exist ?
def controlGeomColExists(data, geomCol) :
    ok = geomCol in data.columns
    return(ok)
    
def readData(filePath, geomCol = '_geom'):
    print('File : %s\n'%filePath)
    
    fileExtension = pathlib.Path(filePath).suffix
    
    if fileExtension == '.csv' :
        
        # Filter data
        data = pd.read_csv(filePath)
        nRows = data.shape[0]
        
        # Check if geometry column exists
        if not controlGeomColExists(data, geomCol):
            sys.exit("[Error] '%s' geometry column does not exist"%geomCol)
        
        # Check if geometries exist for all lines
        emptyGeomRows = getEmptyGeomRows(data, geomCol)
        nEmptyGeomRows = len(emptyGeomRows)
        if nEmptyGeomRows > 0 :
            # Filter non null geometries
            data = data[data[geomCol].notnull()]
        
            # Write CSV
            tempDir = tempfile.gettempdir()
            filePath = pathlib.Path(tempDir)/(pathlib.Path(filePath).stem+'.csv')
            data.to_csv(filePath)
        
        # Rename CSV
        if geomCol != '_geom':
            # Rename
            data = pd.read_csv(filePath).rename(columns = {geomCol:'_geom'})
            
            # Write CSV
            tempDir = tempfile.gettempdir()
            filePath = pathlib.Path(tempDir)/(pathlib.Path(filePath).stem+'.csv')
            data.to_csv(filePath)
            
        # Read CSV
        data = Resource(filePath)
            
        # Write GeoJSON
        tempDir = tempfile.gettempdir()
        tempGeoJSON = pathlib.Path(tempDir)/(pathlib.Path(filePath).stem+'.geojson')
        data.write(tempGeoJSON)
        
        # Read Data
        data = gpd.read_file(tempGeoJSON)
    else:
        # Read Data
        data = gpd.read_file(filePath)
    
    res = {'data' : data, 'nRows' : nRows, 'emptyGeomRows' : emptyGeomRows}
    return(res)
        
# Process
def geovalidate(dataPath, schemaPath, geomCol='_geom'):
    
    # Schema
    if not os.path.exists(schemaPath):
        sys.exit('[Error] %s does not exist'%schemaPath)
    
    schema = readSchema(schemaPath)
    geoFields = getGeoFields(schema)
    
    # Data
    if not os.path.exists(dataPath):
        sys.exit('[Error] %s does not exist'%dataPath)
        
    res = readData(dataPath, geomCol)
    data = res['data']
    
    # Control
    for i in range(data.geometry.count()):
        
        geom = data.geometry[i]
        
        if 'crs' in geoFields.keys():
            okCRS = controlCRS(data.crs.srs, geoFields['crs'])
            if not okCRS:
                print('%d : wrong %s CRS. Must be %s'%(i, data.crs.srs, geoFields['crs']))
        
        if 'geomtype' in geoFields.keys(): 
            okGeomType = controlGeomType(geom.geom_type, geoFields['geomtype'])
            if not okGeomType:
                print("%d : '%s' is found but '%s' geometry type is required"%(i, geom.geom_type, geoFields['geomtype']))
            
        okValid = controlValid(geom)
        if not okValid:
            print('%d : Geometry is not valid'%i)
        
        if 'constraints' in geoFields.keys():
            if 'bounds' in geoFields['constraints'].keys():
                bb = geom.bounds
                refbb = geoFields['constraints']['bounds']
                
                okXmin = controlXmin(bb[0], refbb[0])
                if not okXmin:
                    print('%d : xmin (%f) is inferior to xmin bounds (%f)'%(i, bb[0], refbb[0]))
                
                okYmin = controlYmin(bb[1], refbb[1])
                if not okYmin:
                    print('%d : ymin (%f) is inferior to ymin bounds (%f)'%(i, bb[1], refbb[1]))
                
                okXmax = controlXmax(bb[2], refbb[2])
                if not okXmax:
                    print('%d : xmax (%f) is superior to xmax bounds (%f)'%(i, bb[2], refbb[2]))
                
                okYmax = controlYmax(bb[3], refbb[3])
                if not okYmax:
                    print('%d : ymax (%f) is superior to ymax bounds (%f)'%(i, bb[3], refbb[3]))
                
            if 'minArea' in geoFields['constraints'].keys(): 
                okArea = controlArea(geom, data.crs.srs, geoFields['constraints']['minArea'])
                if not okArea:
                    print('%d : Area bigger than %d square meters'%(i, geoFields['constraints']['minArea']))
                
            if 'unique' in geoFields['constraints'].keys():
                if geoFields['constraints']['unique'] :
                    for j in range(data.geometry.count()):
                        if j != i:
                            okUnique = controlUnique(geom, data.geometry[j])
                            if not okUnique:
                                print('%d : Duplicate found : %d equals %d'%(i,i,j))
            
            if 'overlaps' in geoFields['constraints'].keys():
                if not geoFields['constraints']['overlaps'] :
                    for j in range(data.geometry.count()):
                        if j != i:
                            okOverlaps = controlOverlaps(geom, data.geometry[j])
                            if not okOverlaps:
                                print('%d : %d overlaps %d'%(i, i, j))
