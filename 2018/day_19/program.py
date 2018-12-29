import re

from collections import defaultdict


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


functions = {
    'addr': addr,
    'banr': banr,
    'setr': setr,
    'gtrr': gtrr,
    'addi': addi,
    'bani': bani,
    'seti': seti,
    'eqir': eqir,
    'mulr': mulr,
    'borr': borr,
    'gtir': gtir,
    'eqri': eqri,
    'muli': muli,
    'bori': bori,
    'gtri': gtri,
    'eqrr': eqrr
}

lines = open('input_file.txt').read().strip().split('\n')
ip_reg = int(re.findall(r'\d+', lines[0])[0])
instructions = [l.strip().split() for l in lines[1:]]

regs = [0] * 6
ip = 0
while ip < len(instructions):
    instruction = instructions[ip]
    op = instruction[0]
    alpha = int(instruction[1])
    beta = int(instruction[2])
    charlie = int(instruction[3])

    regs[ip_reg] = ip
    func = functions[op]
    func(regs, alpha, beta, charlie)
    ip = regs[ip_reg]
    ip += 1

print(regs[0])
print(1 + 431 + 24481 + 10551311)
