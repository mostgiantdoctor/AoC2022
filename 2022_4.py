import re

with open("2022/2022_4.txt") as f:
    lines = f.read().splitlines()

#Part1
score = 0
for pair in range(len(lines)):
    section = re.split("-|,", lines[pair])
    section = [int(entry) for entry in section]
    if section[0] >= section[2] and section[1] <= section[3]:
        score += 1
        print(section)
    elif section[2] >= section[0] and section [3] <= section[1]:
        score += 1
        print(section)
    else:
        pass
print(score)
#Part2
score = 0
for pair in range(len(lines)):
    section = re.split("-|,", lines[pair])
    section = [int(entry) for entry in section]
    if section[0] >= section[2] and section[0] <= section[3]:
        score += 1
        continue
    if section[1] >= section[2] and section[1] <= section[3]:
        score += 1
        continue
    if section[1] >= section[3] and section[0] <= section[2]:
        score += 1
        continue
    else:
        pass
print(score)
