input3 = open("input3.txt").readlines()

counters = [0]*12

# 
for i in range(len(input3)):
    for j in range(12):
        if( input3[i][j] == '1'):
            counters[j] += 1

gamma = 0
epsilon = 0
for k in range(12):
    # Maioria é 1
    if( counters[k] > len(input3)/2 ):
        gamma = (gamma << 1) | 1
        epsilon = (epsilon << 1) | 0
    else:
        gamma = (gamma << 1) | 0
        epsilon = (epsilon << 1) | 1


print(f"{gamma},{epsilon},{gamma*epsilon}")
