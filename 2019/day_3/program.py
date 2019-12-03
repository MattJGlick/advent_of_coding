from copy import deepcopy
from itertools import combinations, permutations
# import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip().split(',') for line in inputfile]

wire_1 = rows[0]
wire_2 = rows[1]

def man_dist(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))
def intersection(list_a, list_b):
    return [ e for e in list_a if e in list_b ]

def get_locations(path):
    locs = []
    cur = (0, 0)

    for p in path:
        d = p[0]
        amount = int(p[1:])

        if d == 'R':
            for _ in range(amount):
                locs.append((cur[0] + _, cur[1]))
            cur = (cur[0]+amount, cur[1])
        elif d == 'L':
            for _ in range(amount):
                locs.append((cur[0] - _, cur[1]))
            cur = (cur[0]-amount, cur[1])
        elif d == 'U':
            for _ in range(amount):
                locs.append((cur[0], cur[1] + _))
            cur = (cur[0], cur[1]+amount)
        elif d == 'D':
            for _ in range(amount):
                locs.append((cur[0], cur[1] - _))
            cur = (cur[0], cur[1]-amount)

        # print(locs)

    return locs

loc_1 = get_locations(wire_1)
print("got loc1")
loc_2 = get_locations(wire_2)
print("got loc2")
insect = list(set(loc_1) & set(loc_2))
if (0, 0) in insect:
    insect.remove((0, 0))

min_dist = 99999999999999
for item in insect:
    dist = man_dist((0, 0), item)
    if dist < min_dist:
        min_dist = dist

print(min_dist)

def get_locations_2(path):
    locs = []
    cur = (0, 0)
    count = 0
    counts = {}

    for p in path:
        d = p[0]
        amount = int(p[1:])

        if d == 'R':
            for _ in range(1, amount+1):
                locs.append((cur[0] + _, cur[1]))
                count += 1
                counts[(cur[0] + _, cur[1])] = count
            cur = (cur[0]+amount, cur[1])
        elif d == 'L':
            for _ in range(1, amount+1):
                locs.append((cur[0] - _, cur[1]))
                count += 1
                counts[(cur[0] - _, cur[1])] = count
            cur = (cur[0]-amount, cur[1])
        elif d == 'U':
            for _ in range(1, amount+1):
                locs.append((cur[0], cur[1] + _))
                count += 1
                counts[(cur[0], cur[1] + _)] = count
            cur = (cur[0], cur[1]+amount)
        elif d == 'D':
            for _ in range(1, amount+1):
                locs.append((cur[0], cur[1] - _))
                count += 1
                counts[(cur[0], cur[1] - _)] = count
            cur = (cur[0], cur[1]-amount)

    return counts


min_dist_2 = 999999999999999999
counts_1 = get_locations_2(wire_1)
counts_2 = get_locations_2(wire_2)
for item in insect:
    if counts_1[item] + counts_2[item] < min_dist_2:
        min_dist_2 = counts_1[item] + counts_2[item]

print(min_dist_2)
import pdb; pdb.set_trace()  # noqa
