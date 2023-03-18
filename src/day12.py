import re
from typing import Tuple, List


def parse_instruction(line: str) -> Tuple[str, int]:
    m = re.match(r"([NSEWLRF])([0-9]+)", line)
    return (m.group(1), int(m.group(2)))


I = [parse_instruction(line) for line in open(0).read().splitlines()]

dirs = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def turn(d: int, x: int, y: int) -> Tuple[int, int]:
    assert d % 90 == 0, f"Invalid degree: {d}"
    if d % 360 == 0:
        return (x, y)
    return turn(d - 90, y, -x)


def move(x, y, dx, dy, n):
    return (x + dx * n, y + dy * n)


def navigate(instructions: List[Tuple[str, int]], loc=(0, 0), dir=dirs["E"]):
    for op, arg in instructions:
        if op == "L":
            dir = turn(-arg, *dir)
        elif op == "R":
            dir = turn(arg, *dir)
        elif op == "F":
            loc = move(*loc, *dir, arg)
        else:
            loc = move(*loc, *dirs[op], arg)
    return loc


def manhattan_dist(p):
    return sum(map(abs, p))


# part 1
print(manhattan_dist(navigate(I)))


def navigate2(instructions: List[Tuple[str, int]], wp=(10, 1), loc=(0, 0)):
    for op, arg in instructions:
        if op == "L":
            wp = turn(-arg, *wp)
        elif op == "R":
            wp = turn(arg, *wp)
        elif op == "F":
            loc = move(*loc, *wp, arg)
        else:
            wp = move(*wp, *dirs[op], arg)
    return loc


# part 2
print(manhattan_dist(navigate2(I)))
