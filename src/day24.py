from collections import Counter
from itertools import chain

import re
import operator

I = tuple(open(0).read().splitlines())

hexdirs = {"e": (1, 0), "w": (-1, 0), "ne": (1, -1), "sw": (-1, 1), "se": (0, 1), "nw": (0, -1)}

parse_hex = lambda line: re.findall("e|w|ne|sw|se|nw", line)


def follow_hex(directions):
    x, y = 0, 0
    for d in parse_hex(directions):
        dx, dy = hexdirs[d]
        x += dx
        y += dy
    return x, y


counts = Counter(map(follow_hex, I))
blacks = {tile for tile in counts if counts[tile] % 2}

# part 1
print(len(blacks))


def next_gen(cells):
    neighbors = lambda cell: [tuple(map(operator.add, cell, delta)) for delta in hexdirs.values()]
    counts = Counter(chain.from_iterable(map(neighbors, cells)))
    return ({c for c in cells if counts[c] in (1, 2)} |
            {c for c in counts if c not in cells and counts[c] == 2})


def life(cells, n):
    for g in range(n):
        cells = next_gen(cells)
    return cells


# part 2
print(len(life(blacks, 100)))
