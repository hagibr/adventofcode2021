input6 = open("input6.txt").readline().split(",")

# A gente precisa saber qual era o estado inicial.
count0 = input6.count("0")
count1 = input6.count("1")
count2 = input6.count("2")
count3 = input6.count("3")
count4 = input6.count("4")
count5 = input6.count("5")
count6 = input6.count("6")
count7 = input6.count("7")
count8 = input6.count("8")

# Na verdade, só tem peixes com timer de 1 a 5, como pode-se ver na impressão do estado inicial
print(count0,count1,count2,count3,count4,count5,count6,count7,count8,(count0+count1+count2+count3+count4+count5+count6+count7+count8))

# A gente só precisa saber quantos peixes existem com cada timer e aplicar a lógica de decrementos e reprodução 
for d in range(80): # 80 dias
    count00 = count0            # Isso aqui é só uma cópia dos peixes com timer 0
    count0 = count1             # Todos os peixes que tinham timer 1 agora tem timer 0
    count1 = count2             # Todos os peixes que tinham timer 2 agora tem timer 1
    count2 = count3             # Todos os peixes que tinham timer 3 agora tem timer 2
    count3 = count4             # Todos os peixes que tinham timer 4 agora tem timer 3
    count4 = count5             # Todos os peixes que tinham timer 5 agora tem timer 4
    count5 = count6             # Todos os peixes que tinham timer 6 agora tem timer 5
    count6 = count7 + count00   # Todos os peixes que tinham timer 7 ou 0 agora tem timer 6
    count7 = count8             # Todos os peixes que tinham timer 8 agora tem timer 7
    count8 = count00            # Todos os peixes que tinham timer 0 geraram novos peixes com timer 8

# Pronto, agora é só imprimir a quantidade final de peixes com cada timer
print(count0,count1,count2,count3,count4,count5,count6,count7,count8,(count0+count1+count2+count3+count4+count5+count6+count7+count8))