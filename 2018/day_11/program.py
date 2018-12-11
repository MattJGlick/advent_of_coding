import numpy as np

grid = []
max_grid_size = 300
grid_id = 1788

for x in range(1, max_grid_size + 1):
    row = []
    for y in range(1, max_grid_size + 1):
        rack_id = x + 10
        power = rack_id * y
        power += grid_id
        power *= rack_id
        power = (power // 100) % 10
        power -= 5
        row.append(power)
    grid.append(row)
grid = np.array(grid)

max_power = -999999
for x in range(0, max_grid_size - 1):
    for y in range(0, max_grid_size - 1):
        this_max = np.sum(grid[x:x+3, y:y+3])

        if this_max > max_power:
            max_power = this_max
            max_pos = (x + 1, y + 1)

print(max_pos)

max_power = -999999
for x in range(0, max_grid_size - 1):
    for y in range(0, max_grid_size - 1):
        for square_size in range(1, max_grid_size - (max(x, y))):
            cur_power = np.sum(grid[x:x+square_size, y:y+square_size])

            if cur_power > max_power:
                max_power = cur_power
                max_pos = (x + 1, y + 1)
                max_square_size = square_size

print(max_power, max_pos, max_square_size)
