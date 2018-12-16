import collections

with open('input_file.txt') as inputfile:
    rows = [line.strip() for line in inputfile]


def print_grid(rows, fighters):
    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if (x, y) in spaces:
                print('.', end='')
            elif (x, y) in [(f.x, f.y) for f in fighters if f.is_goblin and f.is_alive]:
                print('G', end='')
            elif (x, y) in [(f.x, f.y) for f in fighters if not f.is_goblin and f.is_alive]:
                print('E', end='')
            else:
                print('#', end='')
        print('')


def neighbors(x, y):
    return [
        (x, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x, y + 1),
    ]


def reading_order(pos):
    return pos[1], pos[0]


def bfs(start, goal, spaces):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path[1], len(path), goal
        for x2, y2 in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
            if (x2, y2) in spaces and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


class Fighter(object):
    def __init__(self, f_id, x, y, is_goblin, dmg):
        self.f_id = f_id
        self.x = x
        self.y = y
        self.hp = 200
        self.dmg = dmg
        self.is_goblin = is_goblin
        self.is_alive = True

    def pos(self):
        return (self.x, self.y)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp <= 0:
            self.is_alive = False
            spaces.append((self.x, self.y))

    def attack(self, enemies_nearby):
        enemies_nearby.sort(key=lambda e: (e.hp, reading_order(e.pos())))
        victim = enemies_nearby[0]
        victim.take_damage(self.dmg)

    def move(self, new_pos, spaces):
        new_x, new_y = new_pos

        spaces.append((self.x, self.y))
        spaces.remove((new_x, new_y))
        self.x = new_x
        self.y = new_y


elves_dmg = 3
while True:
    spaces = []
    fighters = []
    fighter_id = 0
    for y, row in enumerate(rows):
        for x, item in enumerate(row):
            if item == 'G':
                fighters.append(Fighter(fighter_id, x, y, True, 3))
                fighter_id += 1
            elif item == 'E':
                fighters.append(Fighter(fighter_id, x, y, False, elves_dmg))
                fighter_id += 1
            elif item == '.':
                spaces.append((x, y))

    rounds = 0
    done = False
    while not done:
        fighters.sort(key=lambda f: reading_order(*f.pos()))

        for fighter in fighters:
            if not fighter.is_alive:
                continue

            enemies = [f for f in fighters if f.is_goblin is not fighter.is_goblin and f.is_alive]

            if not enemies:
                done = True
                break

            enemies_nearby = [e for e in enemies if e.pos() in neighbors(*fighter.pos())]

            # walk
            if not enemies_nearby:
                enemies_neighbors = [n for e in enemies for n in neighbors(*e.pos())]
                enemies_neighbor_spaces = list(set(enemies_neighbors) & set(spaces))

                bfs_results = [bfs(fighter.pos(), e_n_s, spaces) for e_n_s in enemies_neighbor_spaces]
                bfs_results = list(set([b for b in bfs_results if b]))
                bfs_results.sort(key=lambda f: (f[1], reading_order(f[2]), reading_order(f[0])))

                if bfs_results:
                    new_pos = bfs_results[0][0]

                    fighter.move(new_pos, spaces)

            enemies_nearby = [f for f in enemies if f.pos() in neighbors(*fighter.pos())]

            if enemies_nearby:
                fighter.attack(enemies_nearby)

        rounds += 1

        # print_grid(rows, fighters)

    rounds -= 1
    rem_health = sum([f.hp for f in fighters if f.is_alive])

    if elves_dmg == 3:
        print('Part 1:', rounds * rem_health)
    if not any([f for f in fighters if not f.is_goblin and not f.is_alive]):
        print('Part 2:', rounds * rem_health)
        break
    elves_dmg += 1
