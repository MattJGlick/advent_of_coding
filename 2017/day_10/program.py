with open('input_file.txt') as inputfile:
    input_row = map(int, [line.strip().split(",") for line in inputfile][0])

elms = range(256)
cur_pos = 0
skip_size = 0

for length in input_row:
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

    # print elms
    # print cur_pos
    # print skip_size

print elms[0] * elms[1]





#### PART 2

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

        # print elms
        # print cur_pos
        # print skip_size

    dense = []
    for idx_1 in range(16):
        cur_num = 0
        for idx_2 in range(16):
            cur_num = cur_num ^ elms[idx_1 * 16 + idx_2]
        dense.append(cur_num)
    print dense

    total_hex = ""
    for num in dense:
        hex_num = hex(num)[2:]
        if len(hex_num) == 1:
            hex_num = "0" + hex_num
        total_hex += hex_num
    return total_hex
with open('input_file.txt') as inputfile:
    input_row = [line.strip() for line in inputfile][0]
    print get_knot_hash(input_row)

assert get_knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert get_knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert get_knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert get_knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"


