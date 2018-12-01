with open('input_file.txt') as inputfile:
    rows = [line.strip().split() for line in inputfile]

items = [int(row[0]) for row in rows]
print(sum(items))

freqs = set()
freq = 0
found = False
while not found:
    for item in items:
        freq += item

        if freq not in freqs:
            freqs.add(freq)
        else:
            found = True
            break
print(freq)
