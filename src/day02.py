from dataclasses import dataclass

I = open(0).read().splitlines()


@dataclass
class Passport:
    lo: int
    hi: int
    char: str
    chars: str


def parse_passports(lines):
    def parse_passport(line):
        a, chars = line.split(": ")
        r, c = a.split(" ")
        lo, hi = map(int, r.split("-"))
        return Passport(lo, hi, c, chars)

    return [parse_passport(line) for line in lines]


def part1(ps):
    return sum(1 for p in ps if p.lo <= p.chars.count(p.char) <= p.hi)


ps = parse_passports(I)

print(part1(ps))


def part2(ps):
    return sum(
        1 for p in ps if (p.chars[p.lo - 1] == p.char) ^ (p.chars[p.hi - 1] == p.char)
    )


print(part2(ps))
