from itertools import combinations
from collections import deque

I = [int(x) for x in open(0).read().splitlines()]

preamble_size = 25
preamble, rest = I[:preamble_size], I[preamble_size:]


def invalids_():
    for i, x in enumerate(rest):
        y = I[: preamble_size + i][-preamble_size:]
        cs = map(lambda x: x[0] + x[1], combinations(y, 2))
        if len([() for c in cs if c == x]) == 0:
            yield x


invalids = invalids_()

first_invalid = next(invalids)

# part 1
print(first_invalid)


def find_cont_seq(xs, target):
    xs = xs[::-1]
    seq = deque()
    total = 0

    while total != target:
        if total < target:
            x = xs.pop()
            seq.append(x)
            total += x
        if total > target:
            x = seq.popleft()
            total -= x

    return seq


def part2(xs, target):
    cont_seq = find_cont_seq(xs[:], target)
    return min(cont_seq) + max(cont_seq)


print(part2(I, first_invalid))
