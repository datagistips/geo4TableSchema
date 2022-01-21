# Reference

## `geomtype`

Can be one or many of : `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, `MultiPolygon`, `GeometryCollection`

Can contain multiple values if multiple geometry types are allowed

If only Point type is authorized :

    geomtype : "Point"

If (multi)points and (multi)polygons are authorized :

    geomtype : ["Point", "MultiPoint", "Polygon", "MultiPolygon"]

---

## `crs`

The spatial reference system to consider the data with.

WGS 84 :

    "crs" : "EPSG:4326"

Lambert 93 :

    "crs" : "IGNF:LAMB93"

Must be readable by PROJ4 library

---

## `unique`

If `true`, then geometries must be unique

---

## `bounds`

Specifies `xmin`, `ymin`, `xmax`, `ymax` bounds for the data.

     "bounds": [4.9283, 43.0756, 7.6412, 45.0923]

If polygon bounds :

    "bounds":"POLYGON ((6.561512449318343 42.86044120200139, 5.445690317173171 43.59010057475595, 5.567471813710779 43.8860751165404, 6.032455709581656 44.19521093015088, 6.2391152188576 44.23331451379951, 6.614145636255817 44.27585946282259, 7.184853561048693 44.02066087075947, 7.138592392594731 42.91867862746965, 6.561512449318343 42.86044120200139))"

---

## `overlaps`

If `true`, then two geometries can overlap.

    "overlaps" : true

It can be :

- two neighboring polygons
- two lines that cross
- a point contained in a polygon

---

## `horizontalAccuracy`

    "horizontalAccuracy":5

Horizontal accuracy is +- 5 meters.

<!--

### `scaleRange`

### `scaleZoom`

### `gaps`
Gaps are one of the topological errors for polygons, besides overlaps. It's a property only callable for polygons.

If `true`, then two polygons can have a gap between them.
-->
