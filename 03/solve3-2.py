input3 = open("input3.txt").readlines()

# São valores de 12 bits
counters = [0]*12

# Varre por elas e conta os bits 1 em cada casa
for i in range(len(input3)):
    for j in range(12):
        if( input3[i][j] == '1'):
            counters[j] += 1

gamma = 0
epsilon = 0
for k in range(12):
    # Maioria é 1
    if( counters[k] > len(input3)/2 ):
        gamma = (gamma << 1) | 1
        epsilon = (epsilon << 1) | 0
    # Maioria é 0
    else:
        gamma = (gamma << 1) | 0
        epsilon = (epsilon << 1) | 1

# Vamos fazer da forma mais simples. Primeiro fazemos 2 cópias da lista inteira
oxigen = input3.copy()
scrubber = input3.copy()

# Agora analizamos bit a bit. Primeiro para o oxigen.
for k in range(12):
    count0 = 0
    count1 = 0
    # Contagem de bits 1 e bits 0
    for ox in oxigen:
        if( ox[k] == '1' ):
            count1 += 1
        else:
            count0 += 1
    # print(f"{k},{count0},{count1}")
    # Remover direto da lista no loop não deu certo em Python, então vamos criar uma lista de itens a remove
    ox_remove = []
    # E usamos os critérios de maioria/minoria para colocar na lista de remoção
    for ox in oxigen:
        if( count0 > count1 ):
            if( ox[k] == '1' ):
                ox_remove.append(ox)
        elif( count0 < count1 ):
            if( ox[k] == '0' ):
                ox_remove.append(ox)
        else:
            if( ox[k] == '0' ):
                ox_remove.append(ox)
        # Critério de parada: só vai restar 1 elemento na lista
        if( len(oxigen) - len(ox_remove) == 1 ):
            break
    
    # Agora faz a remoção em si dos itens da lista
    for ox in ox_remove:
        oxigen.remove(ox)

    # Critério de parada: só tem 1 elemento restante
    if( len(oxigen) == 1 ):
        break

# Mesma análise para o scribber
for k in range(12):
    count0 = 0
    count1 = 0
    for sc in scrubber:
        if( sc[k] == '1' ):
            count1 += 1
        else:
            count0 += 1
    # print(f"{k},{count0},{count1}")
    sc_remove = []

    # Aqui só invertemos a lógica minoria/maioria
    for sc in scrubber:
        if( count0 < count1 ):
            if( sc[k] == '1' ):
                sc_remove.append(sc)
        elif( count0 > count1 ):
            if( sc[k] == '0' ):
                sc_remove.append(sc)
        else:
            if( sc[k] == '1' ):
                sc_remove.append(sc)
        if( len(scrubber) - len(sc_remove) == 1 ):
            break
    
    for sc in sc_remove:
        scrubber.remove(sc)
    if( len(scrubber) == 1 ):
        break

# Conferência: só pode ter 1 elemento em cada lista    
print(oxigen)
print(scrubber)

# Parsing e multiplicação
oxigen = int(oxigen[0],2)
scrubber = int(scrubber[0],2)
print(f"{oxigen},{scrubber},{oxigen*scrubber}")