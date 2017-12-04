count = 0
sorted_count = 0
with open('input_file.txt') as inputfile:
    for line in inputfile:
        uniques = set()
        uniques_sorted = set()
        line = line.rstrip()
        words = line.split()

        for word in words:
            uniques.add(word)
            uniques_sorted.add(''.join(sorted(word)))

        if len(uniques) == len(words):
            count += 1

        if len(uniques_sorted) == len(words):
            sorted_count += 1


print count
print sorted_count
