
data = []
flash = []
for l in open("input11.txt").readlines():
    values = [int(i) for i in l[:-1]]
    vflash = [0 for i in l[:-1]]
    data.append(values)
    flash.append(vflash)

print(data) # Conferência

nrows = len(data)
ncols = len(data[0])

print(nrows, ncols)

flash_count = 0
# 100 passos
for step in range(100):
    had_flash = False
    # Incrementa energia em 1 para todos os polvos
    for r in range(nrows):
        for c in range(ncols):
            data[r][c] += 1
            # Demarcando se este polvo irá brilhar ou não
            if( data[r][c] > 9 ):
                flash[r][c] = 1
                had_flash = True
            else:
                flash[r][c] = 0
    
    # Enquanto puder propagar os brilhos
    while(had_flash):
        had_flash = False

        for r in range(nrows):
            for c in range(ncols):
                # Se este polvo brilhou, vamos aumentar a energia dos 8 adjacentes
                if( flash[r][c] == 1 ):
                    if(r > 0 and c > 0): # Canto superior esquerdo
                        data[r-1][c-1] += 1
                    if(r > 0 and c < ncols-1): # Canto superior direito
                        data[r-1][c+1] += 1
                    if(r < nrows-1 and c > 0): # Canto inferior esquerdo
                        data[r+1][c-1] += 1
                    if(r < nrows-1 and c < ncols-1): # Canto inferior direito
                        data[r+1][c+1] += 1
                    if( r > 0 ): # Imediatamente acima
                        data[r-1][c] += 1
                    if( r < nrows-1 ): # Imediatamente abaixo
                        data[r+1][c] += 1
                    if( c > 0 ): # Imediatamente à esquerda
                        data[r][c-1] += 1
                    if( c < ncols-1 ): # Imediatamente à direita
                        data[r][c+1] += 1
                    flash[r][c] = 2  # Vamos marcar que este polvo já influenciou os adjacentes
                    
        # Reavalia as energias
        for r in range(nrows):
            for c in range(ncols):
                # Demarcando se este polvo irá brilhar agora ou não
                if( data[r][c] > 9 and flash[r][c] == 0 ):
                    flash[r][c] = 1
                    had_flash = True
                            
    # Agora que todos os brilhos foram propagados...
    for r in range(nrows):
        for c in range(ncols):
            # Se este polvo brilhou, contabiliza o brilho e reseta o polvo
            if( data[r][c] > 9 ):
                flash_count += 1
                data[r][c] = 0
        print(data[r])

    print()


    
print(flash_count)