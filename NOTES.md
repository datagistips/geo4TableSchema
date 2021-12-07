## Spatial Data Package
https://github.com/cividi/spatial-data-package

https://github.com/cividi/spatial-data-package/discussions

https://specs.frictionlessdata.io/data-package/

## Geojson

https://frictionless-hackathon.herokuapp.com/project/9

https://pypi.org/project/frictionless-geojson/

https://github.com/cividi/frictionless-geojson

## RFC
https://www.rfc-editor.org/rfc/rfc7946

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