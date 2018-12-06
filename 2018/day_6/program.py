from collections import defaultdict
with open('input_file.txt') as inputfile:
    locations = [[int(x) for x in line.strip().split(', ')] for line in inputfile]

max_x = max([x[0] for x in locations])
max_y = max([x[1] for x in locations])

desired_distance = 10000
sizes = defaultdict(int)
bad_letters = set()
in_zone = 0

for x in range(0, max_x + 1):
    for y in range(0, max_y + 1):

        min_d = 100000
        total_d = 0
        for index, location in enumerate(locations):
            distance = abs(x - location[0]) + abs(y - location[1])
            total_d += distance

            if distance < min_d:
                min_d = distance
                min_letter = index
            elif distance == min_d:
                min_letter = '-'

        if x == 0 or x == max_x or y == 0 or y == max_y:
            bad_letters.add(min_letter)

        sizes[min_letter] += 1

        if total_d < desired_distance:
            in_zone += 1

for bad_letter in bad_letters:
    del sizes[bad_letter]

print(max(sizes.values()))
print(in_zone)
