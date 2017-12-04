def get_new(line):
    cur_char = line[0]
    count = 0
    new_string = ""
    for char in line:
        if char == cur_char:
            count += 1
        else:
            new_string += str(count) + cur_char
            cur_char = char
            count = 1

    new_string += str(count) + cur_char
    return new_string

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()

        for _ in range(0, 50):
            line = get_new(line)

print len(line)
