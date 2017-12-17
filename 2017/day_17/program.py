values = [0]
spin = 303
cur = 0

for index in range(1, 2018):
    cur = (cur + spin) % (index) + 1
    values.insert(cur, index)

print values[values.index(2017) + 1]

cur = 0
first = 0
for index in range(1, 50000001):
    cur = (cur + spin) % (index) + 1
    if cur == 1:
        first = index

print first
