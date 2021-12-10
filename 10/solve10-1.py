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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
points = 0
for line in input10:
    line = line.replace("\n","")
    
    sequence = ''
    for c in line:
        if c in ['(','[','{','<']:
            sequence += c
        elif len(sequence) < 0:
            points += pointmap[c]
            break
        else:
            if( sequence[-1] != pair[c] ):
                points += pointmap[c]
                break
            else:
                sequence = sequence[:-1]
        
             
print(points)