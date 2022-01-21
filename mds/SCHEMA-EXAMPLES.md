# `geojson`

Additional specifications for `geojson` type

## Examples

These examples help to illustrate the specifications proposal :

### One point geometry column

Let's say a CSV file has a `geompoint` column. Below could be its specifications :

```json
"fields":[
   {
      "name":"geompt",
      "title":"geometry",
      "description":"Point geometry",
      "type":"geojson",
      "geomtype":"Point",                              # point type
      "crs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
      "constraints":{
         "required":true,                              # geometry must not be empty
         "unique":true,                                # geometries must be unique
         "bounds":[4.9283, 43.0756, 7.6412, 45.0923]  # [xmin, ymin, xmax, ymax]
      }
   }
]
```

> [At this section](#geomtype), attributes, properties and possible constraints affected to the spatial dimension are listed

### One geometry column mixing (Multi)Points, (Multi)Polygons

Let's say a CSV file has a `geompoint` column. Below could be its specifications :

```json
"fields":[
   {
      "name":"geom",
      "title":"geometry",
      "description":"Point & Polygon geometry",
      "type":"geojson",
      "geomtype":["Point", "MultiPoint", "Polygon", "MultiPolygon"], # (multi)point and (multi)polygon type
      "crs":"EPSG:4326",                                             # WGS84 - World Geodetic System 1984, used in GPS
      "constraints":{
         "required":true,                                            # geometry must not be empty
         "unique":true,                                              # geometries must be unique
         "bounds":[4.9283, 43.0756, 7.6412, 45.0923]                # [xmin, ymin, xmax, ymax]
      }
   }
]
```

> [At this section](#geomtype), attributes, properties and possible constraints affected to the spatial dimension are listed

### Two geometry columns

```json
"fields":[
   {
      "name":"geompoint",
      "title":"Point geometry",
      "description":"Point geometry",
      "type":"geojson",
      "geomtype":"point",                              # point type
      "crs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
      "constraints":{
         "required":true,                              # geometry must not be empty
         "unique":true,                                # geometries must be unique
         "bounds":[4.9283, 43.0756, 7.6412, 45.0923]  # [xmin, ymin, xmax, ymax]
      }
   },
   {
      "name":"geompol",
      "title":"Polygon geometry",
      "description":"Polygon geometry",
      "type":"geojson",
      "geomtype":"polygon",                            # polygon type
      "crs":"EPSG:4326",                               # WGS84 - World Geodetic System 1984, used in GPS
      "constraints":{
         "required":true,                              # geometry must not be empty
         "unique":true,                                # geometries must be unique
         "bounds": [4.9283, 43.0756, 7.6412, 45.0923], # [xmin, ymin, xmax, ymax]
         "overlaps":true,                              # two polygons can overlap
         "gaps":true                                   # there can be some gaps in the data
      }
   }
]
```

- Here, we have two columns : `geompt` and `geompol`
- Two polygons can overlap : `"overlaps":true`

### Two columns in different CRS

```json
"fields":[
   {
      "name":"geomptwgs84",
      "title":"Point geometry in WGS84",
      "description":"Point geometry in WGS84",
      "type":"geojson",
      "geomtype": "Point",                             # point type
      "crs" : "EPSG:4326",                             # WGS84 - World Geodetic System 1984, used in GPS
      "constraints":{
         "required":true,                              # geometry must not be empty
         "unique":true,                                # geometries must be unique
         "bounds":[4.9283, 43.0756, 7.6412, 45.0923]   # [xmin, ymin, xmax, ymax]
      }
   },
   {
      "name":"geomptlamb93",
      "title":"geometry in RGF93",
      "description":"Point geometry in RGF93, according to IGN",
      "type":"geojson",
      "geomtype": "Point",                                         # point type
      "crs" : "IGNF:LAMB93",                                       # Lambert 93 from IGN (not EPSG, but IGNF:LAMB93)
      "constraints":{
         "required":true,                                          # geometry must not be empty
         "unique":true,                                            # geometries must be unique
         "bounds":[857155.03, 6221508.54, 1064910.92, 6454397.47]  # [xmin, ymin, xmax, ymax]
      }
   }
]
```
