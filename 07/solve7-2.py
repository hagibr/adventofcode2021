input7 = open("input7.txt").readline().split(",")

crabpos = [int(c) for c in input7]

minpos = min(crabpos)
maxpos = max(crabpos)
# print( minpos, maxpos ) # Conferindo valores mínimo e máximo de posições dos caranguejos

# Mudando o cálculo da "distância": vamos usar uma tabela
disttable = [0]*(maxpos+1)
d = 1
for i in range(1,maxpos+1):
    disttable[i] = disttable[i-1]+d
    d += 1
# print( disttable ) # Conferindo tabela de distância

# Esta é a maior distância entre caranguejos
maxdist = disttable[maxpos]

# Inicializando com valores absurdos
pos = -1
minfuel = len(crabpos)*maxdist

# Abordagem força bruta: passa por todas as posições
for p in range(len(crabpos)):
    sum = 0
    for c in crabpos:
        # Acumula "distâncias"
        sum += disttable[abs(c-p)]
        # Se a soma já ultrapassou algum valor mínimo anterior, já paramos por aqui
        if( sum > minfuel ):
            sum = len(crabpos)*maxdist
            break
    # Se for menor que a soma anterior, marca valor da soma e posição
    if( sum < minfuel ):
        minfuel = sum
        pos = p

print(pos, minfuel)