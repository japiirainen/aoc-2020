from collections import namedtuple

Food = namedtuple("Food", "ingredients allergens")


def parse_food(I):
    i, a = I.split(" (contains ")
    a = a[:-1].split(", ")
    return Food(*map(set, (i.split(), a)))


I = [parse_food(line) for line in open(0).read().splitlines()]


def eliminate_others(possible, i):
    for j in possible:
        if j != i:
            possible[j] -= possible[i]


def allergen_map(foods):
    ingredients = set.union(*(f.ingredients for f in foods))
    allergens = set.union(*(f.allergens for f in foods))
    possible = {a: ingredients.copy() for a in allergens}
    while any(len(possible[a]) > 1 for a in possible):
        for f in foods:
            for a in f.allergens:
                possible[a] &= f.ingredients
                if len(possible[a]) == 1:
                    eliminate_others(possible, a)
    return possible


am = allergen_map(I)
allergens = set([x for x, in am.values()])

# part 1
print(sum([len(food.ingredients - allergens) for food in I]))

# part 2
print(",".join((x for x, in (am[key] for key in sorted(am)))))
