from collections import defaultdict
import re

with open('input_file.txt') as inputfile:
    h = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    rows = [[int(item) for item in h.match(row.strip()).groups()] for row in inputfile]

coors = defaultdict(list)
for row in rows:
    ind, x_s, y_s, x_r, y_r = row

    for x in range(x_s, x_s + x_r):
        for y in range(y_s, y_s + y_r):
            coor = (str(x), str(y))
            coors[coor].append(ind)

print(sum(1 for nums in coors.values() if len(nums) > 1))

for row in rows:
    ind, x_s, y_s, x_r, y_r = row

    good = True
    for x in range(x_s, x_s + x_r):
        for y in range(y_s, y_s + y_r):
            coor = (str(x), str(y))

            if len(coors[coor]) > 1:
                good = False
                break
    if good:
        print(ind)
        break
