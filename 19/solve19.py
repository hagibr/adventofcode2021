# Idéias:

# Criar função de rotação, armazenar todas as versões rotacionadas de beacons visíveis
# Fazer uma função de correlação entre listas de beacons de diferentes scanners
# Pensar numa ordenação que faça sentido para as listas de beacons

raw_data = open("input19.txt").readlines()

scanner_list = []

s_index = -1
b_list = None
refscanner = None
for r in raw_data:
    if( r.find("scanner") > 0 ):
        if( b_list != None ):
            # Separando primeiro scanner do restante da lista
            if( refscanner == None ):
                refscanner = b_list
            else:
                scanner_list.append(b_list)
        b_list = []
    elif( r.find(",") > 0 ):
        b_list.append ([int(c) for c in r.split(",")])

# É preciso adicionar a lista do último scanner na lista    
scanner_list.append(b_list)

# Vou manter o scanner 0 como referência, e usar o seguinte algoritmo:
# - Escolhe um scanner A da lista, A não pode ser 0
# - Seleciona um beacon B na lista do scanner A
# - Simula a perspectiva deste beacon, coloca ela no centro de coordenadas
# - Para todo beacon C do scanner 0, também coloca no centro de coordenadas
# - Compara todos os beacons que deveriam ser visíveis tanto por A quanto por C
# - Se estes beacons baterem em uma das 6 orientações possíveis, encontramos um ponto de sobreposição.
#   - Adiciona todos os beacons do scanner A na lista do scanner 0 (corrigindo a orientação) e remove o scanner A da lista
# - Se nenhum beacon der certo, então coloca o scanner A no final da lista e vai pro próximo

# Análise inicial: são 39 scanners, então faremos a análise comparando 38 deles com o primeiro
# Cada scanner possui entre 25 e 27 beacons. 39 x 27 = 1053 (tem menos, é claro)
# Não é difícil fazer a correção do centro, a delimitação dos limites nem a reorientação para

# Função que pega um beacon específico da lista de beacon de um scanner e retorna
# a lista de beacons deste scanner do ponto de vista do beacon específico
def beacon_view(beacon, scanner):
    view = []
    for b in scanner:
        # Apenas ignoramos o próprio beacon específico
        if( b != beacon ):
            # É basicamente um offset no sistema de coordenadas, usando as coordenadas x,y,z do
            # beacon específico como ponto central
            view.append([b[0]-beacon[0],b[1]-beacon[1],b[2]-beacon[2]])

    return view
            
# Retorna as 24 rotações possíveis
def beacon_view_rotate(view):
    rotations = []
    rotations.append(view)                                #  x, y, z
    rotations.append([[ d[0],-d[2], d[1]] for d in view]) #  x,-z, y
    rotations.append([[ d[0],-d[1],-d[2]] for d in view]) #  x,-y,-z
    rotations.append([[ d[0], d[2],-d[1]] for d in view]) #  x, z,-y

    rotations.append([[ d[1], d[2], d[0]] for d in view]) #  y, z, x
    rotations.append([[ d[1],-d[0], d[2]] for d in view]) #  y,-x, z
    rotations.append([[ d[1],-d[2],-d[0]] for d in view]) #  y,-z,-x
    rotations.append([[ d[1], d[0],-d[2]] for d in view]) #  y, x,-z
    
    rotations.append([[ d[2], d[0], d[1]] for d in view]) #  z, x, y
    rotations.append([[ d[2],-d[1], d[0]] for d in view]) #  z,-y, x
    rotations.append([[ d[2],-d[0],-d[1]] for d in view]) #  z,-x,-y
    rotations.append([[ d[2], d[1],-d[0]] for d in view]) #  z, y,-x
    
    rotations.append([[-d[0],-d[1], d[2]] for d in view]) # -x,-y, z
    rotations.append([[-d[0],-d[2],-d[1]] for d in view]) # -x,-z,-y
    rotations.append([[-d[0], d[1],-d[2]] for d in view]) # -x, y,-z
    rotations.append([[-d[0], d[2], d[1]] for d in view]) # -x, z, y
    
    rotations.append([[-d[1],-d[2], d[0]] for d in view]) # -y,-z, x
    rotations.append([[-d[1],-d[0],-d[2]] for d in view]) # -y,-x,-z
    rotations.append([[-d[1], d[2],-d[0]] for d in view]) # -y, z,-x
    rotations.append([[-d[1],-d[0], d[2]] for d in view]) # -y,-x, z

    rotations.append([[-d[2],-d[0], d[1]] for d in view]) # -z,-x, y
    rotations.append([[-d[2],-d[1],-d[0]] for d in view]) # -z,-y,-x
    rotations.append([[-d[2], d[0],-d[1]] for d in view]) # -z, x,-y
    rotations.append([[-d[2], d[1], d[0]] for d in view]) # -z, y, x
    
    return rotations

def beacon_get_min_max(view):
    minx = maxx = view[0][0]
    miny = maxy = view[0][1]
    minz = maxz = view[0][2]
    for v in view:
        if( v[0] > maxx ):
            maxx = v[0]
        elif( v[0] < minx ):
            minx = v[0]
        if( v[1] > maxy ):
            maxy = v[1]
        elif( v[1] < miny ):
            miny = v[1]
        if( v[2] > maxz ):
            maxz = v[2]
        elif( v[2] < minz ):
            minz = v[2]
    return [minx,maxx,miny,maxy,minz,maxz]
        
# Loop de trabalho. Precisamos limpar todos os scanners
while( len( scanner_list ) > 0 ):
    scanner = scanner_list[0]
    for beacon in scanner:
        # Pega a visão deste beacon usando a referência inicial dele
        beacon_view_0 = beacon_view(beacon, scanner)
        # Gera as 24 rotações deste beacon
        beacon_views = beacon_view_rotate(beacon_view_0)
        for bview in beacon_views:
            minmax_b = beacon_get_min_max(bview)
            # Compara a visão deste beacon com as visões dos beacons vistos pelo scanner de referência
            for bref in refscanner:
                bref_view_0 = beacon_view(bref, refscanner)
                minmax_ref = beacon_get_min_max(bref_view_0)
                # Primeiro vamos encontrar a interseção dos 2 cubos
                minmax_common = [max(minmax_b[0],minmax_ref[0]), min(minmax_b[1],minmax_ref[1]),
                                 max(minmax_b[2],minmax_ref[2]), min(minmax_b[3],minmax_ref[3]),
                                 max(minmax_b[4],minmax_ref[4]), min(minmax_b[5],minmax_ref[5])]
                # Agora vamos verificar se todos os beacons nessa interseção batem e precisamos
                # também que se tenha pelo menos 3 beacons
                nomatch = False
                matchcount = 0
                for b in bref:
                    if( b[0] >= minmax_common[0] and b[0] <= minmax_common[1] and
                        b[1] >= minmax_common[2] and b[1] <= minmax_common[3] and
                        b[2] >= minmax_common[4] and b[2] <= minmax_common[5] ):
                        
                        if( b in bview ):
                            matchcount += 1
                        else:
                            nomatch = True
                            break
                
                # Parece que encontrou uma equivalência aqui
                if( not nomatch and matchcount >= 3 ):
                    # TODO: pegar a lista de beacons atuais, fazer a rotação e colocar na lista bref
                    print("match")