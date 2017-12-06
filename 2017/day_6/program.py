import copy

def get_bank_loop(bank):
    seen = []
    rep_count = 0

    while bank not in seen:
        seen.append(copy.deepcopy(bank))
        rep_count += 1

        highest_index = bank.index(max(bank))
        highest_value = bank[highest_index]
        bank[highest_index] = 0

        for _ in range(0, highest_value):
            highest_index = (highest_index + 1) % len(bank)
            bank[highest_index] += 1

    return rep_count, len(seen) - seen.index(bank)


assert get_bank_loop([0, 2, 7, 0]) == (5, 4)
assert get_bank_loop([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]) == (14029, 2765)

with open('input_file.txt') as inputfile:
    get_bank_loop(map(int, [line.split() for line in inputfile][0]))
