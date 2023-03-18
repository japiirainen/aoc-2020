import re


def parseline(line: str):
    if line.startswith("mask"):
        return ("mask", line.split(" = ")[1])
    return [int(x) for x in re.findall(r"[0-9]+", line)]


I = [parseline(line) for line in open(0).read().splitlines()]

print(I)
