input2 = open("input2.txt").readlines()

horiz = 0
depth = 0
aim = 0
# As instruções mudam levemente, mas também são interpretadas diretamente
for i in range(len(input2)):
    [command, value] = (input2[i].replace("\n","")).split()
    if( command == "forward" ):
        horiz += int(value)
        depth += aim * int(value)
    elif( command == "up" ):
        aim -= int(value)
    elif( command == "down" ):
        aim += int(value)
    else:
        print(input[i])

print(f"{horiz},{depth},{horiz*depth}")

