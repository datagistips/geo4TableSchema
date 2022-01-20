## Polygon CSV

### Schema with multiple columns
The geometry column in our [`invalid-polygon.csv`](..invalid-polygon.csv) data is named `_geom`

Let's consider, [`schema-polygon-multipleColumns.json`](../schemas/schema-polygon-multipleColumns.json), a schema has multiple geometry columns. 

The first geometry column, specified in the schema, will be analyzed by default and the first geometry column of the schema is not named `_geom`, but `geomRGF93`

So, if you control your data

	C:\python39\python geovalidate.py invalid-polygon.csv schemas\schema-polygon-multipleColumns.json

You'll get :

	File : invalid-polygon.csv
	
	2 geometry columns are present in the schema.
	Only geomRGF93 will be analysed.
	
	You can choose the geometry column that will be controlled with :
	> geovalidate data.csv schema.json wktcolumn
	
	[Error] 'geomRGF93' geometry column does not exist. Exiting...

To analyze `_geom`, you'll have to specify the name of the column as a third argument :

	C:\python39\python geovalidate.py invalid-polygon.csv schemas\schema-polygon-multipleColumns.json _geom


### Bounds
The schema [`schema-polygon-with-geombounds.json`](../schemas/schema-polygon-with-geombounds.json) specifies bounds for the data like this :

	"bounds":"POLYGON ((6.561512449318343 42.86044120200139, 5.445690317173171 43.59010057475595, 5.567471813710779 43.8860751165404, 6.032455709581656 44.19521093015088, 6.2391152188576 44.23331451379951, 6.614145636255817 44.27585946282259, 7.184853561048693 44.02066087075947, 7.138592392594731 42.91867862746965, 6.561512449318343 42.86044120200139))"
	
It's the precise geometry of the polygon that must contain the data

You can control your data :

	C:\python39\python geovalidate.py invalid-polygon.csv schemas\schema-polygon-with-geombounds.json

You'll get :
	
	...
	6 : the geometry is not contained by the bounds geometry
	...
	
## Point CSV
The geometry column in `invalid-point.csv` is named `_geom`

This line analyzes a simple point CSV :

	C:\python39\python geovalidate.py invalid-point.csv schema-point.json

And you get :

	File : invalid-point.csv
	
	Geometry column : '_geom' is the geometry column, according to the schema
	
	Analyzing _geom...
	
	1 : 1 equals 3 (duplicates)
	2 : ymin too low. ymin (42.682602) is inferior to ymin bounds (43.075600)
	3 : 3 equals 1 (duplicates)

## Mixed Data CSV
The CSV contains polygon and point Data.  
The schema contains this geometry type specification :

	"geomtype":["point", "polygon"],


Control is made with :

	C:\python39\python geovalidate.py invalid-mixed.csv schema-mixed.json
