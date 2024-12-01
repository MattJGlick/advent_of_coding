from copy import deepcopy
from itertools import combinations, permutations
import heapq
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

left, right = [], []

for row in rows:
    f, s = row.split()
    left.append(int(f))
    right.append(int(s))
heapq.heapify(left)
heapq.heapify(right)

total = 0
while(left):
    l = heapq.heappop(left)
    r = heapq.heappop(right)
    total += abs(l - r)

print(total)

### PART 2
for row in rows:
    f, s = row.split()
    left.append(int(f))
    right.append(int(s))

count = defaultdict(int)
for r in right:
    count[r] += 1
total = 0
for l in left:
    total += l * count[l]

print(total)
