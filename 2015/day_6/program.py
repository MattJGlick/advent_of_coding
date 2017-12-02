import numpy 

grid = set()
def toggle_lights(x1, x2, y1, y2, op):
    for x in range(x1, x2 + 1): 
        for y in range(y1, y2 + 1): 
            if (op == "on") or (op == "toggle" and (x, y) not in grid):
                grid.add((x, y))
            elif (op == "off") or (op == "toggle" and (x, y) in grid):
                if (x, y) in grid:
                    grid.remove((x, y))

mapping = {
    "on": 1,
    "off": -1,
    "toggle": 2
}

array = numpy.zeros((1000,1000), dtype=numpy.int)
def toggle_lights_2(x1, x2, y1, y2, op):
    for x in range(x1, x2 + 1): 
        for y in range(y1, y2 + 1): 
            if not (op == "off" and array[x][y] == 0):
                array[x][y] += mapping[op]

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip().split(" ")

        if line[0] == "toggle":
            x1, y1 = line[1].split(",")
            x2, y2 = line[3].split(",")
            op = "toggle"
        else:
            x1, y1 = line[2].split(",")
            x2, y2 = line[4].split(",")
            op = line[1]

        toggle_lights(int(x1), int(x2), int(y1), int(y2), op)
        toggle_lights_2(int(x1), int(x2), int(y1), int(y2), op)

print len(grid)
print sum(sum(array))
