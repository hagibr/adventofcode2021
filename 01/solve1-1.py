input1 = open("input1.txt").readlines()

increaseCount = 0
# Comparação direta entre elementos consecutivos. Não tem como comparar o último com um depois dele, logo
# subraímos 1 do range
for i in range(len(input1)-1):
    if( int(input1[i]) < int(input1[i+1]) ):
        increaseCount += 1

print(f"increased: {increaseCount}")

