with open('input_file.txt') as inputfile:
    array = [int(line.strip()) for line in inputfile]

        # [array[index] += 1 for index, value in array if array[index]]
    index = 0
    prev_index = 0
    steps = 0
    while index >= 0 and index < len(array):
        prev_index = index
        index += array[index]
        array[prev_index] += 1
        steps += 1

    print steps

with open('input_file.txt') as inputfile:
    array = [int(line.strip()) for line in inputfile]

    index = 0
    prev_index = 0
    steps = 0
    while index >= 0 and index < len(array):
        prev_index = index
        index += array[index]
        if array[prev_index] >= 3:
            array[prev_index] -= 1
        else:
            array[prev_index] += 1
        steps += 1

    print steps
