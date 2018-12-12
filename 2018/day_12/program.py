with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

cur_state = rows[0].split(':')[1].strip()
cur_state = [True if x == '#' else False for x in list(cur_state)]

instructions = rows[2:]
ins = []
for instruction in instructions:
    code, output = instruction.split(' => ')
    parsed_code = [True if x == '#' else False for x in list(code)]
    if output == '#':
        ins.append(parsed_code)

print('cur_state', ''.join(['#' if x else '.' for x in cur_state]))

zero = 0
for state in range(0, 20):
    new_state = []

    diff = -3
    for cur_index in range(0, len(cur_state) + 2):
        to_check = []
        for position in range(0, 5):
            cur_eval_pos = cur_index + position + diff

            if cur_eval_pos < 0 or cur_eval_pos > len(cur_state) - 1:
                is_plant = False
            else:
                is_plant = cur_state[cur_eval_pos]

            to_check.append(is_plant)

        new_state.append(to_check in ins)

        if cur_index < 1:
            zero += 1

    cur_state = new_state

    plant_sum = 0
    for index, is_plant in enumerate(cur_state):
        if is_plant:
            plant_sum += (index - zero)

    print('at state', state + 1, 'total', plant_sum)

# PART 2
#
# Increased the 20 to 50billion and realized a pattern occurs. every new state adds 42. So did math from there on
#
