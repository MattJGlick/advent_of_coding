from collections import defaultdict
import itertools

cities = defaultdict(dict)
with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()

        dirs, dist = map(lambda s: s.strip(), line.split("="))
        dep, arr = dirs.split(" to ")

        cities[dep][arr] = int(dist)
        cities[arr][dep] = int(dist)
        unique = set(cities.keys())

    shortest = 9999999999999999999999999
    longest = 0

    for route in itertools.permutations(unique, len(unique)):
        zipped = zip(route[:-1], route[1:])
        cur_dist = sum(cities[x][y] for x,y in zipped)
        shortest = min(cur_dist, shortest)
        longest = max(cur_dist, longest)

print shortest
print longest

