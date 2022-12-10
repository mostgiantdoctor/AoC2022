with open("2022/2022_8.txt") as f:
    lines = f.read().split()

from copy import deepcopy


trees = []
for i in lines:
    treeline = [int(chars) for chars in i]
    trees.append(treeline)

trees_check = deepcopy(trees) #Listen müssen eindeutig kopiert werden, sonst nur Referenz

def check_hor(treelines, value, status=False):
    if status == False:
        for i, tree in enumerate(treelines):
            print(value,tree)
            if value > tree:
                status = True
            else:
                status = False
                break
    return status

def check_ver(y, trees, value, status):
    if status == False:
        for i, treeline in enumerate(trees):
            #print("hier:", value, treeline[y])
            if value > treeline[y]:
                status = True
            else:
                status = False
                break
    return status

for i, treelines in enumerate(trees):
    for y, tree in enumerate(treelines):
        n = len(trees)
        if i == 0 or i == n - 1:
            trees_check[i][y] = True
        elif y == 0 or y == n - 1:
            trees_check[i][y] = True
        else:
            if y >0 and y < n-1 and i > 0 and i < n-1 :
                status = check_hor(treelines[:y][::-1], tree)
                #print(i, y, treelines[:y][::-1], tree, status)
                status = check_hor(treelines[y+1:], tree, status)
                #print(i, y, treelines[y+1:], tree, status)
                status = check_ver(y, trees[:i][::-1], tree, status)
                #print(i, y, trees[:i][::-1], tree, status)
                status = check_ver(y, trees[i+1:], tree, status)
                #print(i, y, trees[i+1:], tree, status)
                trees_check[i][y] = status

sum([sum(treeline) for treeline in (trees_check)])
           # check_up(y,i)
        #if y <= n/2 and y >1:
         #   check_right()
          #  check_up()



