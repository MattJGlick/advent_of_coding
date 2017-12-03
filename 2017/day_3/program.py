def find_coords(input_num):
    direction = 1
    x = 0
    y = 0
    cur_num = 1
    incr = 1

    while True:
        for _ in range(0, incr):
            x += direction
            cur_num += 1
            if cur_num == input_num:
                return abs(x) + abs(y)
                
        for _ in range(0, incr):
            y += direction
            cur_num += 1
            if cur_num == input_num:
                return abs(x) + abs(y)

        direction *= -1
        incr += 1

num_map = {}
num_map[0,0]=1

def find_sum(loc):
    to_check = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,1),
        (0,-1),
        (1,1),
        (1,0),
        (1,-1),
    ]

    cur_sum = 0
    x, y = loc
    for check in to_check:
        move_x, move_y = check
        if (move_x + x, move_y + y) in num_map:
            cur_sum += num_map[(move_x + x, move_y + y)]

    return cur_sum


def find_coords_2(input_num):
    direction = 1
    x = 0
    y = 0
    incr = 1

    while True:
        for _ in range(0, incr):
            x += direction
            this_block = find_sum((x, y))
            num_map[x,y] = this_block
            if this_block > input_num:
                return this_block

                
        for _ in range(0, incr):
            y += direction
            this_block = find_sum((x, y))
            num_map[x,y] = this_block
            if this_block > input_num:
                return this_block

        direction *= -1
        incr += 1

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()
        print find_coords(int(line))
        print find_coords_2(int(line))


    






