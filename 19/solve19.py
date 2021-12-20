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
    rotations.append(view)                              # x,y,z
    rotations.append([[d[0],-d[2],d[1]] for d in view]) # x,-z,y
    rotations.append([[d[0],-d[1],-d[2]] for d in view])# x,-y,-z
    rotations.append([[d[0],d[2],-d[1]] for d in view]) # x,z,-7

    rotations.append([[d[1],d[2],d[0]] for d in view])  # y,z,x
    rotations.append([[d[1],-d[0],d[2]] for d in view]) # y,-x,z
    rotations.append([[d[1],-d[2],-d[0]] for d in view])# y,-z,-x
    rotations.append([[d[1],d[0],-d[2]] for d in view]) # y,x,-z
    
    rotations.append([[d[2],d[0],d[1]] for d in view])  # z,x,y
    rotations.append([[d[2],-d[1],d[0]] for d in view]) # z,-y,x
    rotations.append([[d[2],-d[0],-d[1]] for d in view])# z,-x,-y
    rotations.append([[d[2],d[1],-d[0]] for d in view]) # z,y,-x
    

# Loop de trabalho. Precisamos limpar todos os scanners
while( len( scanner_list ) > 0 ):
    scanner = scanner_list[0]
    for beacon in scanner:
        beacon_view_0 = beacon_view(beacon, scanner)
