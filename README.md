# spatial-schema
A proposal for including spatial dimension and checks on geodata with frictionless suite.

Introduces specifications for `geojson` and a new `geowkt` type

## `geojson`

Additional specifications for `geojson` type

### Examples
Some examples to illustrate these specification

#### A point geometry column

    "fields":[
      {
         "name":"geompoint",
         "title":"geometry",
         "description":"Point geometry",
         "type":"geojson",
         "geomtype":"Point",                              # point type
         "srs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 7.6412, 43.0756, 45.0923]  # [xmin, ymin, xmax, ymax]
         }
      }
     ]
     
#### Two geometry columns

    "fields":[
      {
         "name":"geompoint",
         "title":"Point geometry",
         "description":"Point geometry",
         "type":"geojson",
         "geomtype":"point",                              # point type
         "srs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 7.6412, 43.0756, 45.0923]  # [xmin, ymin, xmax, ymax]
         }
      },
      {
         "name":"geompolygon",
         "title":"Polygon geometry",
         "description":"Polygon geometry",
         "type":"geojson",
         "geomtype":"polygon",                            # polygon type
         "srs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 7.6412, 43.0756, 45.0923], # [xmin, ymin, xmax, ymax]
            "overlaps":true,                              # two polygons can overlap
            "gaps":true                                   # there can be some gaps in the data
         }
      }
     ]
     
Here, we have two columns : `geompoint` and `geompolygon`  
Two polygons can overlap

#### Two columns in different SRS
    "fields":[
      {
         "name":"geompoint_WGS84",
         "title":"Point geometry in WGS84",
         "description":"Point geometry in WGS84",
         "type":"geojson",
         "geomtype": "Point",                             # point type
         "srs" : "EPSG:4326",                             # WGS84 - World Geodetic System 1984, used in GPS
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 43.0756, 45.0923, 7.6412]  # [xmin, ymin, xmax, ymax]
         }
      },
      {
         "name":"geompoint_lamb93",
         "title":"geometry in RGF93",
         "description":"Point geometry in RGF93, according to IGN",
         "type":"geojson",
         "geomtype": "Point",                             # point type
         "srs" : "IGNF:LAMB93",                           # Lambert 93
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 43.0756, 45.0923, 7.6412]  # [xmin, ymin, xmax, ymax]
         }
      }
     ]
     
### `geomtype`
Can be one or many of : `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, `MultiPolygon`

Can contain multiple values if multiple geometry types are allowed

If only Point type is authorized :

    ...
    geomtype : ["Point"]
    ...

If points and polygons are authorized :
    
    ...
    geomtype : ["Point", "MultiPoint", "Polygon", "MultiPolygon"]
    ...

### `srs`
The spatial reference system to consider the data with.

Examples : `EPSG:4326` , `IGNF:LAMB93`

Must be readable by PROJ4 library

### Constraints

#### `unique`
If true, then geometries must be unique

#### `bounds`
Specifies `xmin`, `ymin`, `xmax`, `ymax` bounds for the data.

Example :
       
       ...
       "bounds": [4.9283, 43.0756, 7.6412, 45.0923]
       ...


#### `overlaps`
If `true`, then two geometries can overlap. It can be two neighboring polygons, two lines that cross, a point contained in a polygon.

#### `gaps`
Gaps are one of the topological errors for polygons, besides overlaps. It's a property only valid for polygons.

If `true`, then two polygons can have a gap between them.

## `geowkt`
In addition to `geopoint` and `geojson` types, it would be nice to add `geowkt` WKT support to TableSchema

The field contains data describing geographic data as WKT point.

- **type** : POINT, MULTIPOINT, LINESTRING, MULTILINESTRING, POLYGON, MULTIPOLYGON, GEOMETRYCOLLECTION

Here are some examples of WKT strings : 

        MULTIPOINT ((10 40), (40 30), (20 20), (30 10))

        MULTILINESTRING ((10 10, 20 20, 10 40),(40 40, 30 30, 40 20, 30 10))

       GEOMETRYCOLLECTION (POINT (40 10), LINESTRING (10 10, 20 20, 10 40), POLYGON ((40 40, 20 45, 45 30, 40 40))) 
       
### Example
    "fields":[
      {
         "name":"geompoint",
         "title":"geometry",
         "description":"Point geometry",
         "type":"geowkt",
         "geomtype": ["POINT"],                           # POINT type, no MULTIPOINT
         "srs" : "EPSG:4326",                             # WGS84 - World Geodetic System 1984, used in GPS
         "example" : "POINT (5 44)",
         "constraints":{
            "required":true,                              # geometry must not be empty
            "unique":true,                                # geometries must be unique
            "bounds": [4.9283, 43.0756, 7.6412, 45.0923]  # [xmin, ymin, xmax, ymax]
         }
      }
     ]

## Checks
### Regular expression to check WKT LineString

    (MULTI|multi)?(LINESTRING|linestring)\(((|,\s?)\(((|,\s?)(-?[0-9](\.[0-9]+)?\s-?[0-9](\.[0-9]+)?))+\))+\)

## TODO
- additional constraints ? holes, min and max inter distances between points etc...
- illustrate
- develop tools to check these elements
- proj4, shapely, grass, qgis libraries

