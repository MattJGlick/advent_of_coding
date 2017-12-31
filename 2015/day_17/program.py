import itertools

with open('input_file.txt') as inputfile:
    jars = [int(line.strip()) for line in inputfile]

total = 0
min_total = 0
for index in range(len(jars)):
    sub_total = 0
    for perm in itertools.combinations(jars, index):
        if sum(perm) == 150:
            sub_total += 1
    if not min_total and sub_total:
        min_total = sub_total
    total += sub_total
print total
print min_total
