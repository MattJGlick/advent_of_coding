from itertools import combinations as combo
from itertools import product as prod

weapons = [(8, 4, 0),
(10, 5, 0),
(25, 6, 0),
(40, 7, 0),
(74, 8, 0)]

armor = [(13, 0, 1),
(31, 0, 2),
(53, 0, 3),
(75, 0, 4),
(102, 0, 5)]

rings = [(25, 1, 0),
(50, 2, 0),
(100, 3, 0),
(20, 0, 1),
(40, 0, 2),
(80, 0, 3)]

lowest_gold = 9999999999999999999999
max_gold = 0
part_1 = False

weapons_perms = list(combo(weapons, 1))
armor_perms = list(combo(armor, 1)) + list(combo(armor, 0))
rings_perms = list(combo(rings, 2)) + list(combo(rings, 1)) + list(combo(rings, 0))
all_perms = [weapons_perms, armor_perms, rings_perms]
tool_perms = list(prod(*all_perms))

for tool_groups in tool_perms:
    cost, play_dmg, play_armor = [sum(zipped) for zipped in zip(*[tool for group in tool_groups for tool in group])]
    play_health = 100

    boss_health = 100
    boss_dmg = 8
    boss_armor = 2

    while True:
        # i attack
        boss_health -= max(play_dmg - boss_armor, 1)

        if boss_health <= 0:
            if part_1:
                lowest_gold = min(cost, lowest_gold)
            break

        # boss attack
        play_health -= max(boss_dmg - play_armor, 1)

        if play_health <= 0:
            if not part_1:
                max_gold = max(cost, max_gold)
            break

if part_1:
    print lowest_gold
else:
    print max_gold
