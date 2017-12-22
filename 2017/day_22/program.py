from collections import defaultdict
with open('input_file.txt') as inputfile:
    rows = [list(line.strip()) for line in inputfile]

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
c_dir = 2

h_map = defaultdict(dict)
for x, row in enumerate(rows):
    for y, col in enumerate(row):
        if col == "X":
            h_map[x][y] = "C"
        elif col == ".":
            h_map[x][y] = "C"
        elif col == "#":
            h_map[x][y] = "I"

x = y = len(h_map) / 2
y = len(h_map[y]) / 2

inf_count = 0
for _ in range(10000000):
    if x not in h_map:
        h_map[x] = defaultdict(dict)
    if y not in h_map[x]:
        h_map[x][y] = "C"

    if h_map[x][y] == "C":
        c_dir = (c_dir + 1) % len(dirs)
        h_map[x][y] = "W"
    elif h_map[x][y] == "W":
        inf_count += 1
        h_map[x][y] = "I"
    elif h_map[x][y] == "I":
        c_dir = (c_dir - 1) % len(dirs)
        h_map[x][y] = "F"
    elif h_map[x][y] == "F":
        c_dir = (c_dir + 2) % len(dirs)
        h_map[x][y] = "C"
    
    dx, dy = dirs[c_dir]
    x += dx
    y += dy

print inf_count
