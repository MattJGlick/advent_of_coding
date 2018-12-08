import re
import regex

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

good_abba = r'(\w)(\w)\2(?!\2)\1'
bad_abba = r'\[\w*((\w)(\w)\3(?!\3)\2)\w*\]'


def is_abba(string):
    if re.search(bad_abba, string) is not None:
        return False
    if re.search(good_abba, string) is not None:
        return True
    return False


print sum([is_abba(row) for row in rows])
aba = r'(\w)(\w)\1'


def is_ssl(string):
    parts = re.split(r'\[|\]', string)
    insides = parts[1::2]
    outsides = parts[::2]

    for outside in outsides:
        for occ in regex.findall(aba, outside, overlapped=True):
            for inside in insides:
                if occ[::-1] in regex.findall(aba, inside, overlapped=True):
                    return True

    return False

print is_ssl("aba[bab]xyz")
print sum([is_ssl(row) for row in rows])
