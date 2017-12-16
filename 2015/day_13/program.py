import itertools
with open('input_file.txt') as inputfile:
    input_rows = [line.strip().strip(".").split() for line in inputfile]
    hap_map = {}
    seating = []
    for row in input_rows:
        pos = -1 if row[2] == "lose" else 1
        seating.append(row[0])
        seating.append(row[10])
        hap_map[(row[0], row[10])] = int(row[3]) * pos

    seating = list(set(seating))

    seating.append("me")
    for person in seating:
        hap_map[(person, "me")] = 0
        hap_map[("me", person)] = 0

    best_hap = None
    for perm in itertools.permutations(seating):
        happiness = 0
        for i in range(len(seating)):
            happiness += hap_map[(perm[i], perm[(i + 1) % len(seating)])]
            happiness += hap_map[(perm[i], perm[i - 1])]
        best_hap = max(happiness, best_hap)

print best_hap
