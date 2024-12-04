from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]
    chart = [list(row) for row in rows]


count = 0

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]


def evaluate_neighbors(r, l, coor, letter):
    new_r = r + coor[0]
    new_l = l + coor[1]

    if new_r < 0 or new_r >= len(chart):
        return False
    if new_l < 0 or new_l >= len(chart[0]):
        return False

    if chart[new_r][new_l] == letter and letter == 'S':
        return True
    elif chart[new_r][new_l] == letter and letter == 'M':
        return evaluate_neighbors(new_r, new_l, coor, 'A')
    elif chart[new_r][new_l] == letter and letter == 'A':
        return evaluate_neighbors(new_r, new_l, coor, 'S')
    return False

for row_num, row in enumerate(chart):
    for letter_num, letter in enumerate(row):
        if letter == 'X':
            for direction, coor in enumerate(directions):
                valid = evaluate_neighbors(row_num, letter_num, coor, 'M')
                if valid:
                    count += 1

print(count)

### PART 2
count = 0
for row_num, row in enumerate(chart):
    for letter_num, letter in enumerate(row):
        if letter == 'A':
            if letter_num <= 0 or letter_num >= len(chart[0]) - 1:
                continue
            if row_num <= 0 or row_num >= len(chart) - 1:
                continue

            left_top = chart[row_num - 1][letter_num - 1]
            right_top = chart[row_num + 1][letter_num - 1]
            left_bottom = chart[row_num - 1][letter_num + 1]
            right_bottom = chart[row_num + 1][letter_num + 1]

            v_l = (left_top == 'M'  and right_bottom == 'S') or (left_top == 'S' and right_bottom == 'M')
            v_r = (right_top == 'M'  and left_bottom  == 'S') or (right_top == 'S' and left_bottom == 'M')
            if v_l and v_r:
                count += 1 

            

print(count)
