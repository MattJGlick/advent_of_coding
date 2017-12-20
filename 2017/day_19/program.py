with open('input_file.txt') as inputfile:
    m = [line.strip('\n') for line in inputfile]
    
x = 0
y = m[0].index("|")

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
current_dir = 0
letters = ""
steps = 0

while m[x][y] != " ":
    point = m[x][y]

    if point.isalpha():
        letters += point
    elif point == "+":
        for index, direction in enumerate(dirs):
            nx = x + direction[0]
            ny = y + direction[1]
            if index == (current_dir + 2) % 4:
                continue
            if nx >= len(m) or ny >= len(m[nx]):
                continue
            if m[nx][ny] != " ":
                current_dir = index
                break

    x += dirs[current_dir][0]
    y += dirs[current_dir][1]
    steps += 1

print letters
print steps
