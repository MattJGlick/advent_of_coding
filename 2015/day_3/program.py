mappings = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, -1),
    "^": (0, 1)
}

part = 2

def get_presents(dirs, part):
    santa_cur = (0, 0)
    elf_cur = (0, 0)
    locs = set()
    locs.add(santa_cur)

    for index, direction in enumerate(dirs):
        delta_x, delta_y = mappings[direction]

        if part == 1 or index % 2 == 0:
            x, y = santa_cur
            santa_cur = (x + delta_x, y + delta_y)
            locs.add(santa_cur)
        else:
            x, y = elf_cur
            elf_cur = (x + delta_x, y + delta_y)
            locs.add(elf_cur)

    print len(locs)

with open('input_file.txt') as inputfile:
    for line in inputfile:
        get_presents(line.rstrip(), part)

