with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split() for line in inputfile]

index = 0
# values = {'a': 1}
values = {}
fin_count = 0
while index < len(input_rows):
    par = input_rows[index]
    cmd = par[0]
    fir = par[1]
    if len(par) > 2:
        sec = par[2]
        if sec.isalpha():
            sec = values[sec]
        else:
            sec = int(sec)

    if fir.isalpha():
        if fir not in values:
            values[fir] = 0

    if cmd == "set":
        values[fir] = sec
    elif cmd == "sub":
        values[fir] -= sec
    elif cmd == "mul":
        values[fir] *= sec
        fin_count += 1
    elif cmd == "jnz":
        if fir.isalpha():
            if values[fir] != 0:
                index += sec - 1
        else:
            if int(fir) != 0:
                index += sec - 1
    index += 1
    
print fin_count


def part_2():
    h = 0
    a = 1
    b = 57
    c = b
    b *= 100
    b -= -100000
    c = b
    c -= -17000 

    while True:
        f = 1
        d = 2
        e = 2

        while True:
            # REFACTORED THIS SIGNIFICANTLY
            # basically G and E were just temp vars we were throwing around 
            # was able to remove them entirely
            if b % d == 0:
                f = 0

            d -= -1

            if d != b:
                continue

            if f == 0:
                h += 1

            if b == c:
                return h

            b -= -17

            break

print part_2()
