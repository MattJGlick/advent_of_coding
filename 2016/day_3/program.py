with open('input_file.txt') as inputfile:
    rows = [map(int, line.strip().split()) for line in inputfile]

def get_good_triangles(all_triangles):
    good_triangles = 0
    for triangle in all_triangles:
        triangle = sorted(triangle)

        if sum(triangle[:-1]) > triangle[-1]:
            good_triangles += 1

    return good_triangles

### PART 1
print get_good_triangles(rows)

### PART 2
new_triangles = []
index = 0
while index != len(rows):
    new_triangles += zip(*rows[index:index+3])
    index += 3

print get_good_triangles(new_triangles)
