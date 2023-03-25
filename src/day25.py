I = 19241437, 17346587


def transform(subj):
    val = 1
    while True:
        val = (val * subj) % 20201227
        yield val


def solve(keys):
    loopsize = next(iter(i for i, val in enumerate(transform(7)) if val == keys[0]))
    return next(iter(val for i, val in enumerate(transform(keys[1])) if i == loopsize))


print(solve(I))
