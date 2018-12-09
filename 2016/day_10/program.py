from collections import defaultdict
with open('input_file.txt') as inputfile:
    rows = [line.strip().split() for line in inputfile]

robots = defaultdict(list)
outputs = {}
instructions = {}

for row in rows:
    if 'value' in row:
        value, bot = map(int, (row[1], row[5]))
        robots[bot].append(value)
    else:
        bot_1, type_2, num_2, type_3, num_3 = int(row[1]), row[5], int(row[6]), row[10], int(row[11])
        instructions[bot_1] = ((type_2, num_2), (type_3, num_3))


to_find = (17, 61)
while True:
    two_products = [bot for bot, products in robots.items() if len(products) == 2]
    if two_products:
        cur_robot = two_products[0]
    else:
        break

    low, high = sorted(robots[cur_robot])
    robots[cur_robot] = []
    ((type_2, num_2), (type_3, num_3)) = instructions[cur_robot]

    if (low, high) == to_find:
        final = cur_robot

    if type_2 == 'bot':
        robots[num_2].append(low)
    else:
        outputs[num_2] = low

    if type_3 == 'bot':
        robots[num_3].append(high)
    else:
        outputs[num_3] = high

print(final)
print(outputs[0] * outputs[1] * outputs[2])
