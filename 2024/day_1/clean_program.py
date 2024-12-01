from copy import deepcopy
from itertools import combinations, permutations
import heapq
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

left, right = [], []
total = 0

for row in rows:
    l, r = row.split()
    heapq.heappush(left, int(l))
    heapq.heappush(right, int(r))

while(left):
    total += abs(heapq.heappop(left) - heapq.heappop(right))

print(total)

### PART 2
count = defaultdict(int)
total = 0

for row in rows:
    l, r = row.split()
    left.append(int(l))
    count[int(r)] += 1

for l in left:
    total += l * count[l]

print(total)
