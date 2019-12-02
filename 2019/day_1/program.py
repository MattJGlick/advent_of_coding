from itertools import combinations, permutations
from math import floor
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [int(line.strip()) for line in inputfile]

total = 0
for num in rows:
    total += floor(num / 3) - 2

print(total)

total = 0
for num in rows:
    cur_fuel = 0
    while floor(num / 3) - 2 > 0:
         num = floor(num / 3) - 2
         cur_fuel += num
    total += cur_fuel

print(total)
