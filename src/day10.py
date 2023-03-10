import functools
from collections import Counter

I = [int(x) for x in open(0).read().splitlines()]


def part1():
    xs = [0] + sorted(I) + [3 + max(I)]
    cs = Counter(b - a for (a, b) in zip(xs, xs[1:]))
    return cs[1] * cs[3]


print(part1())


def part2():
    @functools.cache
    def go(jolts, prev):
        car, cdr = jolts[0], jolts[1:]
        if car - prev > 3:
            return 0
        elif not cdr:
            return 1
        else:
            return go(cdr, car) + go(cdr, prev)

    return go(tuple(sorted(I)), 0)


print(part2())
