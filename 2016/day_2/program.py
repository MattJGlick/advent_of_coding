with open('input_file.txt') as inputfile:
    lines = [line.strip() for line in inputfile]

def get_code(pad, x, y):
    dirs = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }

    code = ""
    for line in lines:
        for instr in line:
            dx, dy = dirs[instr]
            nx = x + dx
            ny = y + dy

            if (nx >= 0 and nx < len(pad)) and (ny >= 0 and ny < len(pad[nx])) and (pad[nx][ny] != None):
                x = nx
                y = ny

        code += str(pad[x][y])

    return code

pad = [[1,2,3],[4,5,6],[7,8,9]]
print get_code(pad, 1, 1)

pad_2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]
print get_code(pad_2, 2, 0)
