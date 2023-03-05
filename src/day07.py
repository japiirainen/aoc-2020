from functools import lru_cache

I = open(0).read().splitlines()


def parse_inner(s: str):
    return {f"{p[1]} {p[2]}":
            (0 if p[0] == 'no' else int(p[0])) for p in [p.split(' ') for p in s.split(', ')]}


def parse_rule(rule: str):
    before, after = rule.split(' contain ')
    bag_color = ' '.join(before.split(' ')[: 2])
    return (bag_color, parse_inner(after))


rules = {k: v for (k, v) in [parse_rule(rule) for rule in I]}


def n_can_contain(target, rules) -> int:
    @lru_cache
    def contains(target: str, rule):
        contents = rules.get(rule, {})
        return (target in contents) or any(contains(target, inner) for inner in contents)
    return sum(1 for c in [contains(target, rule) for rule in rules] if c)


# part 1
print(n_can_contain('shiny gold', rules))


def count_contains(target, rules):
    return sum([n + n * count_contains(inner, rules)
                for (inner, n) in rules.get(target, {}).items()])


# part 2
print(count_contains('shiny gold', rules))
