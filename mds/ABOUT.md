# spatial-schema

Here is an overview of specifications proposal for a `geompoint` spatial field :

    "fields":[
      {
         "name":"geompoint",
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

This proposal introduces :

- some **attributes** and **constraints** for `geojson`
- a new `geowkt` field type

---

## Spatial data

Geographical data can be of these types :

- **points** like location of elements or events in space
- **lines** like roads, borders
- **polygons** like urban planning zones, parcels

But you can not specify these types in Table Schema

### Attributes & constraints for spatial data

Spatial controls can concern :

- **geometry types** : _"are all my objects of type Point ?"_
- **coordinate reference system** assignment : _"are my points in WGS84 ?"_
- **bounds** of the data : _"are my points contained in a defined bounding box ?"_
- **unicity** of geometries : _"are my geometries unique ?"_

### Topology

- **overlaps** : _"do my polygons overlap ?"_
- **gaps** between polygons : _"are there gaps between my polygons ?"_
- **slivers**

---

## Examples

[See some examples](EXAMPLES.md)

---

## Reference

[Check reference documentation](REFERENCE.md)

---

## `geowkt`

[Proposal for a `geowkt` field](geowkt.md)
