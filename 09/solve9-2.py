input9 = open("input9.txt").readlines()

# Excluindo o '\n' no final da linha para contagem de colunas
nrows = len(input9)
ncolumns = len(input9[0])-1

clusters = {}

# Criando clusters para todos os pontos que não são 9
for r in range(nrows):
    for c in range(ncolumns):
        if( input9[r][c] != '9' ):
            clusters[(r,c)] = [r,c]

# Agrupando clusters. Fazendo varredura por linhas.
while(True):
    changes = 0
    for r in range(nrows):
        for c in range(ncolumns):
            # Testa se existe cluster para a posição atual e para a posição à esquerda
            if( c > 0 and input9[r][c] != '9' and input9[r][c-1] != '9' ):
                # Testa se são clusters diferentes
                if( clusters[(r,c)] != clusters[(r,c-1)] ):
                    # Agrupa
                    clusters[(r,c)] = clusters[(r,c-1)]
                    changes += 1

            if( r > 0 and input9[r][c] != '9' and input9[r-1][c] != '9' ):
                # Testa se são clusters diferentes
                if( clusters[(r,c)] != clusters[(r-1,c)] ):
                    # Agrupa
                    clusters[(r,c)] = clusters[(r-1,c)]
                    changes += 1

    for c in range(ncolumns):
        for r in range(nrows):
            # Testa se existe cluster para a posição atual e para a posição à esquerda
            if( c > 0 and input9[r][c] != '9' and input9[r][c-1] != '9' ):
                # Testa se são clusters diferentes
                if( clusters[(r,c)] != clusters[(r,c-1)] ):
                    # Agrupa
                    clusters[(r,c)] = clusters[(r,c-1)]
                    changes += 1

            if( r > 0 and input9[r][c] != '9' and input9[r-1][c] != '9' ):
                # Testa se são clusters diferentes
                if( clusters[(r,c)] != clusters[(r-1,c)] ):
                    # Agrupa
                    clusters[(r,c)] = clusters[(r-1,c)]
                    changes += 1


    if( changes == 0 ):
        break

# Agora todos os clusters estão agrupados
print(clusters)

counters = {}
unique = []
for c in clusters:
    if( not clusters[c] in unique ):
        unique.append(clusters[c])
        counters[tuple(clusters[c])] = 1
    else:
        counters[tuple(clusters[c])] += 1

print(counters)
# print(unique)
# print(len(unique))