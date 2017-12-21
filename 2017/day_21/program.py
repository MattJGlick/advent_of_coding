from collections import defaultdict
import numpy as np
with open('input_file.txt') as inputfile:
    rows = [line.strip().split() for line in inputfile]

rules = {}
for row in rows:
    x = map(list, row[0].split("/"))
    y = tuple(map(tuple, row[2].split("/")))
    for rotate in range(4):
        new_x = tuple(tuple(rot) for rot in np.rot90(x, rotate))
        flipped_new_x = tuple(tuple(rot) for rot in np.rot90(np.fliplr(x), rotate))
        rules[new_x] = y
        rules[flipped_new_x] = y

pattern = tuple(map(tuple, [".#.", "..#", "###"]))

def get_sub_grid(current, x, y, length):
    sub_grid = []
    start_x = x  * length
    end_x = start_x + length
    start_y = y  * length
    end_y = start_y + length

    for x in range(start_x, end_x):
        row = []
        for y in range(start_y, end_y):
            row += current[x][y]
        sub_grid.append(tuple(row))

    return tuple(sub_grid)

for _ in range(18):
    pat_len = len(pattern)
    if pat_len % 3 == 0:
        times = pat_len / 3
        length = 3

    if pat_len % 2 == 0:
        times = pat_len / 2
        length = 2  

    new_pattern = []
    for x in range(times):
        row = defaultdict(list)
        for y in range(times):
            sub = get_sub_grid(pattern, x, y, length)
            box = rules[sub]

            for index, single_row in enumerate(box):
                row[index] += single_row

        for index in row:
            new_pattern.append(row[index])
    pattern = new_pattern

print sum(''.join(row).count("#") for row in pattern)
