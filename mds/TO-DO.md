### Janvier 2022
- [ ] Documentation de référence sur wiki
- [x] Contrôler l'existence de la variable de type wkt à partir de son nom
- [ ] Mettre le nom du schéma
- [ ] minLength
- [ ] increment

### Pre
- [ ] Rapport en json et xml
- [ ] geometry, format = geojson ou wkt
- [x] Area too small
- [ ] Multiple geometries allowed
- [x] If multipolygon, polygon ok
- [ ] `wkt` type & GeoCSV
- [ ] Alléger le schéma
- [ ] snake case
- [ ] jupyter
- [x] Polygon vertexes bounds
- [ ] is_empty

		# https://gis.stackexchange.com/questions/168954/what-does-empty-mean-in-wkt?noredirect=1&lq=1
		POLYGON(EMPTY, (0 0, 0 1, 1 1, 1 0, 0 0)) 

- voir exemple de schéma par etalab
- [x] test multiples > Annulé
- [x] Messages d'erreur type frictionless > messages au style personnel
- [x] Use specific names. Rename geometry column to _geom if _geom does not exist
- [x] schema.json
- [x] voir les schémas pour geojson > pas pris en compte
- [x] contrôler l'existence de la colonne géométrique
- [x] bounds of a polygon
- [x] CRS
- [x] required : Tests if geometry exists
- [ ] additional constraints ? holes, min and max inter distances between points etc...
- [x] valid and invalid data
- [x] utiliser CSV et geojson
- [x] utiliser CSV et geowkt

## Not sure to implement this ?
- [ ] script exécutable avec donnée et schéma en entrée
- [ ] Indicate accuracy horizontale and verticale
- [ ] Indicate scaleRange : [1:100000, 1:10000]
- [ ] Indicate scaleZoom : [1, 15]
- [ ] Fonction pour créer le CSV temporaire
- [ ] holes
- [ ] Inter-table checks
