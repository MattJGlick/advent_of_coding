from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    original = list(map(int, inputfile.readline().strip().split(',')))

temp = deepcopy(original) 
temp.extend([0]*10000000)
cur = 0
cur_input = 2
rel_base = 0
while True:
    if temp[cur] == 99:
        break

    x = f'{int(temp[cur]):05}'
    op = int(x[-2:])
    m_1 = int(x[2])
    m_2 = int(x[1])
    m_3 = int(x[0])

    if m_1 == 0:
        p1 = temp[temp[cur+1]]
    elif m_1 == 1:
        p1 = temp[cur+1]
    elif m_1 == 2:
        p1 = temp[temp[cur+1] + rel_base]

    if op in [1, 2, 5, 6, 7, 8, 9]:
        if m_2 == 0:
            p2 = temp[temp[cur+2]]
        elif m_2 == 1:
            p2 = temp[cur+2]
        elif m_2 == 2:
            p2 = temp[temp[cur+2] + rel_base]

    if op == 1:
        if m_3 == 2:
            temp[temp[cur+3] + rel_base] = p1 + p2
        else:
            temp[temp[cur+3]] = p1 + p2
        cur += 4
    elif op == 2:
        if m_3 == 2:
            temp[temp[cur+3] + rel_base] = p1 * p2
        else:
            temp[temp[cur+3]] = p1 * p2
        cur += 4
    elif op == 3:
        if m_1 == 2:
            temp[temp[cur+1] + rel_base] = cur_input
        else:
            temp[temp[cur+1]] = cur_input
        cur += 2
    elif op == 4:
        print(p1)
        cur += 2
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
        if m_3 == 2:
            x = temp[cur+3] + rel_base
        else:
            x = temp[cur+3]

        if p1 < p2:
            temp[x] = 1
        else:
            temp[x] = 0
        cur += 4
    elif op == 8:
        if m_3 == 2:
            x = temp[cur+3] + rel_base
        else:
            x = temp[cur+3]
        if p1 == p2:
            temp[x] = 1
        else:
            temp[x] = 0
        cur += 4
    elif op == 9:
        rel_base += p1
        cur += 2
