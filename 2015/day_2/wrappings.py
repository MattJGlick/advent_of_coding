def get_paper(w, l, h):
    areas = [w*l, w*h, l*h]

    return min(areas) + sum(map(lambda x: x*2, areas))

def get_ribbon(w, l, h):
    bow = w * l * h
    dims = sorted([w, l, h])

    return bow + (dims[0] * 2) + (dims[1] * 2)

paper_total = 0
ribbon_total = 0

with open('input_file.txt') as inputfile:
    for line in inputfile:
        dims = line.rstrip().split("x")
        paper_total += get_paper(int(dims[0]), int(dims[1]), int(dims[2]))
        ribbon_total += get_ribbon(int(dims[0]), int(dims[1]), int(dims[2]))

print paper_total
print ribbon_total
