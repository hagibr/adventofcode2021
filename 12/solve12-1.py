data = [l.replace("\n","") for l in open("input12.txt").readlines()]

# data = '''start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end'''.split("\n")

# data = '''dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc'''.split("\n")

# data = '''fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW'''.split("\n")

print(data)
# Idéia: tentar montar a árvore e percorrer ela por todos os caminhos possíveis indo de start até end
# Cavernas pequenas só podem ser pontos de passagem ou 'dead-ends'
cave_paths = []
start_paths = []

# Processa os dados de entrada, preenchendo as listas
for d in data:
    caves = d.split("-")
    print(caves)
    if( caves[0] == 'start' ):
        start_paths.append(('start', caves[1]))
    elif( caves[1] == 'start' ):
        start_paths.append(('start', caves[0]))
    elif( caves[0] == 'end' ):
        cave_paths.append((caves[1],'end'))
    elif( caves[1] == 'end' ):
        cave_paths.append((caves[0],'end'))
    else:
        cave_paths.append((caves[0],caves[1]))
        cave_paths.append((caves[1],caves[0]))

print(start_paths)
print(cave_paths)

# Função auxiliar que irá ajudar a percorrer as cavernas
def explore_caves(tracking, current_cave, cave_list):
    tracking += f"{current_cave},"
    path_count = 0
    for p in cave_paths:
        if( p[0] == current_cave ):
            # Se vai terminar o caminho...
            if( p[1] == 'end' ):
                print(f"{tracking}end")
                path_count += 1
            # Se a caverna já foi visitada...
            elif( p[1] in cave_list ):
                # Mas pode ser revisitada...
                if( p[1][0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    path_count += explore_caves(tracking, p[1], cave_list)
                # Se não pode ser revisitada, encontramos um caminho inválido
                # else:
                #     print(f"{tracking}{p[1]},invalid")
            # Se não foi visitada, vamos lá
            else:
                cave_list.append(p[1])
                path_count += explore_caves(tracking, p[1], cave_list)
                cave_list.remove(p[1])
    return path_count

# Agora vamos varrer os caminhos possíveis
total_paths = 0
for s in start_paths:
    tracking = "start,"
    # Para cada caminho, vamos manter uma lista de cavernas que já passamos
    cave_list = [s[1]]
    total_paths += explore_caves(tracking, s[1], cave_list)
    # Pode tirar da lista
    cave_list.remove(s[1])

print(total_paths)
