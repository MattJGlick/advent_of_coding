import re
with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

pos = []
vel = []
for row in rows:
    x, y, m_x, m_y = map(int, re.findall(r'-?\d+', row))

    pos.append((x, y))
    vel.append((m_x, m_y))

for sec in range(1, 1000000):
    for index in range(len(pos)):
        cur_x, cur_y = pos[index]
        m_x, m_y = vel[index]
        pos[index] = (cur_x + m_x, cur_y + m_y)

    min_x = min([x for x, y in pos])
    max_x = max([x for x, y in pos])
    min_y = min([y for x, y in pos])
    max_y = max([y for x, y in pos])

    if -200 < min_x < 200 and -200 < max_y < 200 and -200 < min_y < 200 and -200 < max_y < 200:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in pos:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print(sec)
        import pdb; pdb.set_trace()  # noqa
