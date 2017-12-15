##### COPIED FROM DAY 10

def get_knot_hash(string):
    lengths = [ord(char) for char in string]

    lengths += [17, 31, 73, 47, 23]

    elms = range(256)
    cur_pos = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            sub_list = []

            for idx in range(0, length):
                loc = (cur_pos + idx) % len(elms)
                sub_list.append(elms[loc])

            sub_list.reverse()

            for idx in range(0, length):
                loc = (cur_pos + idx) % len(elms)
                elms[loc] = sub_list[idx]

            cur_pos = (cur_pos + length + skip_size) % len(elms)
            skip_size += 1

    dense = []
    for idx_1 in range(16):
        cur_num = 0
        for idx_2 in range(16):
            cur_num = cur_num ^ elms[idx_1 * 16 + idx_2]
        dense.append(cur_num)

    total_hex = ""
    for num in dense:
        hex_num = hex(num)[2:]
        if len(hex_num) == 1:
            hex_num = "0" + hex_num
        total_hex += hex_num
    return total_hex

##### DAY 14

key = "amgozmfv"
total = 0
from collections import defaultdict
memory = defaultdict(list)

for index in range(128):
    hash_input = key + "-" + str(index)
    knot_hash = get_knot_hash(hash_input)
    knot_hash_bin = '{:0128b}'.format(int(knot_hash, 16))
    memory[index] = map(int, knot_hash_bin)
    total += sum(map(int, knot_hash_bin))

print total

found = set()

def find_neighbors(x, y):
    if memory[x][y] == 0 or (x, y) in found:
        return
    if memory[x][y] == 1:
        found.add((x, y))

    if x - 1 >= 0:
        find_neighbors(x - 1, y)
    if y - 1 >= 0:
        find_neighbors(x, y - 1)
    if x + 1 < 128:
        find_neighbors(x + 1, y)
    if y + 1 < 128:
        find_neighbors(x, y + 1)

count = 0
for x in range(128):
    for y in range(128):
        if memory[x][y] == 1:
            if (x, y) not in found:
                find_neighbors(x, y)
                count += 1
print count
