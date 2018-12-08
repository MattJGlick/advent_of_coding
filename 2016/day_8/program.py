with open('input_file.txt') as inputfile:
    rows = [line for line in inputfile]

grid = []
max_rows = 6
max_columns = 50
for row in rows:
    if 'rect' in row:
        _, dims = row.split()
        max_x, max_y = map(int, dims.split('x'))

        for x in range(max_x):
            for y in range(max_y):
                if (x, y) in grid:
                    grid.remove((x, y))
                else:
                    grid.append((x, y))

    else:
        rotate = row.split()
        col_or_row = rotate[1]
        index = int(rotate[2].split('=')[1])
        value = int(rotate[4])

        for i, point in enumerate(grid):
            cur_x, cur_y = point
            if col_or_row == 'column':
                if cur_x == index:
                    grid[i] = (cur_x, (cur_y + value) % max_rows)
            if col_or_row == 'row':
                if cur_y == index:
                    grid[i] = ((cur_x + value) % max_columns,  cur_y)

    print('--------------------------------')
    for y in range(max_rows):
        for x in range(max_columns):
            if (x, y) in grid:
                print('X', end="")
            else:
                print('-', end="")

        print('')

print(len(grid))
