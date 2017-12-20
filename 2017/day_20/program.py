import re
with open('input_file.txt') as inputfile:
    input_rows = [line.strip() for line in inputfile]

particles = []
for row in input_rows:
    if row == "":
        continue
    x = re.match(r'p=<(.*)>, v=<(.*)>, a=<(.*)>', row)
    p, v, a = map(lambda x: map(int, x.split(",")), list(x.group(1,2,3)))
    particles.append((p, v, a))

while True:
    closest = None
    seen = []
    closest_man = 99999999999999999999999999999
    for index, part in enumerate(particles):
        p, v, a = part
        
        for i in range(3):
            v[i] += a[i]
            p[i] += v[i]

        man = sum(map(abs, p))

        if man < closest_man:
            closest = index
            closest_man = man

        particles[index] = (p, v, a)

    print closest

#### PART 2

while True:
    seen = {}
    collided = []
    for index, part in enumerate(particles):
        p, v, a = part

        for i in range(3):
            v[i] += a[i]
            p[i] += v[i]

        particles[index] = (p, v, a)

        if tuple(p) in seen.keys():
            collided.append(seen[tuple(p)])
            collided.append(index)
        else:
            seen[tuple(p)] = index

    for index in sorted(set(collided), reverse=True):
        del particles[index]

    print len(particles)

