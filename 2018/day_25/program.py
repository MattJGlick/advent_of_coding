from itertools import combinations, permutations
import numpy as np
import re

from collections import defaultdict, Counter
import networkx as nx

with open('input_file.txt') as inputfile:
    points = [tuple(map(int, line.strip().split(','))) for line in inputfile]


def man(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + \
           abs(point_1[1] - point_2[1]) + \
           abs(point_1[2] - point_2[2]) + \
           abs(point_1[3] - point_2[3])


connected = nx.Graph()
for point_1 in points:
    for point_2 in points:
        if man(point_1, point_2) <= 3:
            connected.add_edge(point_1, point_2)

print(len(list(nx.connected_component_subgraphs(connected))))
