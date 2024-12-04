from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

total = 0
for row in rows:
    muls = re.findall("mul\(\d*,\d*\)", row)
    for mul in muls:
        nums = list(map(int, mul[4:-1].split(",")))
        total += nums[0] * nums[1]
print(total)

# 7 mins
# part 2
total = 0
full_row = ''.join(rows)

new_row = re.sub("(don't\(\).*?do\(\))|(don't\(\).*?$)", "", full_row)

muls = re.findall("mul\(\d*,\d*\)", new_row)
for mul in muls:
    nums = list(map(int, mul[4:-1].split(",")))
    total += nums[0] * nums[1]
print(total)
