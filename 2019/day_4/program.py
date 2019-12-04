from copy import deepcopy
from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

count = 0
count_2 = 0
for x in range(145852, 616943):
    y = list(map(int, list(str(x))))
    if y[0] == y[1] or y[1] == y[2] or y[2] == y[3] or y[3] == y[4] or y[4] == y[5]:
        if y[0] <= y[1] and y[1] <= y[2] and y[2] <= y[3] and y[3] <= y[4] and y[4] <= y[5]:
            count += 1

    if (y[0] == y[1] and y[1] != y[2]) or \
         (y[0] != y[1] and y[1] == y[2] and y[2] != y[3]) or \
         (y[1] != y[2] and y[2] == y[3] and y[3] != y[4]) or \
         (y[2] != y[3] and y[3] == y[4] and y[4] != y[5]) or \
         (y[3] != y[4] and y[4] == y[5]):
        if y[0] <= y[1] and y[1] <= y[2] and y[2] <= y[3] and y[3] <= y[4] and y[4] <= y[5]:
            count_2 += 1

print(count)
print(count_2)
