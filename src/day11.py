import sys

I = [list(s) for s in open(0).read().splitlines()]

occupied, empty, floor, bad = "#L.?"
deltas = ((-1, -1), (-1, 0), (1, -1), (0, -1), (1, 0), (-1, 1), (0, 1), (1, 1))


def neighbors(l, r, c):
    return [
        l[r + d[0]][c + d[1]]
        for d in deltas
        if 0 <= r + d[0] < len(l) and 0 <= c + d[1] < len(l[0])
    ]


def see(l, r, c):
    def visible(r, c, dr, dc):
        for _ in range(1, sys.maxsize):
            r, c = r + dr, c + dc
            if not (0 <= r < len(l) and 0 <= c < len(l[0])):
                return bad
            if l[r][c] != floor:
                return l[r][c]

    return [visible(r, c, d[0], d[1]) for d in deltas]


def step_1(prev_gen):
    next_gen = [s[:] for s in prev_gen[:]]
    for i, row in enumerate(prev_gen):
        for j, cur in enumerate(row):
            ns = neighbors(prev_gen, i, j)
            n_occupied = len([x for x in ns if x == occupied])
            if cur == empty and n_occupied == 0:
                next_gen[i][j] = occupied
            elif cur == occupied and n_occupied >= 4:
                next_gen[i][j] = empty
    return next_gen


def step_2(prev_gen):
    next_gen = [s[:] for s in prev_gen[:]]
    for i, row in enumerate(prev_gen):
        for j, cur in enumerate(row):
            ss = see(prev_gen, i, j)
            n_occupied = len([x for x in ss if x == occupied])
            if cur == empty and n_occupied == 0:
                next_gen[i][j] = occupied
            elif cur == occupied and n_occupied >= 5:
                next_gen[i][j] = empty
    return next_gen


def find_fix(gen, step_f):
    next_gen = step_f(gen)
    if gen == next_gen:
        return next_gen
    return find_fix(next_gen, step_f)


def count_occupied(l):
    c = 0
    for r in l:
        for item in r:
            if item == occupied:
                c += 1
    return c


def solve(l, step_f):
    fixed = find_fix(l, step_f)
    return count_occupied(fixed)


# part 1
print(solve(I, step_1))

# part 2
print(solve(I, step_2))
