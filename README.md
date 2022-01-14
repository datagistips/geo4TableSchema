# spatial-schema
On OpenData portals, we observe a significative proportion of spatial data, but tools for checking and validating spatial dimensions are lacking.

[TableSchema](https://specs.frictionlessdata.io//table-schema/) is used on [schema.data.gouv.fr](schema.data.gouv.fr) to check data but, from my point of view, it misses some specifications for spatial data. 

The purpose of `spatial-schema` is to :

- suggest **new tags for TableSchema** in order to **document** spatial aspects (geometry types, bounds, coordinate reference system,...)
- demonstrate with a **POC** how **controls** could be made by confronting spatial data against this new form of TableSchema.

This proposal introduces a new `wkt` column type, following the [cividi frictionless-geojson project](https://github.com/cividi/frictionless-geojson).

## Guide
Install `frictionless_geojson` extension

	pip install frictionless_geojson

> `frictionless_geojson` will be used to convert a GeoCSV into GeoJSON

### Spatial data
Let's consider [invalid-polygon.csv](invalid-polygon.csv)

If we look inside, there's a column named `_geom` that embeds geometries as WKT. 

See the `label` column to get information for the nature of the errors :

fid  |  label                     |  _geom
-----|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
0    |  overlaps 1 and 2          |  POLYGON ((6.2391152188576 44.23331451379951, 6.16161790287912 43.81456334596878, 6.748383295287605 43.83317838644907, 6.727884839005895 43.97646145496493, 6.693028069588689 44.22010833314981, 6.628122911243207 44.22199668957071, 6.2391152188576 44.23331451379951))
1    |  equals 2                  |  POLYGON ((6.032455709581656 44.19521093015088, 5.567471813710779 43.8860751165404, 6.290780096176586 43.62588938560129, 6.438394031373689 44.08970643816957, 6.032455709581656 44.19521093015088))
2    |  equals 1                  |  POLYGON ((6.032455709581656 44.19521093015088, 5.567471813710779 43.8860751165404, 6.290780096176586 43.62588938560129, 6.438394031373689 44.08970643816957, 6.032455709581656 44.19521093015088))
3    |  has a hole                |  POLYGON ((5.685562961868463 43.70225709069182, 5.445690317173171 43.59010057475595, 6.014003967682018 43.28462037694144, 6.025075012821801 43.60079116963337, 5.685562961868463 43.70225709069182), (5.744608535947305 43.60079116963337, 5.914364561423971 43.52591712304841, 5.822105851925783 43.48041248152663, 5.656040174829043 43.58475456510651, 5.744608535947305 43.60079116963337))
4    |  is outside                |  POLYGON ((7.198605797638769 43.0153859029196, 6.678266676068982 42.96949811360918, 6.704099114728473 42.73683492429429, 7.257651371717611 42.77747881636348, 7.198605797638769 43.0153859029196))
...    |  ...  |  ...

Here's a map of the data (you can get it as a geojson [here](data/geojson/invalid-polygon.geojson)) :

<img src="files/map-id.png" width=50%/>

We can see that :

- 1 and 2 are **duplicates**
- 1 **overlaps** 0
- 2 **overlaps** 0
- 4 is **outside** the data extent
- 6 is **not valid**, as it has a self-intersection
- 7 is **too small**

### Schema
Let's consider the [schema-polygon.json](schema-polygon.json) schema file.

Inside, geographic specifications are  :

	{
         "name":"_geom",
         "title":"Polygon geometry",
         "description":"Polygon geometry",
         "type":"wkt",
         "geomtype":"polygon",
         "crs":"EPSG:4326",
         "horizontalAccuracy":5,
         "constraints":{
            "required":true,
            "unique":true,
            "overlaps":false,
            "minArea":100000000,
            "bounds":[
               4.9283,
               43.0756,
               7.6412,
               45.0923
            ]
         }
      }

Here are the corresponding requirements :

- Data MUST be in `WGS84`
- Rows MUST contain geometries
- Geomtries MUST be of `Polygon` type
- Geometries MUST be unique
- Geometries MUST NOT overlap
- Geometries MUST be at least 100000000 square meters
- Geometries MUST be inside the `[4.9283, 43.0756, 7.6412, 45.0923]` bounding box.

### Geovalidate
Now that we have :

- the [invalid-polygon.csv](invalid-polygon.csv) data
- the [schema-polygon.json](schema-polygon.json) schema

We can control our dat against the schema :

	python geovalidate.py invalid-polygon.csv schema-polygon.json

Here is the result :
	
	File : invalid-polygon.csv
	
	0 : 0 overlaps 1
	0 : 0 overlaps 2
	1 : 1 equals 2 (duplicates)
	1 : 1 overlaps 0
	2 : 2 equals 1 (duplicates)
	2 : 2 overlaps 0
	4 : ymin too low. ymin (42.736835) is inferior to ymin bounds (43.075600)
	6 : Geometry is not valid
	7 : Area too small. It is smaller than 100000000 square meters
	8 : Geometry is not valid

For the moment, `geovalidate` provides [all these checkings](mds/CHECKS)

You can check [geovalidate.bat](geovalidate.bat) to have an example of checkings on Point, Polygon, Mixed data

Also, you can can check the [reference documentation](mds/REFERENCE) to have to all the specifications.

### Python
Inside python, you can control data like this :

```python
from geovalidate import *	
geovalidate('../data/invalid-polygon.csv', 'schema-polygon.json')
```


