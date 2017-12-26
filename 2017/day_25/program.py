import re
with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

state = re.match(r'Begin in state (\w).', rows[0]).group(1)
num_steps = int(re.match(r'Perform a diagnostic checksum after (\d+) steps.', rows[1]).group(1))

states = {}
for index, row in enumerate(rows):
    if re.match(r'In state (\w):', row) is not None:
        cur_state = re.match(r'In state (\w):', row).group(1)
        states[cur_state] = []
        for jump in [0, 4]:
            write = int(re.match(r'- Write the value (\d).', rows[index+jump+2]).group(1))
            move = re.match(r'- Move one slot to the (left|right).', rows[index+jump+3]).group(1)
            move = 1 if move == "right" else -1
            new_state = re.match(r'- Continue with state (\w).', rows[index+jump+4]).group(1)

            states[cur_state].append((write, move, new_state))

# I originally hardcoded all of these for purely speed, went back and used regex to make it better
# states = {
#     "A": [(1, 1, "B"), (0, -1, "C")],
#     "B": [(1, -1, "A"), (1, 1, "C")],
#     "C": [(1, 1, "A"), (0, -1, "D")],
#     "D": [(1, -1, "E"), (1, -1, "C")],
#     "E": [(1, 1, "F"), (1, 1, "A")],
#     "F": [(1, 1, "A"), (1, 1, "E")],
# }

tape = {}
index = 0

for step in range(num_steps):
    if index not in tape:
        tape[index] = 0

    value = tape[index]
    new_value, move, new_state = states[state][value]

    tape[index] = new_value
    index += move
    state = new_state
        
print sum(tape.values())
