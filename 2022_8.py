from copy import deepcopy

with open("2022/2022_8.txt") as f:
    lines = f.read().split()

trees = []
for i in lines:
    treeline = [int(chars) for chars in i]
    trees.append(treeline)

trees_check = deepcopy(trees) #Listen müssen eindeutig kopiert werden, sonst nur Referenz

def check_hor(treelines, value, status_org):
    count = 0
    status = status_org
    for i, tree in enumerate(treelines):
        count += 1
        #print(value,tree)
        if value > tree:
            status = True
        else:
            status = False
            break
    if status_org == True:
        status = status_org
    return status, count

def check_ver(y, trees, value, status_org):
    count = 0
    status = status_org
    for i, treeline in enumerate(trees):
        count += 1
        #print("hier:", value, treeline[y])
        if value > treeline[y]:
            status = True
        else:
            status = False
            break
    if status_org == True:
        status = status_org
    return status, count

for i, treelines in enumerate(trees):
    for y, tree in enumerate(treelines):
        n = len(trees)
        if i == 0 or i == n - 1:
            trees_check[i][y] = [True, 1]
        elif y == 0 or y == n - 1:
            trees_check[i][y] = [True, 1]
        else:
            if y >0 and y < n-1 and i > 0 and i < n-1 :
                status = False
                status, count1 = check_hor(treelines[:y][::-1], tree, status)
                #print(i, y, treelines[:y][::-1], tree, status, count1)
                status, count2 = check_hor(treelines[y+1:], tree, status)
                #print(i, y, treelines[y+1:], tree, status, count2)
                status, count3 = check_ver(y, trees[:i][::-1], tree, status)
                #print(i, y, trees[:i][::-1], tree, status, count3)
                status, count4 = check_ver(y, trees[i+1:], tree, status)
                #print(i, y, trees[i+1:], tree, status, count4)
                count = count1*count2*count3*count4
                trees_check[i][y] = [status, count]

treelines = [(treeline) for treeline in (trees_check)]
status = [list(zip(*tree))[0] for tree in treelines]
count = [list(zip(*tree))[1] for tree in treelines]

#Part1
print(sum([sum(tree) for tree in status]))
#Part2
print(max([max(tree) for tree in count]))
