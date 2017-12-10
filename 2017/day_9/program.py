with open('input_file.txt') as inputfile:
    input_row = [line.strip() for line in inputfile][0]

import re
def remove_not(string):
    return re.sub('!.', '', string)

def handle_garbage(string):
    return re.sub('<.*?>', '', string)

input_row = remove_not(input_row)

garbage = False
garbage_count = 0
for char in input_row:
    if garbage:
        garbage_count += 1
    if char == "<":
        garbage = True
    if char == ">":
        garbage = False
        garbage_count -= 1

input_row = handle_garbage(input_row)
input_row = input_row.replace(",", "")

def count(string):
    count = 0
    counter = 1
    for char in string:
        if char == "{":
            counter += 1
        else:
            counter -= 1
            count += counter
    return count

print count(input_row)
print garbage_count
