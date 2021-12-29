from frictionless import Resource
import geopandas as gpd
import json
import pathlib
import tempfile

# Schema
def getGeoSchemaFields(schema):
    f = open(schema)
    schema = json.load(f)
    geoSchemaFields = [elt for elt in schema['fields'] if elt['type'] == 'geojson']
    geoSchemaFields = geoSchemaFields[0]
    return(geoSchemaFields)
    

# Bounds
def controlXmin(xmin, refXmin) :
    ok = True
    if xmin < refXmin:
        ok = False
        print('xmin must be superior or equal to xmin bounds')
    return(ok)

def controlYmin(ymin, refYmin) :
    ok = True
    if ymin < refYmin:
        ok = False
        print('ymin must be superior or equal to ymin bounds')
    return(ok)

def controlXmax(xmax, refXmax) :
    ok = True
    if xmax > refXmax:
        ok = False
        print('xmax must be inferior or equal to xmax bounds')
    return(ok)

def controlYmax(ymax, refYmax) :
    ok = True
    if ymax > refYmax:
        ok = False
        print('ymax must be inferior or equal to ymax bounds')
    return(ok)
    
def ControlBounds(bb, refbb):
    okXmin = controlXmin(bb[0], refbb[0])
    okYmin = controlYmin(bb[1], refbb[1])
    okXmax = controlXmax(bb[2], refbb[2])
    okYmax = controlYmax(bb[3], refbb[3])
        
    ok = (okXmin & okYmin & okXmax & okYmax)
    
    return(ok)
    
# Unique
def controlUnique(data, i):
    ok = True
    for j in range(data.geometry.count()):
        if j != i:
            if data.geometry[j] == data.geometry[i]:
                print(i, ' equals ', j)
                ok = False
    
    return(ok)
    
# Overlaps
def controlOverlaps(data, i):
    ok = True
    for j in range(data.geometry.count()):
        if i != j:
            if data.geometry[i].overlaps(data.geometry[j]):
                print('%d overlaps %d'%(i, j))
                ok = False
    
    return(ok)
    
# Geometry types
def controlGeomType(geomType,refGeomType):
    ok = geomType.lower() == refGeomType.lower()
    if not ok:
        print('%s geometry type is required but %s is found'%(refGeomType, geomType))
    return(ok)

# CRS
def controlCRS(crs, refCrs):
    ok = crs.lower() == refCrs.lower()
    if not ok:
        print('%s CRS is required but %s is found'%(refCrs, crs))
    return(ok)
    
def readData(fileName):
    fileExtension = pathlib.Path(fileName).suffix
    if fileExtension == '.csv' :
        print('File %s is CSV, so we convert it to GeoJSON\n'%fileName)
        tempDir = tempfile.gettempdir()
        data = Resource(fileName)
        outputFile = pathlib.Path(tempDir)/(pathlib.Path(fileName).stem+'.geojson')
        data.write(outputFile)
        data = gpd.read_file(outputFile)
    else:
        print('GeoJSON')
        data = gpd.read_file(fileName)
    
    return(data)
        
# Process
def geovalidate(fileName, schema):
    
    # Schema
    geoSchemaFields = getGeoSchemaFields(schema)
    
    # Data
    data = readData(fileName)
    
    # Control
    for i in range(data.geometry.count()):
        print('>> Entity ', i)
        
        if 'crs' in geoSchemaFields.keys():
            okCRS = controlCRS(data.crs.srs, geoSchemaFields['crs'])
        
        if 'geomtype' in geoSchemaFields.keys(): 
            okGeomType = controlGeomType(data.geometry[i].geom_type, geoSchemaFields['geomtype'])
        
        if 'constraints' in geoSchemaFields.keys():
            if 'bounds' in geoSchemaFields['constraints'].keys():
                okBounds = ControlBounds(data.geometry[i].bounds, geoSchemaFields['constraints']['bounds'])
            
            if 'unique' in geoSchemaFields['constraints'].keys():
                if geoSchemaFields['constraints']['unique'] :
                 okUnique = controlUnique(data, i)
            
            if 'overlaps' in geoSchemaFields['constraints'].keys():
                if not geoSchemaFields['constraints']['overlaps'] :
                 okOverlaps = controlOverlaps(data, i)
         
        print('')
