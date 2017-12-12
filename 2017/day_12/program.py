#### PART 1

def get_neighbors(input_rows, value):
    mappings = {}
    for row in input_rows:
        left = row[0].strip()
        rights = [x.strip() for x in row[1].split(",")]
        mappings[left] = rights

    def find_neighbor(value, neighbors):
        neighbors.add(value)
        for right in mappings[value]:
            if right not in neighbors:
                neighbors |= find_neighbor(right, neighbors)
        return neighbors

    return len(find_neighbor(value, set()))


#### PART 2

def get_groups(input_rows):
    mappings = {}
    for row in input_rows:
        left = row[0].strip()
        rights = [x.strip() for x in row[1].split(",")]
        mappings[left] = rights

    def find_neighbor(value, neighbors):
        neighbors.add(value)
        for right in mappings[value]:
            if right not in neighbors:
                neighbors |= find_neighbor(right, neighbors)
        return neighbors

    found_neighbors = set()
    num_groups = 0
    for num in mappings:
        if num not in found_neighbors:
            found_neighbors |= find_neighbor(num, set())
            num_groups += 1

    return num_groups

with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split('<->') for line in inputfile]
    print get_neighbors(input_rows, '0')
    print get_groups(input_rows)
