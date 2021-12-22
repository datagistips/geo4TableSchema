### `geomtype`
Can be one or many of : `Point`, `LineString`, `Polygon`, `MultiPoint`, `MultiLineString`, `MultiPolygon`, `GeometryCollection`

Can contain multiple values if multiple geometry types are allowed

#### If only Point type is authorized :

    ...
    geomtype : ["Point"]
    ...

#### If (multi)points and (multi)polygons are authorized :
    
    ...
    geomtype : ["Point", "MultiPoint", "Polygon", "MultiPolygon"]
    ...

### `crs`
The spatial reference system to consider the data with.

Examples : 

- `EPSG:4326`
- `IGNF:LAMB93`

Must be readable by PROJ4 library

### Constraints

#### `unique`
If `true`, then geometries must be unique

#### `bounds`
Specifies `xmin`, `ymin`, `xmax`, `ymax` bounds for the data.

Example :
       
       ...
       "bounds": [4.9283, 43.0756, 7.6412, 45.0923]
       ...

> TODO : Consider a polygon as boundary of the data ?

#### `overlaps`
If `true`, then two geometries can overlap. It can be :

- two neighboring polygons
- two lines that cross
- a point contained in a polygon

#### `gaps`
Gaps are one of the topological errors for polygons, besides overlaps. It's a property only callable for polygons.

If `true`, then two polygons can have a gap between them.