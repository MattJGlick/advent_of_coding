import copy

with open('input_file.txt') as inputfile:
    grid = [list(line.strip()) for line in inputfile]

grid = [[False if spot == "." else True for spot in row] for row in grid]
max_x = len(grid) - 1
max_y = len(grid[max_x]) - 1

def get_new_state(grid, x, y):
    if (x, y) in [(0, 0), (0, max_y), (max_x, 0), (max_x, max_y)]:
        return True

    on_count = 0

    for dx in [-1, 0, 1]:
        nx = x + dx
        for dy in [-1, 0, 1]:
            ny = y + dy

            if ((x, y) != (nx, ny) 
                and (nx >= 0 and nx <= max_x) 
                and (ny >= 0 and ny <= max_y)):

                on_count += grid[nx][ny]

    if grid[x][y]:
        if on_count not in [2, 3]:
            return False
    elif not grid[x][y]:
        if on_count == 3:
            return True

    return grid[x][y]

new_grid = copy.deepcopy(grid)
for _ in range(100):
    grid = copy.deepcopy(new_grid)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            new_grid[x][y] = get_new_state(grid, x, y)

print sum(map(sum, new_grid))
