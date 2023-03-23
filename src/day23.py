import numpy as np


def move(after, current):
    c1 = after[current]
    c2 = after[c1]
    c3 = after[c2]
    dest = current
    while (dest := dest - 1) % len(after) in (c1, c2, c3):
        pass
    after[current] = after[c3]
    after[c3] = after[dest]
    after[dest] = c1
    return after[current]


def play(init, move_count):
    after = np.zeros_like(init)
    after[init] = np.roll(init, -1)
    current = init[0]
    for _ in range(move_count):
        current = move(after, current)
    return after


def labels(after, count, start=0):
    if count:
        yield after[start] + 1
        yield from labels(after, count - 1, after[start])


I = np.array([int(r) - 1 for r in open(0).read().strip()])

# part 1
print("".join(map(str, labels(play(I, 100), len(I) - 1))))

I = np.r_[I, np.mgrid[len(I) : 10**6]]

# part 2
print(np.prod(list(labels(play(I, 10**7), 2)), dtype=np.int64))
