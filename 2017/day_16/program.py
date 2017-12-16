import string
with open('input_file.txt') as inputfile:
    moves = [line.strip().split(",") for line in inputfile][0]
    letters = list(string.ascii_lowercase[:16])

    found = []

    while True:
        if tuple(letters) in found:
            print ''.join(found[1000000000 % len(found)])
            break;
        else:
            found.append(tuple(letters))
        for move in moves:
            if move[0] == "s":
                dist = int(move[1:]) * -1
                letters = letters[dist:] + letters[:dist]
            elif move[0] == "x":
                swaps = map(int, move[1:].split("/"))
                
                temp = letters[swaps[0]]
                letters[swaps[0]] = letters[swaps[1]]
                letters[swaps[1]] = temp
            elif move[0] == "p":
                swaps = move[1:].split("/")
                l_index = letters.index(swaps[0])
                r_index = letters.index(swaps[1])

                letters[l_index] = swaps[1]
                letters[r_index] = swaps[0]
