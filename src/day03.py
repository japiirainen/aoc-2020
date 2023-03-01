I = open(0).read().splitlines()


def trees_in_slope(pic, dx, dy, tree="#"):
    return sum(
        1 for y, line in enumerate(pic[::dy]) if line[(y * dx) % len(line)] == tree
    )


print(trees_in_slope(I, 3, 1))

print(
    trees_in_slope(I, 1, 1)
    * trees_in_slope(I, 3, 1)
    * trees_in_slope(I, 5, 1)
    * trees_in_slope(I, 7, 1)
    * trees_in_slope(I, 1, 2)
)
