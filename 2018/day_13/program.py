from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter

with open('input_file.txt') as inputfile:
    rows = [list(line.strip()) for line in inputfile]

carts = []
vels = []
axes = []
turns = []
for y, row in enumerate(rows):
    for x, item in enumerate(row):
        if item == '>':
            carts.append((x, y))
            vels.append(1)
            rows[y][x] = '-'
            axes.append(0)
            turns.append(0)
        elif item == 'v':
            carts.append((x, y))
            vels.append(1)
            rows[y][x] = '|'
            axes.append(1)
            turns.append(0)
        elif item == '<':
            carts.append((x, y))
            vels.append(-1)
            rows[y][x] = '-'
            axes.append(0)
            turns.append(0)
        elif item == '^':
            carts.append((x, y))
            vels.append(-1)
            rows[y][x] = '|'
            axes.append(1)
            turns.append(0)


disabled = set()
part_1 = True
for _ in range(100000000):
    moved = set()
    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if (x, y) in carts:
                cart_num = carts.index((x, y))
                if cart_num in moved or cart_num in disabled:
                    continue
                vel = vels[cart_num]
                axis = axes[cart_num]
                turn = turns[cart_num]

                new_y = y
                new_x = x
                new_vel = vel
                new_axis = axis
                new_turn = turn

                # check for next move
                if item == '|':
                    new_y += vel
                if item == '-':
                    new_x += vel
                if item == '/':
                    if vel > 0:
                        if axis == 0:
                            new_y = y - 1
                            new_axis = 1
                            new_vel = -1
                        else:
                            new_x = x - 1
                            new_axis = 0
                            new_vel = -1
                    else:
                        if axis == 0:
                            new_y = y + 1
                            new_axis = 1
                            new_vel = 1
                        else:
                            new_x = x + 1
                            new_axis = 0
                            new_vel = 1
                if item == '\\':
                    if vel > 0:
                        if axis == 0:
                            new_y = y + 1
                            new_axis = 1
                            new_vel = 1
                        else:
                            new_x = x + 1
                            new_axis = 0
                            new_vel = 1
                    else:
                        if axis == 0:
                            new_y = y - 1
                            new_axis = 1
                            new_vel = -1
                        else:
                            new_x = x - 1
                            new_axis = 0
                            new_vel = -1
                if item == '+':
                    if vel > 0:
                        if axis == 0:
                            if turn == 0:
                                new_y = y - 1
                                new_axis = 1
                                new_vel = -1
                                new_turn = 1
                            if turn == 1:
                                new_x = x + 1
                                new_turn = 2
                            if turn == 2:
                                new_y = y + 1
                                new_axis = 1
                                new_vel = 1
                                new_turn = 0
                        else:
                            if turn == 0:
                                new_x = x + 1
                                new_axis = 0
                                new_vel = 1
                                new_turn = 1
                            if turn == 1:
                                new_y = y + 1
                                new_turn = 2
                            if turn == 2:
                                new_x = x - 1
                                new_axis = 0
                                new_vel = -1
                                new_turn = 0
                    else:
                        if axis == 0:
                            if turn == 0:
                                new_y = y + 1
                                new_axis = 1
                                new_vel = 1
                                new_turn = 1
                            if turn == 1:
                                new_x = x - 1
                                new_turn = 2
                            if turn == 2:
                                new_y = y - 1
                                new_axis = 1
                                new_vel = -1
                                new_turn = 0
                        else:
                            if turn == 0:
                                new_x = x - 1
                                new_axis = 0
                                new_vel = -1
                                new_turn = 1
                            if turn == 1:
                                new_y = y - 1
                                new_turn = 2
                            if turn == 2:
                                new_x = x + 1
                                new_axis = 0
                                new_vel = 1
                                new_turn = 0

                crashed = False
                if (new_x, new_y) in carts:
                    if part_1:
                        print('Part 1:', new_x, new_y)
                        part_1 = False
                    if carts.index((new_x, new_y)) not in disabled:
                        crashed = True

                carts[cart_num] = (new_x, new_y)
                vels[cart_num] = new_vel
                axes[cart_num] = new_axis
                turns[cart_num] = new_turn
                moved.add(cart_num)

                if crashed:
                    indices = [i for i, pos in enumerate(carts) if pos == (new_x, new_y)]
                    disabled = disabled.union(set(indices))

    if len(disabled) == len(carts) - 1:
        remaining_cart = (set(range(0, len(carts))) - disabled).pop()
        print('Part 2', carts[remaining_cart])
