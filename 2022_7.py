import re
from itertools import zip_longest

with open("2022/2022_7.txt") as f:
    lines = f.read().splitlines()

#cd x  ->up
#cd .. ->down
#cd /  ->outermost dir
#ls    ->list

pattern = '\$ '
lines = [re.sub(pattern, "", z) for z in lines]
line = [i.split() for i in lines]

def result_dict(data, y):
    score = 0
    #print(y)
    for i in range(len(data.get(y))):
        #print(i)
        if type(data.get(y)[i]) == int:
            score += data.get(y)[i]
            #print (score, data.get(y)[i])
        else:
            #print(data.get(y)[i])
            z = data.get(y)[i]
            score += result_dict(data, z)
    return score

score2=[]
y = "0"
myDict = {y: []}
level = 0
folderlist = ["0"]

for i in range(1,len(line)):
    if line[i][0] == 'ls':
        pass
    elif line[i][0] == 'dir':
        if level == 0:
            myDict[y].append(line[i][1] +"".join(folderlist[:(level)]))
        else:
            myDict[y].append(line[i][1] +"".join(folderlist[:(level)]))
    elif line[i][0] == 'cd' and line[i][1] == '..':
        level -= 1
        folderlist = folderlist[:level]
    elif line[i][0] == 'cd' and line[i][1] != '..':
        level += 1
        if len(folderlist) <= level:
            folderlist.append(line[i][1])
        else:
            folderlist[level] = line[i][1]
        y = line[i][1]+"".join(folderlist[:(level - 1)])
        if myDict.get(y) == None:
            myDict[y] = []
            print(y, i, folderlist, level)
        else:
            print("WARNUNG!!!", y, i, folderlist, level)
    elif str.isalpha(line[i][0]) == False:
        myDict[y].append(int(line[i][0]))
        score2.append(int(line[i][0]))

scores_min = []
scores_all =[]
for i in myDict:
    score = [result_dict(myDict, i)]
    #print("key", i, score)
    scores_all.append(score)
    if score[0] < 100000:
        print("key", i, score)
        scores_min.append(score)
print(scores_min)

#PartII
tofree = 30000000 - (70000000 - sum(score2))

score_dif = []
for score in scores_all:
    if score[0] >= tofree:
        score_dif.append(score[0])

print(min(score_dif) + tofree)