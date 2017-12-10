with open('input_file.txt') as inputfile:
    highest = 0
    values = {}
    input_rows = [line.strip() for line in inputfile]
    for row in input_rows:
        row = row.split("if")
        left = row[0].split()
        right = row[1]

        reg = left[0]
        inc = left[1]
        amount = int(left[2])

        right_split = right.split()
        var = right_split[0]
        if var not in values:
            values[var]= 0
        new_right_string = "values['"+var+"']"+''.join(right_split[1:])

        if reg not in values:
            values[reg] = 0

        if eval(new_right_string):
            if inc == "inc":
                
                am = values[reg] + amount
            else:
                am = values[reg] - amount

            if am > highest:
                highest = am
            values[reg] = am

    import operator
    print max(values.iteritems(), key=operator.itemgetter(1))[0]
    # TODO I did some wonky shit here by hand to find the wrong one.
    #      need to come back and make this better
    import pdb; pdb.set_trace()  # noqa
