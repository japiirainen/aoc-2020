from typing import Tuple, List
from dataclasses import dataclass

Ticket = List[int]
Rule = List[Tuple[int, int]]


@dataclass
class Env:
    rules: dict[str, Rule]
    my: Ticket
    nearby: List[Ticket]


def parse_input(I):
    rules, my, nearby = I.split("\n\n")
    rules = {
        name: [tuple(map(int, x.split("-"))) for x in ranges.split(" or ")]
        for name, ranges in [x.split(": ") for x in rules.splitlines()]
    }
    parse_ticket = lambda ts: [int(t) for t in ts.split(",")]
    my = parse_ticket(my.splitlines()[-1])
    nearby = map(parse_ticket, nearby.splitlines()[1:])
    return Env(rules=rules, my=my, nearby=nearby)


env = parse_input(open(0).read())


def find_invalid(t: Ticket, rules: List[Rule]):
    for val in t:
        is_invalid = lambda rs: all(
            (lambda lo, hi: val < lo or val > hi)(*r) for r in rs
        )
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
