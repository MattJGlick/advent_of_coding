from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip().split(')') for line in inputfile]

orbits = {}
total = set()
for row in rows:
    x, y = row
    total.add(x)
    total.add(y)
    orbits[y] = x
    orbits[y] = x

count = 0

for cur in total:
    while cur != 'COM':
        count += 1
        cur = orbits[cur]

print(count)



orbits = defaultdict(list)
total = set()
for row in rows:
    x, y = row
    total.add(x)
    total.add(y)
    orbits[y].append(x)
    orbits[x].append(y)

count = 0

def explore(orbits, cur, count, seen, total):
    explorable = orbits[cur]

    if seen == total:
        return

    for y in explorable:
        if y == 'SAN':
            print(count)

        if y not in seen:
            seen.append(y)
            explore(orbits, y, count+1, seen, total)
