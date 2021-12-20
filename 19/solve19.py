# Idéias:

# Criar função de rotação, armazenar todas as versões rotacionadas de beacons visíveis
# Fazer uma função de correlação entre listas de beacons de diferentes scanners
# Pensar numa ordenação que faça sentido para as listas de beacons

raw_data = open("input19.txt").readlines()

scanner_list = []

s_index = -1
b_list = None
for r in raw_data:
    if( r.find("scanner") > 0 ):
        if( b_list != None ):
            scanner_list.append(b_list)
        b_list = []
    elif( r.find(",") > 0 ):
        b_list.append ([int(c) for c in r.split(",")])

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