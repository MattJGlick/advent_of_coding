import re
import numpy as np
from itertools import permutations
with open('input_file.txt') as inputfile:
    input_rows = [line.strip() for line in inputfile]

ingreds = {}
for row in input_rows:
    x = re.match(r'(\w*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', row)
    ingreds[x.group(1)] = map(int, list(x.group(2,3,4,5,6)))

amounts = [perm for perm in permutations(range(0, 101), len(ingreds.keys())) if sum(perm) == 100]
ingreds_zipped = zip(*ingreds.values())

print max([np.prod(np.array([sum(np.array(s) * np.array(amount)) if sum(np.array(s) * np.array(amount)) > 0 else 0 for s in ingreds_zipped[:-1]])) for amount in amounts])

highest_score = 0
for amount in amounts:
    current_props = []
    for ingred_zipped in ingreds_zipped[:-1]:
        if sum(np.array(ingred_zipped) * np.array(amount)) > 0 and sum(np.array(ingreds_zipped[-1]) * np.array(amount)) == 500:
            current_props.append(sum(np.array(ingred_zipped) * np.array(amount)))
    highest_score = max(highest_score, np.prod(current_props))
print highest_score

