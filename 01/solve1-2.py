input1 = open("input1.txt").readlines()

increaseCount = 0
# Não precisamos calcular as somas, basta comparar o elemnto atual com 3 elementos à frente
# Afinal, a1 + a2 + a3 < a2 + a3 + a4 significa que a1 < a4
for i in range(len(input1)-3):
    if( int(input1[i]) < int(input1[i+3]) ):
        increaseCount += 1

print(f"increased: {increaseCount}")

