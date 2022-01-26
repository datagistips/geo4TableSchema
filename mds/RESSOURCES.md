# Resources

## validate

https://github.com/frictionlessdata/frictionless-py

https://github.com/frictionlessdata/frictionless-py/blob/main/CONTRIBUTING.md

## geopandas

- is_ring
- is_simple
- is_empty
- geom_equals
- geom_almost_equals
- geom_equals_exact

## JSON Schema

<https://json-schema.org/>

## Templates

<https://github.com/etalab/tableschema-template/blob/master/schema.json>

## TableSchema

- <https://specs.frictionlessdata.io/table-schema/>

## Spatial Data Package

- <https://github.com/cividi/spatial-data-package>
- <https://github.com/cividi/spatial-data-package/discussions>
- <https://specs.frictionlessdata.io/data-package/>

## Data package

- https://specs.frictionlessdata.io/data-package/

## Geojson

- https://frictionless-hackathon.herokuapp.com/project/9
- https://pypi.org/project/frictionless-geojson/
- https://github.com/cividi/frictionless-geojson

### WGS84
- https://datatracker.ietf.org/doc/html/rfc7946#appendix-B.1

## RFC GeoJSON

https://www.rfc-editor.org/rfc/rfc7946

## Spatial issues

- https://github.com/frictionlessdata/specs/issues?q=spatial
- https://github.com/henrykironde/spatial-packages
- https://github.com/frictionlessdata/specs/issues/499
- https://github.com/frictionlessdata/specs/issues/86#issuecomment-318976645

## GeoCSV

https://giswiki.hsr.ch/GeoCSV

## Autres

https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
https://fr.wikipedia.org/wiki/GeoJSON

## PROJ

https://proj.org/

## Schema et attributs en plus

https://github.com/etalab/schema.data.gouv.fr/blob/master/aggregateur/data/NaturalSolutions/schema-arbre/0.2.0/schema.json#L284

Pareil pour geometry

## Geojson

    {
       "type":"FeatureCollection",
       "name":"geodata",
       "crs":{
          "type":"name",
          "properties":{
             "name":"urn:ogc:def:crs:EPSG::3857"
          }
       },
       "features":[
          {
             "type":"Feature",
             "properties":{
                "fid":1
             },
             "geometry":{
                "type":"Point",
                "coordinates":[
                   596916.502326328773052,
                   5436863.327570304274559
                ]
             }
          },
          {
             "type":"Feature",
             "properties":{
                "fid":2
             },
             "geometry":{
                "type":"Point",
                "coordinates":[
                   661123.960107152001001,
                   5427157.549068551510572
                ]
             }
          }
       ]
    }

## GeometryCollection

https://stackoverflow.com/questions/34044893/how-to-make-a-geometrycollection-in-geojson-with-a-single-point-polygon

## Notes

- rfc
- que wgs84
- geojson
- bbox
- left hand right hand
- left hand rule
- geojson rewind
- holes
