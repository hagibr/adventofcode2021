input5 = open("input5.txt").readlines()
# input5 = open("example5.txt").readlines()


# Tem que inicializar o grid assim, usando cópia caso contrário o Python usa referências aí avacalha tudo
grid = []
for i in range(1000):
    grid.append(([0]*1000).copy())

# grid = [[0]*1000]*1000
# Conferindo grid inicial
# print(grid)

# Parsing da entrada
for line in input5:
    x1,y1,x2,y2 = line.strip().replace(" -> ", ",").split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    print(x1,y1,x2,y2)
    
    # Validação
    # if( x1 != x2 and y1 != y2 ): # Se não for mesma linha ou coluna
    #     if( abs(x1-x2) != abs(y1-y2) ): # se não for diagonal de quadrado
    #         print(line)

    # Mesma linha
    if( x1 == x2 ):
        if( y1 < y2 ):
            for y in range(y1,y2+1):
                grid[x1][y] += 1
        else:
            for y in range(y2,y1+1):
                grid[x1][y] += 1
        print("mesma linha")
    # Mesma coluna
    elif( y1 == y2 ):
        if( x1 < x2 ):
            for x in range(x1,x2+1):
                grid[x][y1] += 1
        else:
            for x in range(x2,x1+1):
                grid[x][y1] += 1
        print("mesma coluna")
    # Diagonal
    # else:
    #     diff = abs(x1-x2)
    #     # x e y crescentes
    #     if( x1 < x2 and y1 < y2 ):
    #         for i in range( diff + 1 ):
    #             grid[x1+i][y1+i] += 1
    #     # x crescente, y decrescente
    #     elif( x1 < x2 and y1 > y2 ):
    #         for i in range( diff + 1 ):
    #             grid[x1+i][y1-i] += 1
    #     # x e y decrescentes
    #     elif( x1 > x2 and y1 > y2 ):
    #         for i in range( diff + 1 ):
    #             grid[x1-i][y1-i] += 1
    #     # x decrescente, y crescente
    #     elif( x1 > x2 and y1 < y2 ):
    #         for i in range( diff + 1 ):
    #             grid[x1-i][y1+i] += 1
    #     print("diagonal ", diff)

point = 0      
for i in range(1000):
    for j in range(1000):
        if( grid[i][j] > 1 ):                
            point += 1

# print(grid)

print(point)
    