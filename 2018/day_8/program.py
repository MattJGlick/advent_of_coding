with open('input_file.txt') as inputfile:
    numbers = [int(num) for num in inputfile.read().split()]


def get_metadata(numbers):
    total_metadata = 0
    child_values = []
    num_c = numbers[0]
    num_m = numbers[1]
    numbers = numbers[2:]

    for cur_child in range(num_c):
        numbers, metadata, value = get_metadata(numbers)
        total_metadata += metadata
        child_values.append(value)

    metadata = numbers[:num_m]
    total_metadata += sum(metadata)

    if num_c == 0:
        return numbers[num_m:], total_metadata, total_metadata
    else:
        value = 0
        for m_d in metadata:
            if m_d <= len(child_values):
                value += child_values[m_d - 1]

        return numbers[num_m:], total_metadata, value


print(get_metadata(numbers)[1])
print(get_metadata(numbers)[2])
