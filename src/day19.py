import re


def atoms(text: str):
    for atom in text.split():
        for typ in (int, str):
            try:
                yield typ(atom)
                break
            except ValueError:
                pass


rules, messages = open(0).read().split("\n\n")


def parse_rule(rule):
    key, *rule = atoms(rule.replace(":", " ").replace('"', " "))
    if "|" in rule:
        idx = rule.index("|")
        rule = [tuple((rule[:idx], rule[idx + 1 :]))]
    return key, rule


def parse_rules(rules):
    return dict(map(parse_rule, rules.splitlines()))


rules, messages = parse_rules(rules), messages.splitlines()


def pattern_match(pat, rules, msg):
    if not pat:
        return msg
    elif pat and not msg:
        return None
    elif pat[0] == msg[0]:
        return pattern_match(pat[1:], rules, msg[1:])
    elif isinstance(pat[0], int):
        new_pat = rules[pat[0]] + pat[1:]
        return pattern_match(new_pat, rules, msg)
    elif isinstance(pat[0], tuple):
        for choice in pat[0]:
            m = pattern_match(choice + pat[1:], rules, msg)
            if m != None:
                return m
    return None


def rule_matches(rule, rules, messages) -> list[str]:
    matches = [pattern_match(rules[rule], rules, message) for message in messages]
    return filter(lambda match: match == "", matches)


# part 1
print(len(list(rule_matches(0, rules, messages))))

optional = lambda n: tuple(([], [n]))
rules = {**rules, 8: [42, optional(8)], 11: [42, optional(11), 31]}

# part 2
print(len(list(rule_matches(0, rules, messages))))
