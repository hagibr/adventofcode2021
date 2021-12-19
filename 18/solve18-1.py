data = [l.replace("\n","") for l in open("input18.txt").readlines()]

# Vamos trabalhar somente com strings. Vai ser penoso, mas dá para avaliar cada função em separado

# Adição de 2 números: bem direto
def add(n1, n2):
    return "[" + n1 + "," + n2 + "]"

# Explosão de 2 números: esta função faz 1 explosão por vez
def explode(number):
    # Procurando o aninhamento mais interno de todos
    max_nest = 0
    pos_max_nest = -1
    count_nested = 0
    for i in range(len(number)):
        # Início de 1 aninhamento
        if( number[i] == '[' ):
            count_nested += 1
            # Marcando o aninhamento mais profundo de todos
            if( count_nested > max_nest ):
                pos_max_nest = i
                max_nest = count_nested
        # Final de 1 aninhamento
        elif( number[i] == ']' ):
            count_nested -= 1

    # Achou um aninhamento de pelo menos 4?
    if( max_nest >= 5 ):
        i = pos_max_nest
        # Vamos tentar achar os valores deste par
        left_right = None
        # Procura o fechamento do par...
        for j in (range(i+1, len(number))):
            # Achou fechamento do par
            if( number[j] == ']' ):
                # Separando o par
                inner = number[i+1:j]
                # print(inner)
                left_right = [int(n) for n in inner.split(",")]
                
                # Vamos procurar o primeiro número à esquerda
                nleft = None
                pleft1 = None
                pleft2 = None
                for k in range(i-1,-1,-1):
                    if( number[k] in "0123456789" ):
                        pleft2 = k
                        pleft1 = k
                        while( number[pleft1-1] in "0123456789"):
                            pleft1 -= 1
                        vleft = int(number[pleft1:pleft2+1])
                        nleft = left_right[0] + vleft
                        break
                
                # Vamos procurar o primeiro número à direita
                nright = None
                pright1 = None
                pright2 = None
                for k in range(j+1,len(number)):
                    if( number[k] in "0123456789" ):
                        pright1 = k
                        pright2 = k
                        while( number[pright2+1] in "0123456789" ):
                            pright2 += 1
                        vright = int(number[pright1:pright2+1])
                        nright = left_right[1] + vright
                        break
                
                # Na explosão, o número explodido vira zero
                number = number[:i] + "0" + number[j+1:]

                # Corrigindo o índice do número à direita
                if( pright1 != None ):
                    pright1 = pright1 - (j-i)
                    pright2 = pright2 - (j-i)

                # Fazendo as contas e substituições no número    
                if( pleft1 != None and pright1 == None ):
                    number = number[:pleft1] + str(nleft) + number[pleft2+1:]
                elif( pleft1 == None and pright1 != None ):
                    number = number[:pright1] + str(nright) + number[pright2+1:]
                elif( pleft1 != None and pright1 != None ):
                    number = number[:pleft1] + str(nleft) + number[pleft2+1:pright1] + str(nright) + number[pright2+1:]
                
                # Retorna o novo número e diz que houve uma explosão
                return number, True

    # Retorna o número original e diz que não houve explosão
    return number, False

# Faz a operação de split de números. Somente 1 split e retorna.
def split(number):
    # Procura qualquer número
    for i in range(len(number)):
        if( number[i] in "0123456789" ):
            j = i
            while( number[j+1] in "0123456789" ):
                j += 1
            n = int(number[i:j+1])
            # Opa, deu algo maior do que 10. Vamos criar o novo par.
            if( n >= 10 ):
                nleft = n//2
                nright = n - nleft
                # Subtituição no número
                number = number[:i] + "[" + str(nleft) + "," + str(nright) + "]" + number[j+1:]
                # Retorna o novo número e afirma que ocorreu um split
                return number, True
    # Retorna o mesmo número e diz que não ocorreu o split
    return number, False

# Operação básica de adição de 2 números
def add_explode_split(n1, n2):
    # Primeiro faz a adição simples (basicamente um tipo de concatenação)
    n = add(n1,n2)
    # Agora vai fazendo as esplosões e splits até não poder mais
    while(True):
        # Primeiro esgota as explosões
        n, exploded = explode(n)
        while( exploded ):
            n, exploded = explode(n)
        
        # Agora faz os splits necessários
        n, splitted = split(n)
        
        # Se houve um split, vamos continuar processando porque podem ocorrer mais explosões
        if( not splitted ):
            break
    return n

# Cálculo de magnitude (função recursiva)
def magnitude(number):
    # Final da recursão: só tem o par de números
    if( number.count("[") == 1 ):
        n1, n2 = number[1:-1].split(",")
        return 3*int(n1) + 2* int(n2)
    # Vamos dividir para conquistar
    else:
        # Fazendo análise de aninhamentos
        count_nest = 0
        for i in range(1,len(number)-1):
            if(number[i] == '['):
                count_nest += 1
            elif(number[i] == ']'):
                count_nest -= 1
            # Opa, tem uma vírgula (,), então vamos ver se estamos desaninhados
            elif(number[i] == ','):
                # Fechou, podemos dividir
                if( count_nest == 0 ):
                    # Dividindo entre antes e depois da vírgula...
                    number1 = number[1:i]
                    number2 = number[i+1:len(number)-1]
                    # Vendo se vamos fazer recursão nos 2 valores
                    if( number1[0] == '['):
                        n1 = magnitude(number1)
                    else:
                        n1 = int(number1)
                    if( number2[0] == '['):
                        n2 = magnitude(number2)
                    else:
                        n2 = int(number2)
                    # Retorna o valor da magnitude desta recursão
                    return 3 * n1 + 2 * n2

# explode("[[[[[9,8],1],2],3],4]")
# explode("[7,[6,[5,[4,[3,2]]]]]")
# explode("[[6,[5,[4,[3,2]]]],1]")
# explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
# explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")


# n = add_explode_split("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]")
# print(n)

# n = add_explode_split("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]","[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
# print(n)
# n = add_explode_split(n, "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]")
# print(n)
# n = add_explode_split(n, "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]")
# print(n)
# n = add_explode_split(n, "[7,[5,[[3,8],[1,4]]]]")
# print(n)
# n = add_explode_split(n, "[[2,[2,2]],[8,[8,1]]]")
# print(n)
# n = add_explode_split(n, "[2,9]")
# print(n)
# n = add_explode_split(n, "[1,[[[9,3],9],[[9,0],[0,7]]]]")
# print(n)
# n = add_explode_split(n, "[[[5,[7,4]],7],1]")
# print(n)
# n = add_explode_split(n, "[[[[4,2],2],6],[8,7]]")
# print(n)

# print(magnitude("[[9,1],[1,9]]")) # 129
# print(magnitude("[[1,2],[[3,4],5]]")) # 143
# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")) # 3488

n = add_explode_split(data[0],data[1])
for n2 in data[2:]:
    n = add_explode_split(n, n2)

# Imprimindo último número e sua magnitude
print(n)
print(magnitude(n))

