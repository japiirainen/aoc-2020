import math

I = open(0).read().splitlines()


def trans(bp): return int(bp.translate(str.maketrans("FLBR", "0011")), base=2)


ids = {trans(bp) for bp in I}

# part 1
print(max(ids))

# part 2
print(
    list(set(range(min(ids), max(ids))) - ids)[0]
)
