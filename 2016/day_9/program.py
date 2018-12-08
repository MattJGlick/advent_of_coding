with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

total = 0
for row in rows:
    output = ''
    i = 0
    in_data = []
    while i != len(row):
        if row[i] == '(' and i not in in_data:
            num_letters = ''
            i += 1

            while row[i] != 'x':
                num_letters += row[i]
                i += 1

            i += 1

            times = ''
            while row[i] != ')':
                times += row[i]
                i += 1

            num_letters = int(num_letters)
            times = int(times)
            in_data += range(i+1, i+1+num_letters)

            output += row[i+1:i+1+num_letters] * (times - 1)
        else:
            output += row[i]
        i += 1
    total += len(output)

print(total)


def remove_parens(string):
    total_length = 0
    if '(' not in string:
        return len(string)
    while '(' in string:
        left = string.find('(')
        right = string.find(')')
        num_l, times = map(int, string[left+1:right].split('x'))
        total_length += remove_parens(string[right+1:right+1+num_l]) * times + left
        string = string[right+1+num_l:]
    return total_length + len(string)


for row in rows:
    print(remove_parens(row))





