from copy import deepcopy
from itertools import combinations, permutations
import re
import sys
import math

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [list(line.strip()) for line in inputfile]

asts = []
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == '#':
            asts.append((x, y))

def isBetween(x1, x2, x3, y1, y2, y3):
    crossproduct = (y3 - y1) * (x2 - x1) - (x3 - x1) * (y2 - y1)

    if abs(crossproduct) > sys.float_info.epsilon:
        return False

    dotproduct = (x3 - x1) * (x2 - x1) + (y3 - y1)*(y2 - y1)
    if dotproduct < 0:
        return False

    squaredlengthba = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
    if dotproduct > squaredlengthba:
        return False

    return True
counts = [0] * len(asts)
for i, ast in enumerate(asts):
    x, y = ast
    count = 0

    for ast2 in asts:
        x2, y2 = ast2
        if ast != ast2:
            path_clear = True
            for ast3 in asts:
                if ast != ast3 and ast2 != ast3:
                    x3, y3 = ast3
                    if isBetween(x, x2, x3, y, y2, y3):
                        path_clear = False
            if path_clear:
                count += 1

    counts[i] = count


print(asts[counts.index(max(counts))])
print(max(counts))

best_station = asts[counts.index(max(counts))]

def man(x, y, x2, y2):
    return abs(x2 - x) + abs(y2 - y)

def degrees(x, y, x2, y2):
    x =  math.degrees(math.atan2(y2-y, x2-x))
    return (x + 360 + 90) % 360

x, y = best_station
asts.remove(best_station)
used_degrees = []
removed = []

while len(asts) > 0:
    closest_ast = asts[0]
    current_low_degree = None
    right_degree = []
    for ast in asts:
        this_degree = degrees(x, y, ast[0], ast[1])
        if this_degree == current_low_degree and this_degree not in used_degrees:
            right_degree.append(ast)
        elif current_low_degree == None or (this_degree < current_low_degree and this_degree not in used_degrees):
            current_low_degree = this_degree
            right_degree = [ast]

    if right_degree:
        used_degrees.append(current_low_degree)
        mans = [man(x, y, a[0], a[1]) for a in right_degree]
        lowest_man = min(mans)
        to_remove = right_degree[mans.index(lowest_man)]
        removed.append(to_remove)
        asts.remove(to_remove)

print(removed[199])

