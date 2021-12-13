input_data = [l.replace("\n","") for l in open("input13.txt").readlines()]

# Exemplo
# input_data = '''
# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5
# '''.splitlines()

print(input_data)

# Vamos fazer um parsing básico, preenchendo as 2 listas
dots = []
folds = []
for d in input_data:
    if( len(d) != 0 ):
        if( d.startswith("fold along y=")):
            folds.append(['y',int(d.replace("fold along y=",""))])
        elif( d.startswith("fold along x=")):
            folds.append(['x',int(d.replace("fold along x=",""))])
        else:
            xy = d.split(",")
            dots.append([int(xy[0]), int(xy[1])])

print(dots)
print(folds)

# Algoritmo de dobra(s)
for f in folds:
    to_remove = [] # Lista dos pontos a remover
    if( f[0] == 'y' ): # Dobra horizontal
        yfold = f[1]
        for d in range(len(dots)):
            x,y = dots[d]
            # Todos os pontos com coordenada y maior que a posição da dobra
            if( y > yfold ):
                diff = y-yfold
                # Serão espelhados em relação à posição da dobra
                newpos = [x,yfold-diff]
                # Se não tinha antes algo lá, vamos colocar
                if( not newpos in dots ):
                    dots.append(newpos)
                # E marca este ponto para remoção
                to_remove.append(dots[d])
    elif( f[0] == 'x' ): # Dobra vertical
        xfold = f[1]
        for d in range(len(dots)):
            x,y = dots[d]
            # Todos os pontos com coordenada x maior que a posição da dobra
            if( x > xfold ):
                diff = x-xfold
                # Serão espelhados em relação à posição da dobra
                newpos = [xfold-diff,y]
                # Se não tinha antes algo lá, vamos colocar
                if( not newpos in dots ):
                    dots.append(newpos)
                # E marca este ponto para remoção
                to_remove.append(dots[d])
    # Agora pode remover
    for tr in to_remove:
        dots.remove(tr)
   
print(dots)
print(len(dots))

# Avaliando valores mínimos e máximos
minX, maxX, minY, maxY = None, None, None, None
for d in dots:
    if( minX == None or d[0] < minX ):
        minX = d[0]
    if( maxX == None or d[0] > maxX ):
        maxX = d[0]
    if( minY == None or d[1] < minY ):
        minY = d[1]
    if( maxY == None or d[1] > maxY ):
        maxY = d[1]

print(minX,maxX,minY,maxY)

# Imprimindo manual dobrado
for y in range(minY, maxY-minY+1):
    for x in range(minX, maxX-minX+1):
        if( [x,y] in dots ):
            print("#",end="")
        else:
            print(".",end="")
    print()