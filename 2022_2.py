#A = Rock
#B = Paper
#C = Scissors

#X = Rock
#Y = Paper
#Z= Scissors

with open("2022/2022_2.txt") as f:
    lines = f.read().splitlines()
line =[line.split() for line in lines]
#Part 1
point = 0
for i in range(len(line)):
    if line[i][0] == "A":
        if line[i][1] == "X":
            point += 1
            point += 3
        elif line[i][1] == "Y":
            point += 2
            point += 6
        elif line[i][1] == "Z":
            point += 3
            point += 0
    elif line[i][0] == "B":
        if line[i][1] == "X":
            point += 1
            point += 0
        elif line[i][1] == "Y":
            point += 2
            point += 3
        elif line[i][1] == "Z":
            point += 3
            point += 6
    elif line[i][0] == "C":
        if line[i][1] == "X":
            point += 1
            point += 6
        elif line[i][1] == "Y":
            point += 2
            point += 0
        elif line[i][1] == "Z":
            point += 3
            point += 3
print(point)

#Part2
point = 0

#X= Loose
#Y = Draw
#Z = Win


for i in range(len(line)):
    if line[i][0] == "A":
        if line[i][1] == "X":
            point += 3
            point += 0
        elif line[i][1] == "Y":
            point += 1
            point += 3
        elif line[i][1] == "Z":
            point += 2
            point += 6
    elif line[i][0] == "B":
        if line[i][1] == "X":
            point += 1
            point += 0
        elif line[i][1] == "Y":
            point += 2
            point += 3
        elif line[i][1] == "Z":
            point += 3
            point += 6
    elif line[i][0] == "C":
        if line[i][1] == "X":
            point += 2
            point += 0
        elif line[i][1] == "Y":
            point += 3
            point += 3
        elif line[i][1] == "Z":
            point += 1
            point += 6
print(point)
