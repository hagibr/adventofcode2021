input8 = open("input8.txt").readlines()

result = 0

for line in input8:
    # Primeiro vamos separar a parte de símbolos e a parte dos valores
    (symbols, values) = line.split(" | ")
    
    # Agora, vamos descobrir quais são os símbolos para 1, 4, 7 e 8:
    symbols = symbols.strip().split(" ")

    print( symbols )
    s0 = s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = None

    # Essa parte é facil, basta contar quantos segmentos temos
    for s in symbols:
        if( len(s) == 2 ):
            s1 = s
        elif( len(s) == 4 ):
            s4 = s
        elif( len(s) == 3 ):
            s7 = s
        elif( len(s) == 7 ):
            s8 = s
    
    # Agora vem a análise de qual segmento é qual

    #     0:      1:      2:      3:      4:
    #  aaaa    ....    aaaa    aaaa    ....
    # b    c  .    c  .    c  .    c  b    c
    # b    c  .    c  .    c  .    c  b    c
    # ....    ....    dddd    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f
    # e    f  .    f  e    .  .    f  .    f
    #  gggg    ....    gggg    gggg    ....

    # 5:      6:      7:      8:      9:
    #  aaaa    aaaa    aaaa    aaaa    aaaa
    # b    .  b    .  .    c  b    c  b    c
    # b    .  b    .  .    c  b    c  b    c
    #  dddd    dddd    ....    dddd    dddd
    # .    f  e    f  .    f  e    f  .    f
    # .    f  e    f  .    f  e    f  .    f
    #  gggg    gggg    ....    gggg    gggg

    # Sabendo que os dígitos 1 e 7 compartilham os segumentos 'c' e 'f', podemos descobrir qual é o segmento 'a'
    symbols.remove(s1)
    symbols.remove(s4)
    symbols.remove(s7)
    symbols.remove(s8)

    # Sobraram:
    # 0: 6 segmentos
    # 2: 5 segmentos
    # 3: 5 segmentos
    # 5: 5 segmentos
    # 6: 6 segmentos
    # 9: 6 segmentos
    
    print(symbols)
    for s in symbols:
        # 6 segmentos: 0, 6 ou 9
        if( len(s) == 6 ):
            match4 = 0
            for p in s4:
                if( s.find(p) >= 0 ):
                    match4 += 1
            # Dos de 6 segmentos, o 9 é o único que contém os 4 segmentos do 7
            if( match4 == 4 ):
                s9 = s
            # Sobram o 0 e o 6
            else:
                match1 = 0
                for p in s1:
                    if( s.find(p) >=0 ):
                        match1 += 1
                # Dos de 6 segmentos, o único que contém somente 1 segmento do 1 é o 6
                if( match1 == 1 ):
                    s6 = s
                # Caso contrário, só pode ser o 0
                else:
                    s0 = s

    symbols.remove(s0)
    symbols.remove(s6)
    symbols.remove(s9)
    
    print(symbols)
    # só sobraram os de 5 segmentos: 2, 3 ou 5
    for s in symbols:
        match1 = 0
        for p in s1:
            if( s.find(p) >= 0 ):
                match1 += 1
        # Dos de 5 segmentos, o único que contém os 2 segmentos do 1 é o 3
        if( match1 == 2 ):
            s3 = s
        # Sobraram o 2 e o 5
        else:
            match6 = 0
            for p in s6:
                if( s.find(p) >= 0 ):
                    match6 += 1
            # Todos os segmentos do 5 estão no 6
            if( match6 == 5 ):
                s5 = s
            # Caso contrário, só pode ser o 2
            else:
                s2 = s
    
    print(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9) # Conferência
    
    # Agora vamos descobrir qual é o número exibido. Separando os 4 dígitos....
    values = values.strip().split(" ")
    print(values)
    
    # Vamos usar este mapa de valores para facilitar a vida
    vmap = {s0:0,s1:1,s2:2,s3:3,s4:4,s5:5,s6:6,s7:7,s8:8,s9:9}
    
    # A parte chata é que os segmentos dos 4 dígitos não batem a ordem com o mapa. Mas vamos lá...
    entry = 0
    for v in values:
        for k in vmap:
            if( len(k) == len(v) ):
                count = 0
                for d in k:
                    if( d in v ):
                        count += 1
                if( count == len(k) ):
                    print(k, vmap[k])
                    entry = 10*entry+vmap[k]
                    break
    
    print(entry)
    result += entry


print(result)
