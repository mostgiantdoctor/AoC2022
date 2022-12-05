import re
from itertools import zip_longest

with open("2022/2022_5.txt") as f:
    lines = f.read().splitlines()

input = []
commands_set = False
commands = []
for i in range((len(lines))):
    if lines[i] == '':
        commands_set = True
        continue
    if commands_set:
        command = [int(y) for y in re.findall('\d+', lines[i])]
        commands.append(command)
    else:
        test = re.findall('.{1,4}', lines[i])
        test = [re.sub("\[|\]| ", "", z) for z in test]
        input.append(test)


input2 = zip_longest(*input, fillvalue="")
input2 = list(input2)
input2 = [i[:-1] for i in input2]

#Part1
input3 = []

for i in range(len(input2)):
    input3.append([x for x in input2[i] if x != ''])

for i in range(len(commands)):
    print(commands[i])
    for y in range(commands[i][0]):
        print(commands[i][0]-1)
        input3[(commands[i][2]-1)].insert(0,input3[(commands[i][1]-1)][0])
        del input3[(commands[i][1]-1)][0]

answer = [x[0] for x in input3]
print("".join(answer))

#Part2
input3 = []

for i in range(len(input2)):
    input3.append([x for x in input2[i] if x != ''])

for i in range(len(commands)):
    if commands[i][0] == 1:
        input3[(commands[i][2] - 1)].insert(0, input3[(commands[i][1] - 1)][0])
        del input3[(commands[i][1] - 1)][0]
    else:
        input3[(commands[i][2] - 1)] = input3[commands[i][1] -1][:commands[i][0]] + input3[(commands[i][2] - 1)]
        del input3[commands[i][1] -1][:commands[i][0]]
    print(input3)

answer = [x[0] for x in input3]
print("".join(answer))