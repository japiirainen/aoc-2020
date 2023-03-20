from collections import Counter
from itertools import product


def parse_cells(input, d=3, active="#"):
    return {
        (x, y, *(0,) * (d - 2))
        for y, row in enumerate(input)
        for x, cell in enumerate(row)
        if cell == active
    }


pic = open(0).read().splitlines()


def neighbors(cell):
    return {
        tuple(x + dx for x, dx in zip(cell, d))
        for d in product((-1, 0, 1), repeat=len(cell))
        if any(d)
    }


def next_gen(cells):
    neighbor_counts = lambda cells: Counter(
        n for cell in cells for n in neighbors(cell)
    )
    return {
        cell
        for cell, count in neighbor_counts(cells).items()
        if count == 3 or (count == 2 and cell in cells)
    }


def simulate(cells, n=6):
    for i in range(n):
        cells = next_gen(cells)
    return len(cells)


# part 1
print(simulate(parse_cells(pic)))

# part 2
print(simulate(parse_cells(pic, d=4)))
