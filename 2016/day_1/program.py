with open('input_file.txt') as inputfile:
    vectors = [line.strip().split(", ") for line in inputfile][0]

    point_dir = 0
    points = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    loc = [0, 0]
    for vector in vectors:
        direction, distance = vector[0], int(vector[1:])

        point_dir = ((point_dir + (1 if direction == 'R' else -1)) % 4)

        point = points[point_dir]
        loc = ((point[0] * distance) + loc[0], (point[1] * distance) + loc[1])
        
    print sum(map(abs, loc))


    point_dir = 0
    loc = [0, 0]
    found_locs = []
    not_found = True
    for vector in vectors:
        direction, distance = vector[0], int(vector[1:])

        point_dir = ((point_dir + (1 if direction == 'R' else -1)) % 4)
        point = points[point_dir]

        for _ in range(distance):
            loc = (point[0] + loc[0], point[1] + loc[1])

            if loc in found_locs and not_found:
                not_found = False
                print sum(map(abs, loc))
            found_locs.append(loc)
