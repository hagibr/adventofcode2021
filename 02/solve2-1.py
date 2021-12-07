input2 = open("input2.txt").readlines()

horiz = 0
depth = 0

# Intrepretação direta das instruções
for i in range(len(input2)):
    [command, value] = (input2[i].replace("\n","")).split()
    if( command == "forward" ):
        horiz += int(value)
    elif( command == "up" ):
        depth -= int(value)
    elif( command == "down" ):
        depth += int(value)
    else:
        print(input2[i])

print(f"{horiz},{depth},{horiz*depth}")

