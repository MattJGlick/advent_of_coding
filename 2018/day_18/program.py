from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter, namedtuple


class P(namedtuple('P', 'x y')):
    def __add__(self, new):
        return P(self.x + new.x, self.y + new.y)


with open('input_file.txt') as inputfile:
    rows = [list(line.strip()) for line in inputfile]

grid = {}
for y, row in enumerate(rows):
    for x, item in enumerate(row):
        grid[P(x, y)] = item

surrs = [
    P(-1, -1),
    P(0, -1),
    P(1, -1),
    P(-1, 0),
    P(1, 0),
    P(-1, 1),
    P(0, 1),
    P(1, 1)
]

num_secs = 1000000000
for y, row in enumerate(rows):
    for x, item in enumerate(row):
        print(grid[P(x, y)], end='')
    print('')

for sec in range(1, num_secs + 1):
    new_grid = {}

    for pos, item in grid.items():
        neighbor_positions = [surr + pos for surr in surrs]
        types = [grid[n] for n in neighbor_positions if n in grid]

        if item == '.':
            if types.count('|') >= 3:
                new_grid[pos] = '|'
            else:
                new_grid[pos] = item
        elif item == '|':
            if types.count('#') >= 3:
                new_grid[pos] = '#'
            else:
                new_grid[pos] = item
        elif item == '#':
            if types.count('#') >= 1 and types.count('|') >= 1:
                new_grid[pos] = '#'
            else:
                new_grid[pos] = '.'
        else:
            new_grid[pos] = item
    grid = new_grid

    # print('-----------------------------------')
    # for y, row in enumerate(rows):
    #     for x, item in enumerate(row):
    #         print(grid[P(x, y)], end='')
    #     print('')

    # print(sec, list(grid.values()).count('|') * list(grid.values()).count('#'))

print(sec, list(grid.values()).count('|') * list(grid.values()).count('#'))







