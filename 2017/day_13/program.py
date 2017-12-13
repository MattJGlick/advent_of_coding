with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split(": ") for line in inputfile]
    walls = {int(time): int(height) for time, height in input_rows}

    part_1 = sum(time * walls[time] for time in walls if (time % ((walls[time] - 1) * 2) == 0))
    print part_1

    delay = 0
    found = False
    while not found:
        found = True
        for time in walls:
            if (time + delay) % ((walls[time] - 1) * 2) == 0:
                found = False
                delay += 1
                break;

    print delay

