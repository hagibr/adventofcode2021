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

# Flag que indica se já deu bingo nesta cartela
bingo_list = [False]*n_cards
bingo_count = 0

# Precisamos armazenar a informação da última cartela que deu bingo
last_bingo = -1
last_value = -1
last_sumcard = -1

for i in range(len(sequence)):
    value = int(sequence[i])
    print(f"{value}")
    for n in range(n_cards):
        marked = False
        # Procura o valor na cartela
        for r in range(5):
            for c in range(5):
                if( cards[n][r][c] == value ):
                    cards[n][r][c] = -1
                    marked = True
                    break
            if( marked ):
                break
        # Se acabamos de marcar, vamos analizar se deu bingo (linhas ou colunas cheias), mas também vamos evitar
        # cartelas que já deram bingo antes
        if( marked and not bingo_list[n] ):
            bingo = False
            sumr = 0
            sumc = 0
            # Analizando linha a linha
            for r in range(5):
                sumc = 0
                for c in range(5):
                    if( cards[n][r][c] == -1 ):
                        sumc += 1
                if( sumc == 5 ):
                    break
            # Se não deu por linhas, vamos analizar coluna a coluna
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

                # Marca a flag
                bingo_list[n] = True
                bingo_count += 1
                print(f'b {bingo_count}')
                
                # Marca as informações da cartela
                last_bingo = n
                last_value = value
                
                # Calcula e armazena a última soma
                sumcard = 0
                for r in range(5):
                    for c in range(5):
                        if( cards[n][r][c] != -1 ):
                            sumcard += cards[n][r][c]

                last_sumcard = sumcard

# Agora varremos todas as possibilidades e podemos simplesmente exibir as informações da última cartela
print(f'{last_bingo},{last_value},{last_sumcard},{last_value*last_sumcard}')
print()

