puzzle_presents = 33100000 / 10

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

house = 1
while True:
    if sum(factors(house)) > puzzle_presents:
        print house
        break

    house += 1

# PART 2
puzzle_presents = 33100000 / 11

house = 1
while True:
    if sum(factor for factor in factors(house) if house / factor <= 50) > puzzle_presents:
        print house
        break

    house += 1
