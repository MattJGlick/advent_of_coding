from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]


safe = 0
for row in rows:
    levels = list(map(int, row.split()))
    if levels != sorted(levels) and levels != list(reversed(sorted(levels))):
        continue

    prev = 0
    cur = 1

    while cur < len(levels):
        diff = abs(levels[cur] - levels[prev])
        if diff <= 3 and diff >= 1:
            cur += 1
            prev += 1
        else:
            break

    if cur == len(levels):
        safe += 1

print(safe)

### PART 2
def check_safe(levels):
    if levels != sorted(levels) and levels != list(reversed(sorted(levels))):
        return False

    prev = 0
    cur = 1

    while cur < len(levels):
        diff = abs(levels[cur] - levels[prev])
        if diff <= 3 and diff >= 1:
            cur += 1
            prev += 1
        else:
            break

    if cur == len(levels):
        return True
    return False


safe = 0
for row in rows:
    levels = list(map(int, row.split()))

    for i, num in enumerate(levels):
        if check_safe(levels[:i] + levels[i+1:]):
            safe += 1
            break

print(safe)
