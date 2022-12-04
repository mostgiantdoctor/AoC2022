import re

with open("2022/2022_4.txt") as f:
    lines = f.read().splitlines()

#Part1
score = 0
for pair in range(len(lines)):
    test = re.split("-|,", lines[pair])
    test = [int(entry) for entry in test]
    if test[0] >= test[2] and test [1] <= test[3]:
        score += 1
        print(test)
    elif test[2] >= test[0] and test [3] <= test[1]:
        score += 1
        print(test)
    else:
        pass
print(score)
#Part2
score = 0
for pair in range(len(lines)):
    test = re.split("-|,", lines[pair])
    #test = lines[pair][0], lines[pair][2], lines[pair][4], lines[pair][6]
    test = [int(entry) for entry in test]
    if test[0] >= test[2] and test[0] <= test[3]:
        score += 1
        print(test, "1")
        continue
    if test[1] >= test[2] and test[1] <= test[3]:
        score += 1
        print(test)
        continue
    if test[1] >= test[3] and test[0] <= test[2]:
        score += 1
        print(test)
        continue
    else:
        pass
print(score)
