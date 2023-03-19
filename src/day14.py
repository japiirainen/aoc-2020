import re
import itertools


def parseline(line: str):
    if line.startswith("mask"):
        return ("mask", line.split()[-1])
    return tuple([int(x) for x in re.findall(r"[0-9]+", line)])


I = [parseline(line) for line in open(0).read().splitlines()]


def bin36(i: int) -> str:
    return f"{i:036b}"


def exec_v1(instrs, mask=bin36(0), mem={}):
    if len(instrs) == 0:
        return mem
    (addr, val), *instrs = instrs
    if addr == "mask":
        return exec_v1(instrs, val, mem)
    mem[addr] = int(
        "".join([m if m in "01" else v for m, v in zip(mask, bin36(val))]), base=2
    )
    return exec_v1(instrs, mask, mem)


def exec_v2(instrs, mask=bin36(0), mem={}):
    if len(instrs) == 0:
        return mem
    (addr, val), *instrs = instrs
    if addr == "mask":
        return exec_v2(instrs, val, mem)
    addr = "".join(
        a if m == "0" else "1" if m == "1" else "{}" for m, a in zip(mask, bin36(addr))
    )
    for bits in itertools.product("01", repeat=addr.count("{")):
        mem[int(addr.format(*bits), base=2)] = val
    return exec_v2(instrs, mask, mem)


def solve(mem):
    return sum(mem.values())


print(solve(exec_v1(I)))
print(solve(exec_v2(I)))
