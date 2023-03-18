from typing import Tuple, List

I = [(lambda l: (l[0], int(l[1:])))(line) for line in open(0).read().splitlines()]

dirs = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def turn(d: int, x: int, y: int) -> Tuple[int, int]:
    assert d % 90 == 0, f"Invalid degree: {d}"
    if d % 360 == 0:
        return (x, y)
    return turn(d - 90, y, -x)


def move(x, y, dx, dy, n):
    return (x + dx * n, y + dy * n)


def navigate(instructions: List[Tuple[str, int]], loc=(0, 0), dir=dirs["E"]):
    if len(instructions) == 0:
        return loc
    (op, arg), *rest = instructions
    if op == "L":
        return navigate(rest, loc, turn(-arg, *dir))
    elif op == "R":
        return navigate(rest, loc, turn(arg, *dir))
    elif op == "F":
        return navigate(rest, move(*loc, *dir, arg), dir)
    else:
        return navigate(rest, move(*loc, *dirs[op], arg), dir)


def manhattan_dist(p):
    return sum(map(abs, p))


# part 1
print(manhattan_dist(navigate(I)))


def navigate2(instructions: List[Tuple[str, int]], wp=(10, 1), loc=(0, 0)):
    if len(instructions) == 0:
        return loc
    (op, arg), *rest = instructions
    if op == "L":
        return navigate2(rest, turn(-arg, *wp), loc)
    elif op == "R":
        return navigate2(rest, turn(arg, *wp), loc)
    elif op == "F":
        return navigate2(rest, wp, move(*loc, *wp, arg))
    else:
        return navigate2(rest, move(*wp, *dirs[op], arg), loc)


# part 2
print(manhattan_dist(navigate2(I)))
