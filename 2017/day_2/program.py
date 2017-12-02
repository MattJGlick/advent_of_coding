def calc_diff(array):
    return max(array) - min(array)

def get_even_div(array):
    for x in array:
        for y in array:
            if x != y and x % y == 0:
                return x / y

sum_1 = 0
sum_2 = 0

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = map(int, line.rstrip().split())
        sum_1 += calc_diff(line)
        sum_2 += get_even_div(line)

print sum_1
print sum_2
        

