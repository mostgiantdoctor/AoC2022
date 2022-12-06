with open("2022/2022_6.txt") as f:
    line = f.read()
#Part1
for char in range(len(line)):
    if len(set(line[char:char+4])) == len(line[char:char+4]):
        print(char+4)
        break
#Part2
for char in range(len(line)):
    if len(set(line[char:char+14])) == len(line[char:char+14]):
        print(char+14)
        break