from collections import Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

num_2s = 0
num_3s = 0
for row in rows:
    counts = Counter(list(row))
    if 2 in counts.values():
        num_2s += 1
    if 3 in counts.values():
        num_3s += 1

print(num_2s * num_3s)

for i_1, row_1 in enumerate(rows):
    for i_2, row_2 in enumerate(rows):
        if i_1 != i_2:
            for cur_i in range(len(row_1)):
                str_1 = row_1[:cur_i - 1] + row_1[cur_i:]
                str_2 = row_2[:cur_i - 1] + row_2[cur_i:]

                if str_1 == str_2:
                    print(str_1)
