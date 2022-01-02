import geopandas as gpd

df = gpd.read_file('../data/geojson/emprise.geojson')

wkt = df.geometry[0].wkt
print(wkt)

def getGeomFromWkt(wkt):
    geom = gpd.GeoSeries.from_wkt([wkt])
    return(geom)
    
geom = getGeomFromWkt(wkt)

print(geom)
