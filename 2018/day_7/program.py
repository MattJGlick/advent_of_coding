from collections import defaultdict
import re

step_regex = re.compile('Step ([A-Z]) .* step ([A-Z]) .*')

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

steps = defaultdict(set)

o_starts = set()
o_stops = set()
all_l = set()

for row in rows:
    start, stop = step_regex.match(row).groups()
    steps[stop].add(start)

    o_starts.add(start)
    o_stops.add(stop)
    all_l = all_l.union(set([start, stop]))

avail = o_starts - o_stops

order = []

while set(order) != all_l:
    for stop, starts in steps.items():
        if starts.issubset(set(order)) and stop not in order:
            avail.add(stop)

    current = sorted(list(avail))[0]
    order.append(current)
    avail.remove(current)
print(''.join(order))

avail = o_starts - o_stops

order = []

starting_secs = 60
avail_workers = 5
cur_time = 1
workers = {}
workers_time = {}
working = set()

for worker in range(avail_workers):
    workers[worker] = None
    workers_time[worker] = 0

while set(order) != all_l:
    if avail_workers > 0:
        for stop, starts in steps.items():
            if starts.issubset(set(order)) and stop not in order and stop not in working:
                avail.add(stop)

    for avail_item in avail:
        if avail_workers > 0:
            assigned = False
            for worker, item in workers.items():
                if not item and not assigned:
                    assigned = True
                    workers[worker] = avail_item
                    avail_workers -= 1
                    workers_time[worker] = starting_secs + ord(avail_item) - 64

    for worker in workers_time:
        workers_time[worker] -= 1
        if workers[worker] in avail:
            avail.remove(workers[worker])
        working.add(workers[worker])

        if workers_time[worker] == 0 and workers[worker]:
            avail_workers += 1
            current = workers[worker]
            workers[worker] = None

            order.append(current)
            working.remove(current)
    cur_time += 1
print(cur_time - 1)
