from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter, namedtuple

map_regex = re.compile('(x|y)=(\d+), (x|y)=(\d+)..(\d+)')
with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]


class P(namedtuple('P', 'x y')):
    def __add__(self, new):
        return P(self.x + new.x, self.y + new.y)


clay = set([])
flow = set([P(500, 0)])
spring = set([P(500, 0)])
still = set([])

L = P(-1, 0)
R = P(1, 0)
D = P(0, 1)
U = P(0, -1)

max_water = 0


def print_map(min_x, max_x, min_y, max_y):
    for x in range(min_x, max_x):
        print('A', end='')
    print('')
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if (x, y) in still:
                print('~', end='')
            elif (x, y) in flow:
                print('|', end='')
            elif (x, y) in clay:
                print('#', end='')
            else:
                print('.', end='')

        print('')


for row in rows:
    ax, ax_num, ax_2, ax_2_1, ax_2_2 = map_regex.match(row).groups()
    ax_num = int(ax_num)

    for second_axis in range(int(ax_2_1), int(ax_2_2) + 1):
        if ax == 'x':
            clay.add(P(ax_num, second_axis))
        else:
            clay.add(P(second_axis, ax_num))

min_x = min(item.x for item in clay)
max_x = max(item.x for item in clay)
min_y = min(item.y for item in clay)
max_y = max(item.y for item in clay)


def spread(cur_pos, still, flow, spring):
    cur_eval = set([cur_pos])
    left_edge = cur_pos
    right_edge = cur_pos

    while left_edge + L not in clay and (left_edge + D in clay or left_edge + D in still):
        left_edge += L
        cur_eval.add(left_edge)

    while right_edge + R not in clay and (right_edge + D in clay or right_edge + D in still):
        right_edge += R
        cur_eval.add(right_edge)

    if left_edge + L in clay and right_edge + R in clay:
        if cur_pos in flow:
            flow.remove(cur_pos)
        still |= cur_eval
    else:
        if right_edge + R not in clay:
            spring.add(right_edge)
        if left_edge + L not in clay:
            spring.add(left_edge)
        flow |= cur_eval


while spring:
    cur_spot = spring.pop()
    # print_map(min_x, max_x, min_y, max_y)

    cur_spot += D
    while cur_spot.y <= max_y:
        # try to drop
        if cur_spot not in flow and \
           cur_spot not in clay and \
           cur_spot not in still:
            flow.add(cur_spot)
            cur_spot += D
        elif cur_spot in clay or \
                cur_spot in still:
            cur_spot += U
            spread(cur_spot, still, flow, spring)
        elif cur_spot in flow:
            break

        # print_map(min_x, max_x, min_y, max_y)

print_map(min_x, max_x, min_y, max_y)
count = 0
for water in flow.union(still):
    x, y = water
    if y <= max_y and y >= min_y:
        count += 1
print(count)
count = 0
for water in still:
    x, y = water
    if y <= max_y and y >= min_y:
        count += 1
print(count)
