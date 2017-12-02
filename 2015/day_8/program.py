import re

def chars_per_line(input_str):
    trimmed = input_str[1:-1]

    decoded = trimmed.decode('string_escape')

    return len(input_str) - len(decoded)

def chars_per_line_2(input_str):
    return (len(input_str.replace('\\', '\\\\').replace('"','\\"')) + 2) - len(input_str)

total = 0

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()
        total += chars_per_line_2(line)

print total
