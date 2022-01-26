# `geowkt`

In addition to `geopoint` and `geojson` types, it would be nice to add `geowkt` WKT support to TableSchema

The field contains data describing geographic data as WKT point.

- **type** : `POINT`, `MULTIPOINT`, `LINESTRING`, `MULTILINESTRING`, `POLYGON`, `MULTIPOLYGON`, `GEOMETRYCOLLECTION`

Here are some examples of WKT strings :

        MULTIPOINT ((10 40), (40 30), (20 20), (30 10))

        MULTILINESTRING ((10 10, 20 20, 10 40),(40 40, 30 30, 40 20, 30 10))

       GEOMETRYCOLLECTION (POINT (40 10), LINESTRING (10 10, 20 20, 10 40), POLYGON ((40 40, 20 45, 45 30, 40 40)))

## Example

```json
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
```

---

## Checks

### Regular expression to check WKT LineString

```regex
(MULTI|multi)?(LINESTRING|linestring)\(((|,\s?)\(((|,\s?)(-?[0-9](\.[0-9]+)?\s-?[0-9](\.[0-9]+)?))+\))+\)
```
