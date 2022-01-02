def getMultiGeomType(refGeomType):
    if refGeomType == 'point':
        refGeomType = ['point', 'multipoint']
    if refGeomType == 'linestring':
        refGeomType = ['linestring', 'multilinestring']
    if refGeomType == 'polygon':
        refGeomType = ['polygon', 'multipolygon']
        
    return(refGeomType)
    
def getMultiGeomTypes(refGeomTypes):
    res = [getMultiGeomType(elt) for elt in refGeomTypes]
    res = [item for sublist in res for item in sublist]
    return(res)
    
print(getMultiGeomType('point'))
print(getMultiGeomTypes(['point', 'polygon']))



