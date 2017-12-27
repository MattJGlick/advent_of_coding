import re
from collections import Counter

with open('input_file.txt') as inputfile:
    rooms = [line.strip() for line in inputfile]

real_rooms = 0
for room in rooms:
    regex = r'([a-z*-]*)(\d*)\[(\w*)]'
    string, sector, check_sum = re.match(regex, room).group(1, 2, 3)
    sector = int(sector)
    string = string.replace("-", "")

    cnts = Counter(''.join(sorted(string))).most_common(5)
    if not any(cnt for cnt in cnts if cnt[0] not in check_sum):
        real_rooms += sector

    shifted_string = ''.join([chr(((ord(letter) - 97) + sector) % 26 + 97) for letter in string])
    if shifted_string.startswith("north"):
        print shifted_string, sector

print real_rooms
