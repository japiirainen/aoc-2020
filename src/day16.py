from typing import Tuple, List
from collections import namedtuple
import numpy as np
import math

Ticket = List[int]
Rule = List[Tuple[int, int]]
Env = namedtuple("Env", ["rules", "my", "nearby"])


def parse_input(I):
    rules, my, nearby = I.split("\n\n")
    rules = {
        name: [tuple(map(int, x.split("-"))) for x in ranges.split(" or ")]
        for name, ranges in [x.split(": ") for x in rules.splitlines()]
    }
    parse_ticket = lambda ts: [int(t) for t in ts.split(",")]
    my = parse_ticket(my.splitlines()[-1])
    nearby = list(map(parse_ticket, nearby.splitlines()[1:]))
    return Env(rules=rules, my=my, nearby=nearby)


env = parse_input(open(0).read())


is_valid = lambda lo, hi, v: lo <= v <= hi


def find_invalid(t: Ticket, rules: List[Rule]):
    for val in t:
        is_invalid = lambda rs: all(not is_valid(*r, val) for r in rs)
        if len([val for rule in rules.values() if is_invalid(rule)]) == len(t):
            return val


def invalid_tickets(env: Env):
    return [
        invalid
        for invalid in [find_invalid(t, env.rules) for t in env.nearby]
        if invalid != None
    ]


# part 1
print(sum(invalid_tickets(env)))


def valid_rules(vs: List[int], rules: List[Rule]):
    rule_applies = lambda rule, v: any(is_valid(*r, v) for r in rule)
    return [
        name for name, rule in rules.items() if all(rule_applies(rule, v) for v in vs)
    ]


def find_valid_fields(env: Env, valids: List[Ticket]):
    valids = np.array(valids).T.tolist()
    valids = enumerate([valid_rules(col, env.rules) for col in valids])
    valids = sorted(valids, key=lambda s: len(s[1]))
    for i in range(1, len(valids)):
        for j in range(i, len(valids)):
            valids[j][1].remove(valids[i - 1][1][0])
    return [env.my[i] for (i, field) in valids if field[0].startswith("departure")]


valids = [t for t in env.nearby if find_invalid(t, env.rules) == None]

# part 2
print(math.prod(find_valid_fields(env, valids)))
