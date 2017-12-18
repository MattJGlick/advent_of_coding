with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split() for line in inputfile]

index = 0
values = {}
while True:
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
    if cmd == "add":
        values[fir] += sec
    if cmd == "mul":
        values[fir] *= sec
    if cmd == "mod":
        values[fir] %= sec
    if cmd == "snd":
        freq = values[fir]
    if cmd == "rcv":
        if values[fir] != 0:
            break
    if cmd == "jgz":
        if values[fir] > 0:
            index += sec - 1

    index += 1
    
print freq

#############
#
# This part 2 is absolute garbage, there is most definitely a better way of doing it, but for the 
# sake of the speed challenge I wrote this monstrosity. It helped with the rank, but now this
# comment is needed to explain the garbage that is the next 100 lines. If you've stumbled upon this
# hoping to learn how to do this problem well GO SOMEWHERE ELSE.
# 
# I'll try and come back and fix this, but I probably wont
#
##########

import Queue

freq = 0
index = 0
index_2 = 0
values = {'p': 0}
values_2 = {'p': 1}
msgs = Queue.Queue()
msgs_2 = Queue.Queue()
count = 0
while True:
    par = input_rows[index]
    cmd = par[0]
    first_cmd = cmd
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
    else:
        fir = int(fir)

    move = True
    if cmd == "set":
        values[fir] = sec
    if cmd == "add":
        values[fir] += sec
    if cmd == "mul":
        values[fir] *= sec
    if cmd == "mod":
        values[fir] %= sec
    if cmd == "snd":
        if fir in values:
            msgs_2.put(values[fir])
        else:
            msgs_2.put(fir)
    if cmd == "rcv":
        if not msgs.empty():
            values[fir] = msgs.get()
        else:
            move = False
    if cmd == "jgz":
        if fir in values:
            if values[fir] > 0:
                index += sec - 1
        else:
            if fir > 0:
                index += sec - 1


    if move:
        index += 1

    par = input_rows[index_2]
    cmd = par[0]
    sec_cmd = cmd
    fir = par[1]
    if len(par) > 2:
        sec = par[2]
        if sec.isalpha():
            sec = values_2[sec]
        else:
            sec = int(sec)

    if fir.isalpha():
        if fir not in values_2:
            values_2[fir] = 0
    else:
        fir = int(fir)

    move_2 = True
    if cmd == "set":
        values_2[fir] = sec
    if cmd == "add":
        values_2[fir] += sec
    if cmd == "mul":
        values_2[fir] *= sec
    if cmd == "mod":
        values_2[fir] %= sec
    if cmd == "snd":
        count += 1
        if fir in values_2:
            msgs.put(values_2[fir])
        else:
            msgs.put(fir)
    if cmd == "rcv":
        if not msgs_2.empty():
            values_2[fir] = msgs_2.get()
        else:
            move_2 = False
    if cmd == "jgz":
        if fir in values_2:
            if values_2[fir] > 0:
                index_2 += sec - 1
        else:
            if fir > 0:
                index_2 += sec - 1

    if move_2:
        index_2 += 1

    if first_cmd == "rcv" and sec_cmd == "rcv" and msgs.empty() and msgs_2.empty():
        break

print count



