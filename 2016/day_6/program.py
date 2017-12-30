from collections import Counter

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

# PART 1
print ''.join(Counter(list(group)).most_common()[0][0] for group in zip(*rows))

# PART 2
print ''.join(Counter(list(group)).most_common()[-1][0] for group in zip(*rows))
