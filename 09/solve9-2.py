input9 = open("input9.txt").readlines()
# input9 = open("example9.txt").readlines()


# Excluindo o '\n' no final da linha para contagem de colunas
nrows = len(input9)
ncolumns = len(input9[0])-1

clusters = {}
for r in range(nrows):
    for c in range(ncolumns):
        clusters[(r,c)] = [(r,c)]

while(True):
    changes = 0
    for r in range(nrows):
        for c in range(ncolumns):
            if( r > 0 and input9[r][c] != '9' and input9[r-1][c] != '9' ):
                for e in clusters[(r-1,c)]:
                    if( not e in clusters[(r,c)] ):
                        clusters[(r,c)].append(e)
                        changes += 1
                clusters[(r-1,c)] = clusters[(r,c)]

            if( r < (nrows-1) and input9[r][c] != '9' and input9[r+1][c] != '9' ):
                for e in clusters[(r+1,c)]:
                    if( not e in clusters[(r,c)] ):
                        clusters[(r,c)].append(e)
                        changes += 1
                clusters[(r+1,c)] = clusters[(r,c)]
                
            if( c > 0 and input9[r][c] != '9' and input9[r][c-1] != '9' ):
                for e in clusters[(r,c-1)]:
                    if( not e in clusters[(r,c)] ):
                        clusters[(r,c)].append(e)
                        changes += 1
                clusters[(r,c-1)] = clusters[(r,c)]
            
            if( c < (ncolumns-1) and input9[r][c] != '9' and input9[r][c+1] != '9' ):
                for e in clusters[(r,c+1)]:
                    if( not e in clusters[(r,c)] ):
                        clusters[(r,c)].append(e)
                        changes += 1
                clusters[(r,c+1)] = clusters[(r,c)]
    if( changes == 0 ):
        break        
print(len(clusters))


size1 = 0
size2 = 0
size3 = 0
cluster1 = None
cluster2 = None
cluster3 = None

uniqueclusters = []

for c in clusters:
    clusters[c].sort()
    if( not clusters[c] in uniqueclusters ):
        uniqueclusters.append(clusters[c])

print(uniqueclusters)
print(len(uniqueclusters))

for c in uniqueclusters:
    lenc = len(c)
    if( lenc >= size1 ):
        size3 = size2
        cluster3 = cluster2
        size2 = size1
        cluster2 = cluster1
        size1 = lenc
        cluster1 = c
    elif( lenc > size2 ):
        size3 = size2
        cluster3 = cluster2
        size2 = lenc
        cluster2 = c
    elif( lenc > size3 ):
        size3 = lenc
        cluster3 = c

print(cluster1)
print(cluster2)
print(cluster3)

print(size1,size2,size3,size1*size2*size3)