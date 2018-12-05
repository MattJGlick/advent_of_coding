from collections import defaultdict, Counter
from datetime import datetime
import re
with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]

times_slept = defaultdict(list)
for row in rows:
    timestamp, text = row.split('] ')
    timestamp = datetime.strptime(timestamp[1:], '%Y-%m-%d %H:%M')

    if 'Guard' in row:
        cur_guard = int(re.findall(r'\d+', text)[0])
    elif 'falls' in row:
        sleep_time = int(timestamp.minute)
    elif 'wakes' in row:
        awake_time = int(timestamp.minute)
        times_slept[cur_guard].append([sleep_time, awake_time])

max_guard = times_slept[0]
max_time = 0
for guard, ranges in times_slept.items():
    total_time = sum([time_range[1] - time_range[0] for time_range in ranges])

    if total_time > max_time:
        max_guard = guard
        max_time = total_time

max_guard_times = [item for time in times_slept[max_guard] for item in list(range(time[0], time[1]))]
max_guard_min, max_guard_count = Counter(max_guard_times).most_common()[0]
print(max_guard * max_guard_min)

max_guard = times_slept[0]
max_minute = 0
max_count = 0
for guard, ranges in times_slept.items():
    max_guard_times = [item for time in ranges for item in list(range(time[0], time[1]))]

    if max_guard_times:
        max_guard_min, max_guard_count = Counter(max_guard_times).most_common()[0]

        if max_guard_count > max_count:
            max_guard = guard
            max_count = max_guard_count
            max_minute = max_guard_min
print(max_guard * max_minute)

