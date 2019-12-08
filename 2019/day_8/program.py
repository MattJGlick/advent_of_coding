from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]
full = list(map(int, list(rows[0])))

x = np.array_split(full, 100)

least_zeroes = 9999999999999999
least_counter = None
for l in x:
    y = Counter(l)
    if y[0] < least_zeroes:
        least_zeroes = y[0]
        least_counter = y

print(least_counter[1] * least_counter[2])

grid = []
for y in x:
    grid.append(np.array_split(y, 6))

final = deepcopy(grid[0])
for row in range(6):
    for col in range(25):
        y = [grid[x][row][col] for x in range(100)]
        z = next(obj for obj in y if obj!=2)
        final[row][col] = z

for row in final:
    print(''.join(map(str, row)))
