import hashlib

part = 2

def find_hash(key, part):
    answer = 0

    while True:
        output = hashlib.md5(str(key) + str(answer)).hexdigest()

        if part == 1:
            if output[:5] == "00000":
                return answer
        else:
            if output[:6] == "000000":
                return answer

        answer += 1

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()
        print find_hash(line, part)


