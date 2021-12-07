input4 = open("input4.txt").readlines()

# A sequência está na 1ª linha
sequence = input4[0].strip().replace("  ", " ").replace("\n", "").split(",")

# As cartelas ocupam cada uma 6 linhas a partir da 2ª linha
n_cards = int( (len(input4)-1)/6 )

print(f"cards: {n_cards}")

# Inicializando lista de cartelas
cards = []
for i in range(n_cards):
    cards.append([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])

# Parsing das cartelas
for n in range(n_cards):
    for r in range(5):
        row = input4[2 + 6*n+r].strip().replace("  "," ").split(" ")
        # print(row)
        for c in range(5):
            cards[n][r][c] = int(row[c])

# Vai saindo a sequência sorteada
for s in sequence:
    value = int(s)
    print(f"{value}")
    bingo = False
    # Varre todas as cartas
    for n in range(n_cards):
        marked = False
        for r in range(5):
            for c in range(5):
                if( cards[n][r][c] == value ):
                    cards[n][r][c] = -1
                    marked = True
                    break
            if( marked ):
                break
        # Só tem chance de ter dado bingo quando marcamos uma posição na cartela
        if( marked ):
            bingo = False
            sumr = 0
            sumc = 0
            # Analiza linha a linha
            for r in range(5):
                sumc = 0
                for c in range(5):
                    if( cards[n][r][c] == -1 ):
                        sumc += 1
                if( sumc == 5 ):
                    break
            # Analiza coluna a coluna
            if( sumc < 5 ):
                for c in range(5):
                    sumr = 0
                    for r in range(5):
                        if( cards[n][r][c] == -1 ):
                            sumr += 1
                    if( sumr == 5 ):
                        break
            
            # Deu bingo?
            if( sumc == 5 or sumr == 5 ):
                bingo = True
                
                # Calcula a soma da cartela
                sumcard = 0
                for r in range(5):
                    for c in range(5):
                        if( cards[n][r][c] != -1 ):
                            sumcard += cards[n][r][c]

                # Imprime os valores
                print(cards[n])
                print(f'{n},{value},{sumcard},{value*sumcard}')
                print()
                break
    
    # Se deu bingo, pode parar de sair valores da sequência
    if( bingo ):
        break                
    