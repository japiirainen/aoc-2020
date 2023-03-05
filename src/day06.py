I = open(0).read().split('\n\n')

# part 1
print(
    sum(len(x) for x in [set(y.replace('\n', '')) for y in I])
)

# part 2
print(sum(len(set.intersection(*map(set, g.splitlines()))) for g in I))
