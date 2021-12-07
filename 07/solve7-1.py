input7 = open("input7.txt").readline().split(",")

crabpos = [int(c) for c in input7]

minpos = min(crabpos)
maxpos = max(crabpos)
# print( minpos, maxpos ) # Conferindo valores mínimo e máximo de posições dos caranguejos

# Esta é a maior distância entre caranguejos
maxdist = maxpos-minpos

# Inicializando com valores absurdos
pos = -1
minfuel = maxdist*len(crabpos)

# Abordagem força bruta: passa por todas as posições
for p in range(len(crabpos)):
    sum = 0
    for c in crabpos:
        # Acumula distâncias
        sum += abs(c - p)
        # Se a soma já ultrapassou algum valor mínimo anterior, já paramos por aqui
        if( sum > minfuel ):
            sum = maxdist*len(crabpos)
            break
    # Se for menor que a soma anterior, marca valor da soma e posição
    if( sum < minfuel ):
        minfuel = sum
        pos = p

print(pos, minfuel)