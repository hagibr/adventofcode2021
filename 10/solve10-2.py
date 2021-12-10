input10 = open("input10.txt").readlines()

# input10 = '''
# [({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]
# '''.split("\n")

pointmap = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

scorelist = []

for line in input10:
    line = line.replace("\n","")
    
    sequence = ''

    # Eliminando linhas corrompidas
    corrupted = False
    for c in line:
        if c in ['(','[','{','<']:
            sequence += c
        elif len(sequence) < 0:
            corrupted = True
            break
        else:
            if( sequence[-1] != pair[c] ):
                corrupted = True
                break
            else:
                sequence = sequence[:-1]
    
    
    # Se é só linha incompleta:
    if not corrupted:
        sequence = sequence[::-1]
        print(sequence)
        # Calcula pontuação 
        score = 0
        for c in sequence:
            score = score*5 + pointmap[c]
        print(score)
        if score > 0 :
            scorelist.append(score)

# Ordena    
scorelist.sort()
# Pega o score mais do meio (mediana)
print(scorelist)
print(scorelist[int(len(scorelist)/2)])
