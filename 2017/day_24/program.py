with open('input_file.txt') as inputfile:
    bridges = [map(int, line.strip().split('/')) for line in inputfile]

lengths = []
def find_next(port, remaining, cur_total, length):
    lengths.append([length, cur_total])

    for next_port in remaining:
        x, y = next_port

        if x == port or y == port:
            new_remaining = [new_bridge for new_bridge in remaining if new_bridge != next_port]
            find_next(x if y == port else y, new_remaining, cur_total + sum(next_port), length + 1)

for bridge in bridges:
    x, y = bridge
    if x == 0 or y == 0:
        remaining = [new_bridge for new_bridge in bridges if new_bridge != bridge]
        find_next(x if y == 0 else y, remaining, sum(bridge), 1)

print max([length[1] for length in lengths])
longest = max([length[0] for length in lengths])
print max([length[1] for length in lengths if length[0] == longest])
