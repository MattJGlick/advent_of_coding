import re

from collections import defaultdict

before = []
instructions = []
after = []

lines, program = open('input_file.txt').read().strip().split('\n\n\n\n')
lines = [l.strip() for l in lines.split('\n')]
program = [p.strip() for p in program.split('\n')]

for line in lines:
    numbers = list(map(int, re.findall(r'\d+', line)))
    if numbers:
        if line[0] == 'B':
            before.append(numbers)
        if line[0].isdigit():
            instructions.append(numbers)
        if line[0] == 'A':
            after.append(numbers)


def addr(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] + regs[beta]


def addi(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] + beta


def mulr(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] * regs[beta]


def muli(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] * beta


def banr(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] & regs[beta]


def bani(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] & beta


def borr(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] | regs[beta]


def bori(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha] | beta


def setr(regs, alpha, beta, charlie):
    regs[charlie] = regs[alpha]


def seti(regs, alpha, beta, charlie):
    regs[charlie] = alpha


def gtir(regs, alpha, beta, charlie):
    if alpha > regs[beta]:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


def gtri(regs, alpha, beta, charlie):
    if regs[alpha] > beta:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


def gtrr(regs, alpha, beta, charlie):
    if regs[alpha] > regs[beta]:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


def eqir(regs, alpha, beta, charlie):
    if alpha == regs[beta]:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


def eqri(regs, alpha, beta, charlie):
    if regs[alpha] == beta:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


def eqrr(regs, alpha, beta, charlie):
    if regs[alpha] == regs[beta]:
        regs[charlie] = 1
    else:
        regs[charlie] = 0


functions = [
    addr, banr, setr, gtrr,
    addi, bani, seti, eqir,
    mulr, borr, gtir, eqri,
    muli, bori, gtri, eqrr
]

above_three = 0
possible_operations = defaultdict(set)
for index, instruction in enumerate(instructions):
    cur_state, new_state = before[index], after[index]
    o_id, alpha, beta, charlie = instruction

    count = []
    for func in functions:
        regs = list(cur_state)
        func(regs, alpha, beta, charlie)

        if new_state == regs:
            possible_operations[o_id].add(func)
            count.append(func)

    if len(count) >= 3:
        above_three += 1

print('Part 1:', above_three)

operations = defaultdict(set)
while len(operations) != len(possible_operations):
    for o_id, funcs in possible_operations.items():
        if len(funcs) == 1:
            operations[o_id] = funcs
    for o_id, funcs in operations.items():
        for possible_o_id, possible_funcs in possible_operations.items():
            if o_id != possible_o_id:
                possible_funcs.difference_update(funcs)

operations = {k: operations[k].pop() for k in operations}

regs = [0, 0, 0, 0]
for instruction in program:
    ins, alpha, beta, charlie = list(map(int, re.findall(r'\d+', instruction)))

    operations[ins](regs, alpha, beta, charlie)
print('Part 2:', regs[0])
