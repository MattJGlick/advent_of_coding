def find_dist(directions):
    x = 0
    y = 0
    max_dist = 0
    for direction in directions:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "ne":
            x += .5
            y += .5
        elif direction == "sw":
            x -= .5
            y -= .5
        elif direction == "nw":
            x -= .5
            y += .5
        elif direction == "se":
            x += .5
            y -= .5
        if max_dist < abs(x)+abs(y):
            max_dist = abs(x)+abs(y)

    print abs(x)+abs(y)
    print max_dist

with open('input_file.txt') as inputfile:
    rows = [line.strip().split(",") for line in inputfile]

    for row in rows:
        find_dist(row)
