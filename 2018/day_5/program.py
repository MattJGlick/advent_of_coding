with open('input_file.txt') as inputfile:
    word = inputfile.read().strip()

bad_strings = []
for i in range(65, 91):
    cap = chr(i)
    lower = chr(i + 32)

    bad_strings.append(cap + lower)
    bad_strings.append(lower + cap)

can_react = True
while can_react:
    before_len = len(word)
    for bad_string in bad_strings:
        word = word.replace(bad_string, '')

    if before_len == len(word):
        can_react = False

print(len(word))

min_len = len(word) + 1
min_letter = None
new_word = word
for i in range(65, 91):
    cap = chr(i)
    lower = chr(i + 32)

    new_word = word
    new_word = new_word.replace(cap, '')
    new_word = new_word.replace(lower, '')

    can_react = True
    while can_react:
        before_len = len(new_word)
        for bad_string in bad_strings:
            new_word = new_word.replace(bad_string, '')

        if before_len == len(new_word):
            can_react = False

    if len(new_word) < min_len:
        min_len = len(new_word)
        min_letter = cap

print(min_letter)
