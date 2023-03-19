I = [int(x) for x in open(0).read().split(",")]


def solve(init, n):
    last = init[-1]
    seen = {val: turn_played for turn_played, val in enumerate(init[:-1], 1)}
    for turn in range(len(init), n):
        new = 0 if last not in seen else turn - seen[last]
        seen[last] = turn
        last = new
    return last


print(solve(I, 2020))
print(solve(I, 30000000))
