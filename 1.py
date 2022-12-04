with open("2022/2022_1.txt") as f:
    lines = f.read().splitlines()

sumcals=[]
sumcal = 0

for i in range(len(lines)):
    if lines[i] != '':
        sumcal += int(lines[i])
    else:
        sumcals.append(sumcal)
        sumcal = 0
max(sumelfs)

#PartII

sumcals.sort()
sum(sumcals[-3:])