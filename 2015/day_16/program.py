import re

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

sues = {}
for row in rows:
    regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    m = re.match(regex, row)

    sue = {
        m.group(2): int(m.group(3)),
        m.group(4): int(m.group(5)),
        m.group(6): int(m.group(7))
    }

    sues[int(m.group(1))] = sue

good_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def check(sue):
    for key, count in sue.items():
        if key in ["cats", "trees"]:
            if good_sue[key] >= count:
                return False
        elif key in ["pomeranians", "goldfish"]:
            if good_sue[key] <= count:
                return False
        else:
            if good_sue[key] != count:
                return False
    return True

for sue, sue_details in sues.items():
    if check(sue_details):
        print sue
        break
