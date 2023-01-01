from copy import deepcopy
import numpy as np

with open("2022/2022_9.txt") as f:
    lines = f.read().splitlines()

lines = [line.split(" ") for line in lines]
tail_len = 1  # for part 2 = 9, part 1 = 1

# Part 2
def tail_pos(position_t, position_h, positions_t, position_h_before, i):
    pos_dif_x = position_t[0] - position_h[0]
    pos_dif_y = position_t[1] - position_h[1]
    # print("1", direct, "Head:", position_H, "Tail:", position_T, "Dif X:", pos_dif_x, "Dif Y:", pos_dif_y)

    if abs(pos_dif_x) > 1:
        position_t = position_h_before
    if abs(pos_dif_y) > 1:
        position_t = position_h_before
    if abs(pos_dif_y) > 1 and abs(pos_dif_y) > 1:
        position_t = position_h_before
    if abs(pos_dif_x) == 2 and abs(pos_dif_y) == 2:
        position_t = position_h_before
    elif abs(pos_dif_x) == 2:
        position_t[0] = position_h_before[0]
        position_t[1] = position_h[1]
    elif abs(pos_dif_y) == 2:
        position_t[0] = position_h[0]
        position_t[1] = position_h_before[1]

    position_t_store = [position_t[0], position_t[1]]
    if i == tail_len:
        if position_t_store not in positions_t:
            positions_t.append(position_t_store)
    # pos_dif_x = position_T[0] - position_H[0]
    # pos_dif_y = position_T[1] - position_H[1]
    # print("2", direct, "Head:", position_H, "Tail:", position_T, "Dif X:", pos_dif_x, "Dif Y:", pos_dif_y)
    return position_t_store, positions_t

position_all_T = []
position_H = np.array([0, 0])
position_T = np.array([0, 0])
positions_H = []
positions_T = []
for i in range(1, tail_len+1):
    position_all_T.append(([0, 0]))

for line, direct in enumerate(lines):
    for steps in range(0, int(direct[1])):
        position_H_before = np.copy(position_H)
        position_all_Hs_before = deepcopy(position_all_T)
        position_all_Hs_before.insert(0, [position_H_before[0], position_H_before[1]])
        if direct[0] == "R":
            position_H += [1, 0]
        elif direct[0] == "L":
            position_H += [-1, 0]
        elif direct[0] == "U":
            position_H += [0, 1]
        elif direct[0] == "D":
            position_H += [0, -1]
        position_H_store = [position_H[0], position_H[1]]
        if position_H_store not in positions_H:
            positions_H.append(position_H_store)
        # print(direct, position_H, position_all_T)
        position_H4T = position_H

        for i in range(1, tail_len+1):
            # print("Tail:", i)
            position_T, positions_T = tail_pos(np.array(position_all_T[i-1]), position_H4T, positions_T,
                                               position_all_Hs_before[i-1], i)
            position_all_T[i-1] = position_T
            position_H4T = np.array(position_T)
        # print("End of Move", direct, position_H, position_all_T)

print(len(positions_T))
