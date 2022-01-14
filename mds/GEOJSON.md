## GeoJSON files
You can also check a CSV file with a WKT column. 

For this, just type :

	from geovalidate import *	
	geovalidate('../data/geojson/invalid-polygon.geojson', '../schema.json')

> Internally, the script will convert the CSV to GeoJSON before inspecting it