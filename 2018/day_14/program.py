code = 939601
code_list = [int(num) for num in str(code)]
recipes = [3, 7]

elf_1_index = 0
elf_2_index = 1
while True:
    if len(recipes) == (code + 10):
        print(''.join(map(str, recipes[-10:])))
    if recipes[-6:] == code_list:
        print(len(recipes) - 6)
        break
    if recipes[-7:-1] == code_list:
        print(len(recipes) - 7)
        break

    elf_1_score = recipes[elf_1_index]
    elf_2_score = recipes[elf_2_index]

    recipes.extend(map(int, str(elf_1_score + elf_2_score)))

    elf_1_index = (elf_1_index + elf_1_score + 1) % len(recipes)
    elf_2_index = (elf_2_index + elf_2_score + 1) % len(recipes)
