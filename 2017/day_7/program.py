from collections import defaultdict
with open('input_file.txt') as inputfile:
    input_rows = [line.strip().split() for line in inputfile]
    all_parents = set()
    all_children = set()

    weights = {}
    tree = {}

    for row in input_rows:
        parent = row[0]
        weight = int(row[1][1:-1])
        children = [item.strip(',') for item in row[3:]]

        all_parents.add(parent)
        all_children |= set(children)

        weights[parent] = weight
        tree[parent] = children

    root =  list(all_parents - all_children)[0]
    print root

    diff = 0

    def get_weight(parent):
        return sum([get_weight(child) for child in tree[parent]]) + weights[parent]

    def find_problem_child(parent):
        problem_child = None
        global diff

        child_weights = defaultdict(list)
        for child in tree[parent]:
            child_weights[get_weight(child)].append(child)

        if len(child_weights) == 1:
            return parent
        for weight in child_weights:
            if len(child_weights[weight]) == 1:
                diff = child_weights.keys()[0] - child_weights.keys()[1]
                return find_problem_child(child_weights[weight][0])

    problem_child = find_problem_child(root)
    print weights[problem_child] - diff
