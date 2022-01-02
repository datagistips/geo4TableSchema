nRows = 11
emptyGeomRows = [3, 10]

# Maps initial data frame with filtered data frame
def getMapping(nRows, emptyGeomRows):
    d = dict()
    j = 0
    for i in range(nRows):
        if i in emptyGeomRows:
            d[i] = None
        else:
            d[i] = j
            j += 1

    return(d)
    
res = getMapping(nRows, emptyGeomRows)
print(res)

for elt in res:
    print(elt)
