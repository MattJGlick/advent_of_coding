from itertools import combinations, permutations
from copy import deepcopy
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    original = list(map(int, inputfile.readline().strip().split(',')))

temp = deepcopy(original)
cur = 0
while True:
    if temp[cur] == 99:
        break

    if temp[cur] == 1:
        temp[temp[cur+3]] = temp[temp[cur+1]] + temp[temp[cur+2]]
    elif temp[cur] == 2:
        temp[temp[cur+3]] = temp[temp[cur+1]] * temp[temp[cur+2]]

    cur += 4

print(temp[0])

for x in range(0, 100):
    for y in range(0, 100):
        cur = 0
        temp = deepcopy(original)
        temp[1] = x
        temp[2] = y

        while True:
            if temp[cur] == 99:
                break

            if temp[cur] == 1:
                temp[temp[cur+3]] = temp[temp[cur+1]] + temp[temp[cur+2]]
            elif temp[cur] == 2:
                temp[temp[cur+3]] = temp[temp[cur+1]] * temp[temp[cur+2]]

            cur += 4

        if temp[0] == 19690720:
            print(100*x+y)


#------------------------ BETTERRRRR

def get_output(reg):
    cur = 0
    while True:
        if reg[cur] == 99:
            break

        if reg[cur] == 1:
            reg[reg[cur+3]] = reg[reg[cur+1]] + reg[reg[cur+2]]
        elif reg[cur] == 2:
            reg[reg[cur+3]] = reg[reg[cur+1]] * reg[reg[cur+2]]

        cur += 4
    
    return reg[0]

print(get_output(deepcopy(original)))

for x in range(0, 100):
    for y in range(0, 100):
        temp = deepcopy(original)
        temp[1] = x
        temp[2] = y
        if get_output(temp) == 19690720:
            print(100*x+y)
            break
