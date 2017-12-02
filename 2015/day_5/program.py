from collections import Counter
import re

def is_str_nice(input_str):
    vowels = ["a", "e", "i", "o", "u"]
    three_v = sum([input_str.count(vowel) for vowel in vowels]) >= 3

    regexp = re.compile(r"(.)\1")
    contains_double = bool(re.search(regexp, input_str))

    bad_strings = ["ab", "cd", "pq", "xy"]
    no_bad_string = not any(x in input_str for x in bad_strings)

    return three_v and contains_double and no_bad_string

def is_str_nice_2(input_str):
    regexp = re.compile(r"(.{2}).*\1")
    repeated = bool(re.search(regexp, input_str))

    regexp = re.compile(r"(.)(.)\1")
    contains_double = bool(re.search(regexp, input_str))

    return repeated and contains_double

count = 0
count_2 = 0

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()

        if is_str_nice(line):
            count += 1
        if is_str_nice_2(line):
            count_2 += 1

print count
print count_2
