# Exemplo: target area: x=20..30, y=-10..-5
#x1,x2,y1,y2=20,30,-10,-5

# Puzzle input: target area: x=207..263, y=-115..-63
x1,x2,y1,y2=207,263,-115,-63

# Função que faz o cálculo do passo da trajetória
def calcstep(x,y,vx,vy):
    x += vx
    y += vy
    vx -= 1
    if( vx < 0 ):
        vx = 0
    vy -= 1
    return x,y,vx,vy
    
# Maior y de uma trajetória que atinge o alvo
maxy = y1
# Quantidade de trajetórias que atingiram o alvo
hits = 0

# Vamos fazer uma varredura de velocidades iniciais nas direções x (svx) e y (svy)
for svx in range(1,x2+1):
    for svy in range(y1,-y1):
        # Maior y desta trajetória
        my = y1
        # Posições velocidades iniciais para esta trajetória
        x,y,vx,vy = 0,0,svx,svy
        # Se ainda não passou os limites da região do alvo
        while( x <= x2 and y >= y1 ):
            # Anda um passo
            x,y,vx,vy = calcstep(x,y,vx,vy)
            # Guarda o valor máximo da coordenada y desta trajetória
            if( y > my ):
                my = y
            # Verifica se atingiu o alvo
            if( x1 <= x and x <= x2 and y1 <= y and y <= y2 ):
                # Incrementa contador de trajetórias que atinge o alvo
                hits += 1
                # Atualiza y máximo de todas as trajetórias
                if( my > maxy):
                    maxy = my
                #print(f"{svx,svy}")
                break

# Pode imprimir os 2 valores desejados
print(maxy) # Maior y alcançado por alguma trajetória que atingiu o alvo
print(hits) # Quantidade de trajetórias que atingiram o alvo