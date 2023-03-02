I = set([int(x) for x in open(0).read().splitlines()])

# part 1
print(next(a * b for a in I for b in I & {2020 - a}))

# part 2
print(next(a * b * c for a in I for b in I for c in I & {2020 - a - b}))
