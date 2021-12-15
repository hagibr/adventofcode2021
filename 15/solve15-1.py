strdata = [line.replace("\n","") for line in open("input15.txt").readlines()]

# print(strdata)

data = []
for line in strdata:
    data_line = [int(v) for v in line]
    data.append(data_line)

nrows = len(data)
ncols = len(data[0])

# print(data)

# Criando mapa de distâncias e conjunto de nós, onde colocaremos informação de nó anterior e menor distância acumulada
neighbor_set = {}
for r in range(nrows):
    for c in range(ncols):
        neighbors = []
        if( r > 0 ): # Adicionando vizinho de cima
            if( (r-1,c) != (0,0) and (r,c) != (nrows-1,ncols-1) ): # Não se pode retornar para ponto inicial e nem pode retornar do ponto final
                neighbors.append((r-1,c,data[r-1][c]))
        if( r < nrows-1 ): # Adicionando vizinho de baixo
            neighbors.append((r+1,c,data[r+1][c]))
        if( c > 0 ): # Adicionando vizinho da esquerda
            if( (r,c-1) != (0,0) and (r,c) != (nrows-1,ncols-1) ): # Não se pode retornar para ponto inicial e nem pode retornar do ponto final
                neighbors.append((r,c-1,data[r][c-1]))
        if( c < ncols-1 ): # Adicionando vizinho da direita
            neighbors.append((r,c+1,data[r][c+1]))
        neighbor_set[(r,c)] = neighbors

# print(neighbor_set)

# O que entendo do algoritmo:
# A gente parte do nó de origem e calcula o custo para ir para os nós vizinhos
# Colocamos esses nóz vizinhos na lista de "a visitar"
# Avaliamos sempre os nós da lista "a visitar" daquele com menor custo até o de maior custo
# Quando um nó vai adicionar outro na lista de "a visitar", se este nó já está na lista de "a visitar",
# avalia se o custo passando pelo nó atual será menor, e caso positivo, substitui na lista de "a visitar"

# O primeiro ponto a ser visitado é o ponto inicial
visited_set = {}
tovisit_set = {(0,0):[None,0]}
# O critério de parada é quando terminamos todos os nós
while(len(visited_set) < nrows*ncols):
    # Vamos pegar o nó com menor custo da lista de "a visitar"
    current_node = None
    for tv in tovisit_set:
        if( current_node == None or tovisit_set[tv][1] < tovisit_set[current_node][1] ):
            current_node = tv

    # Agora usa ele para adicionar os vizinhos dele na lista de "a visitar"
    neighbors = neighbor_set[current_node]
    current_cost = tovisit_set[current_node][1]
    for n in neighbors:
        node = (n[0],n[1])
        cost = n[2] + current_cost
        tovisit = [current_node, cost]
        # Não pode revisitar um nó já visitado
        if( not node in visited_set ):
            # Se o vizinho não estava na lista de "a visitar", adiciona agora
            if( not node in tovisit_set ):
                tovisit_set[node] = tovisit
            # Se ele estava na lista de "a visitar", apenas substitui se o custo vindo pelo atual é menor
            else:
                if( cost < tovisit_set[node][1] ):
                    tovisit_set[node] = tovisit
        
    # Agora tira o nó atual da lista de "a visitar" e coloca na lista de "visitados"
    visited_set[current_node] = tovisit_set[current_node]
    tovisit_set.pop(current_node)
    
    # Não precisa fazer mais caminhos quando chegamos no ponto final
    if( current_node == (nrows-1,ncols-1) ):
        break
    
# Dá pra ver a lista completa agora 
for v in visited_set:
    print(v, visited_set[v])
    
# Mas só estamos interessados no último deles
print(visited_set[(nrows-1,ncols-1)][1])
