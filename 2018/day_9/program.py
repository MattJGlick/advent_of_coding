from blist import blist
from collections import defaultdict

numbers = blist([0])
cur_index = 0
cur_player = 1
num_players = 446
# part 1 is just max_marble / 100
max_marble = 7152200
scores = defaultdict(int)

for num in range(1, max_marble + 1):
    if num % 23 == 0:
        cur_index = ((cur_index - 8) % (len(numbers))) + 1
        scores[num % num_players] += (numbers.pop(cur_index) + num)
    else:
        cur_index = ((cur_index + 1) % (len(numbers))) + 1
        numbers.insert(cur_index, num)

print(max(scores.values()))


