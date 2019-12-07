from copy import deepcopy
from itertools import combinations, permutations
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    original = list(map(int, inputfile.readline().strip().split(',')))

def run(inputs, cur):
    temp = deepcopy(original)
    while True:
        if temp[cur] == 99:
            return None, cur

        x = f'{int(temp[cur]):05}'
        op = int(x[-2:])
        m_1 = int(x[2])
        m_2 = int(x[1])
        m_3 = int(x[0])

        if m_1 == 0:
            p1 = temp[temp[cur+1]]
        elif m_1 == 1:
            p1 = temp[cur+1]

        if op in [1, 2, 5, 6, 7, 8]:
            if m_2 == 0:
                p2 = temp[temp[cur+2]]
            elif m_2 == 1:
                p2 = temp[cur+2]

        if op == 1:
            temp[temp[cur+3]] = p1 + p2
            cur += 4
        elif op == 2:
            temp[temp[cur+3]] = p1 * p2
            cur += 4
        elif op == 3:
            temp[temp[cur+1]] = inputs[0]
            inputs.pop(0)
            cur += 2
        elif op == 4:
            cur += 2
            return p1, cur
        elif op == 5:
            if p1 != 0:
                cur = p2
            else:
                cur += 3
        elif op == 6:
            if p1 == 0:
                cur = p2
            else:
                cur += 3
        elif op == 7:
            if p1 < p2:
                temp[temp[cur+3]] = 1
            else:
                temp[temp[cur+3]] = 0
            cur += 4
        elif op == 8:
            if p1 == p2:
                temp[temp[cur+3]] = 1
            else:
                temp[temp[cur+3]] = 0
            cur += 4

max_speed = -99999999999999999999999
max_speed_combo = None

for combo in permutations([5, 6, 7, 8, 9], 5):
    inputs = [[x] for x in combo]
    inputs[0].append(0)
    curs = [0 for _ in range(5)]
    done = False

    while not done:
        for i in range(5):
            output, new_cur = run(inputs[i], curs[i])
            curs[i] = new_cur
            if not output:
                if inputs[0] and inputs[0][0] > max_speed:
                    max_speed_combo = combo
                    max_speed = inputs[0][0]
                done = True
                break
            inputs[(i + 1) % 5].append(output)

print(max_speed_combo)
print(max_speed)
