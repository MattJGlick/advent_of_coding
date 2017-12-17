with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split() for line in inputfile]

reins = [map(int, [row[3], row[6], row[13]]) for row in input_rows]
cur_time = 2503

def get_dist(rein, cur_time):
    speed, time, wait = rein
    # full 
    times = cur_time / (time + wait)
    total_dist = times * time * speed

    # partial
    left = cur_time % (time + wait)
    left_time = min(left, time)
    total_dist += left_time * speed
    return total_dist

print max([get_dist(rein, cur_time) for rein in reins])

total_points = [0 for _ in input_rows]

for time in range(1, cur_time + 1):
    dists = [get_dist(rein, time) for rein in reins]

    max_dist = max(dists)

    for index, dist in enumerate(dists):
        if dist == max_dist:
            total_points[index] += 1

print max(total_points)
