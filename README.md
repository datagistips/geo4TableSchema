# spatial-schema
A proposal for including spatial dimension to TableSchema (https://specs.frictionlessdata.io/table-schema/) and implement spatial checks on data containing geometry columns

Introduces specifications for `geojson` and a new `geowkt` type

## `geojson`
Additional specifications for `geojson` type

### Examples
Some examples help to illustrate the specifications proposal

#### A point geometry column
Let's say a CSV file has a `geompoint` column. Below could be its specifications :

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
     
> At the end of the document, attributes, properties and possible constraints affected to the spatial dimension are listed
     
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
Can be one or many of : `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, `MultiPolygon`, `GeometryCollection`

Can contain multiple values if multiple geometry types are allowed

If only Point type is authorized :

    ...
    geomtype : ["Point"]
    ...

If (multi)points and (multi)polygons are authorized :
    
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
[See this document for the specifications of `geowkt` type field](geowkt.md)

## Additional resources
### Spatial Data Package
- https://github.com/cividi/spatial-data-package
- https://github.com/cividi/spatial-data-package/discussions
- https://specs.frictionlessdata.io/data-package/

### frictionless-geojson
- https://frictionless-hackathon.herokuapp.com/project/9
- https://pypi.org/project/frictionless-geojson/
- https://github.com/cividi/frictionless-geojson

