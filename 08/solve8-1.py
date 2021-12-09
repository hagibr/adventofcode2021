input8 = open("input8.txt").readlines()

result = 0

for line in input8:
    # Primeiro vamos separar a parte de símbolos e a parte dos valores
    (symbols, values) = line.split(" | ")
    
    # Agora, vamos descobrir quais são os símbolos para 1, 4, 7 e 8:
    # symbols = symbols.strip().split(" ")

    # # Essa parte é facil, basta contar quantos segmentos temos
    # for s in symbols:
    #     if( len(s) == 2 ):
    #         s1 = s
    #     elif( len(s) == 4 ):
    #         s4 = s
    #     elif( len(s) == 3 ):
    #         s7 = s
    #     elif( len(s) == 7 ):
    #         s8 = s

    # Não precisamos saber qual símbolo é qual, basta lembrar que os dígitos 1, 4, 7 e 8 possuem
    # quantidades únicas de segmentos
    values = values.strip().split(" ")
    for v in values:
        lenv = len(v)
        if( lenv == 2 or lenv == 4 or lenv == 3 or lenv == 7 ):
            result += 1
    
print(result)