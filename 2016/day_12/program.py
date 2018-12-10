with open('input_file.txt') as inputfile:
    instructions = [line.strip().split() for line in inputfile]

regs = {
    'a': 0,
    'b': 0,
    'c': 1,  # part 1 just set this to 0
    'd': 0
}

index = 0
while index != len(instructions):
    inc = 1
    instruction = instructions[index]
    op, x = instruction[0], instruction[1]

    if op == 'cpy':
        y = instruction[2]
        if x.isdigit():
            regs[y] = int(x)
        else:
            regs[y] = regs[x]
    elif op == 'inc':
        regs[x] += 1
    elif op == 'dec':
        regs[x] -= 1
    elif op == 'jnz':
        y = instruction[2]
        if (x.isdigit() and int(x) > 0) or (regs[x] > 0):
            inc = int(y)

    index += inc
print(regs)
