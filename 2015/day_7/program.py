values = {}

def find_value(value):
    try:
        return int(value)
    except ValueError:
        pass

    ops = values[value]

    if not isinstance(ops, list):
        return int(ops)

    if len(ops) == 1:
        result = find_value(ops[0])
    else:
        if ops[0] == "NOT":
            result = ~find_value(ops[1])
        elif ops[1] == "AND":
            result = find_value(ops[0]) & find_value(ops[2])
        elif ops[1] == "OR":
            result = find_value(ops[0]) | find_value(ops[2])
        elif ops[1] == "LSHIFT":
            result = find_value(ops[0]) << find_value(ops[2])
        elif ops[1] == "RSHIFT":
            result = find_value(ops[0]) >> find_value(ops[2])

    values[value] = result
    return result

with open('input_file.txt') as inputfile:
    for line in inputfile:
        line = line.rstrip()
        ops, value = line.split("->")
        values[value.strip()] = ops.split()

print find_value("a")
