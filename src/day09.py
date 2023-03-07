from itertools import combinations

I = [int(x) for x in open(0).read().splitlines()]

preamble_size = 25
preamble, rest = I[:preamble_size], I[preamble_size:]

def part1():
    for i, x in enumerate(rest):
        y = I[:preamble_size + i][-preamble_size:]
        cs = map(lambda x: x[0] + x[1], combinations(y, 2))
        if len([() for c in cs if c == x]) == 0:
            return x

print(part1())