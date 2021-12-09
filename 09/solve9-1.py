input9 = open("input9.txt").readlines()

# Excluindo o '\n' no final da linha para contagem de colunas
nrows = len(input9)
ncolumns = len(input9[0])-1

risk = 0
for r in range(nrows):
    for c in range(ncolumns):
        lowcount = 0
        
        if( r == 0 ):
            lowcount += 1
        elif( input9[r-1][c] > input9[r][c] ):
            lowcount += 1

        if( r == (nrows-1) ):
            lowcount += 1
        elif( input9[r+1][c] > input9[r][c] ):
            lowcount += 1

        if( c == 0 ):
            lowcount += 1
        elif( input9[r][c-1] > input9[r][c] ):
            lowcount += 1

        if( c == (ncolumns-1) ):
            lowcount += 1
        elif( input9[r][c+1] > input9[r][c] ):
            lowcount += 1

        if( lowcount == 4 ):
            risk += 1 + int(input9[r][c])
        
print(risk)