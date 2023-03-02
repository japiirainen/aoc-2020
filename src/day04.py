import re

I = open(0).read().split("\n\n")

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

passports = [(dict(re.findall(r"([a-z]+):([^\s]+)", p))) for p in I]

p1 = sum(1 for p in passports if required_fields.issubset(set(p.keys())))

print(p1)

validations = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: (v.endswith("cm") and 150 <= int(v[:-2]) <= 193)
    or (v.endswith("in") and 59 <= (int(v[:-2])) <= 76),
    "hcl": lambda v: re.match("#[0-9a-f]{6}$", v),
    "ecl": lambda v: re.match("(amb|blu|brn|gry|grn|hzl|oth)$", v),
    "pid": lambda v: re.match("[0-9]{9}$", v),
}

p2 = sum(
    1
    for p in passports
    if all(field in p and validations[field](p[field]) for field in required_fields)
)

print(p1)
