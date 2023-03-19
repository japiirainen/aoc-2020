import re
from itertools import product


def parseline(line: str):
    if line.startswith("mask"):
        return ("mask", line.split()[-1])
    return tuple([int(x) for x in re.findall(r"[0-9]+", line)])


I = [parseline(line) for line in open(0).read().splitlines()]


def bin36(i: int) -> str:
    return f"{i:036b}"


def exec_v1(instrs):
    mask = bin36(0)
    mem = {}
    for op, arg in instrs:
        if op == "mask":
            mask = arg
        else:
            addr, val = op, bin36(arg)
            val = "".join([m if m in "10" else v for m, v in zip(mask, val)])
            mem[addr] = int(val, base=2)
    return mem


def exec_v2(instrs):
    mask = bin36(0)
    mem = {}
    for addr, val in instrs:
        if addr == "mask":
            mask = val
        else:
            addr = "".join(
                a if m == "0" else "1" if m == "1" else "{}"
                for m, a in zip(mask, bin36(addr))
            )
            for bits in product("01", repeat=addr.count("{")):
                mem[int(addr.format(*bits), base=2)] = val
    return mem


def solve(mem):
    return sum(mem.values())


print(solve(exec_v1(I)))
print(solve(exec_v2(I)))
