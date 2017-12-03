"""
 this is slightly misleading. for part 1 i actually didn't do the code to solve it. every bottom
 right corner is a odd square (1, 9 25, etc). So I found the nearest odd square (bottom right
 corner) was 312481 (559**2), which made the center of that line 312202 (312481 - 279 ((559-1)/2). then did
 312202 (center) - 312051 (my num) = 151 to the left. and i was on the 279th ((559-1)/2) row.
 so 151 + 279 = 430

 might have been a mathy way to do part 2, but couldnt see it... so brute forced. then went back
 and brute forced part 1.
"""


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


    






