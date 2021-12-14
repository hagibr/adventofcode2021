# Dados de exemplo. Precisa usar 4 passos para conferir se a cadeia resultante faz sentido e 
# 10 passos para conferir se a quantidade final de elementos está correta

# data = '''NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''.splitlines()

data = [d.replace("\n","") for d in open("input14.txt").readlines()]

# Lista da cadeia atual XYZW... -> XY, YZ, ZW, ...
chain_list = {}
# Lista de regras XY -> Z quer irão mapear para 2 pares: XY -> (XZ,ZY)
poly_rules = {}
for d in data:
    if(len(d) != 0):
        if(not ' -> ' in d):
            for i in range(len(d)-1):
                pair = d[i:i+2]
                if( pair in chain_list ):
                    chain_list[pair] += 1
                else:
                    chain_list[pair] = 1
        else:
            rule = d.split(' -> ')
            left = rule[0][0] + rule[1]
            right = rule[1] + rule[0][1]
            poly_rules[rule[0]] = (left,right)
            
print(chain_list)
print(poly_rules)

# É só mudar para 40 passos desta vez. O algoritmo escolhido ajudou bastante a escalabilidade.
for s in range(40):
    new_chain = {}
    # Varrendo cadeia atual
    for c in chain_list:
        pair = poly_rules[c]
        quantity = chain_list[c]
        # Os novos pares formarão a nova cadeia, cada par atual irá criar um de cada par
        if( pair[0] in new_chain ):
            new_chain[pair[0]] += quantity
        else:
            new_chain[pair[0]] = quantity
        if( pair[1] in new_chain ):
            new_chain[pair[1]] += quantity
        else:
            new_chain[pair[1]] = quantity

    # Agora a cadeia foi substituída   
    chain_list = new_chain
    print(chain_list)

# Somando a quantidade de elementos usando a quantidade de cada pares
elements = {}
for c in chain_list:
    left = c[0]
    right = c[1]
    quantity = chain_list[c]
    if( left in elements ):
        elements[left] += quantity
    else:
        elements[left] = quantity
    if( right in elements ):
        elements[right] += quantity
    else:
        elements[right] = quantity

max,min=None,None

# A gente somou dobrado, já que cada elemento está em 2 pares, com exceção das pontas que possuem somente 1 vez cada elemento
for e in elements:
    # Dividindo por 2, e consertando o que ocorre nas pontas
    elements[e] = (elements[e]+1)//2
    # Atualizando valores de máximo e mínimo
    if( max == None or elements[e] > max ):
        max = elements[e]
    if( min == None or elements[e] < min ):
        min = elements[e]

print(elements)
print(max,min,max-min)


