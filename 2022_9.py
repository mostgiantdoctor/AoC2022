from copy import deepcopy
import numpy as np

with open("2022/2022_9.txt") as f:
    lines = f.read().splitlines()

lines = [line.split(" ") for line in lines]
position_H = np.array([0,0])
position_T = np.array([0,0])
positions_H = []
positions_T = []
lastmove = []

for i, direct in enumerate(lines):
    for i in range(0,int(direct[1])):
        if direct[0] == "R":
            position_H += [1, 0]
            lastmove = [1, 0]
        elif direct[0] == "L":
            position_H += [-1, 0]
            lastmove = [-1, 0]
        elif direct[0] == "U":
            position_H += [0, 1]
            lastmove = [0, 1]
        elif direct[0] == "D":
            position_H += [0, -1]
            lastmove = [0, -1]
        position_H_store = [position_H[0], position_H[1]]
        if position_H_store not in positions_H:
            positions_H.append(position_H_store)
        # Position T
        pos_dif_x = abs(position_T[0] - position_H[0])
        pos_dif_y = abs(position_T[1] - position_H[1])
        print(direct, position_H, position_T, pos_dif_x, pos_dif_y)
        if direct[0] == "R":
            if position_T[1] == position_H[1] and pos_dif_x > 1:
                position_T += [1, 0]
            elif position_T[1] != position_H[1] and pos_dif_x >1:
                position_T += [1, position_H[1]-position_T[1]]
        elif direct[0] == "L":
            if position_T[1] == position_H[1] and pos_dif_x > 1:
                position_T += [-1, 0]
            elif position_T[1] != position_H[1] and pos_dif_x >1:
                position_T += [-1, position_H[1]-position_T[1]]
        elif direct[0] == "U":
            if position_T[0] == position_H[0] and pos_dif_y > 1:
                position_T += [0, 1]
            elif position_T[0] != position_H[0] and pos_dif_y >1:
                position_T += [position_H[0]-position_T[0], 1]
        elif direct[0] == "D":
            if position_T[0] == position_H[0] and pos_dif_y > 1:
                position_T += [0, -1]
            elif position_T[0] != position_H[0] and pos_dif_y >1:
                position_T += [position_H[0]-position_T[0], -1]
        position_T_store = [position_T[0], position_T[1]]
        if position_T_store not in positions_T:
            positions_T.append(position_T_store)
        #Position H

        print(direct, position_H, position_T, pos_dif, abs(sum(pos_dif)))

len(positions_T)
        #print(position_H)


