I = open(0).read().splitlines()


def exec_instruction(instr, ip, acc):
    op, arg = instr.split(' ')
    if op == 'nop':
        ip += 1
    elif op == 'acc':
        acc += int(arg)
        ip += 1
    elif op == 'jmp':
        ip += int(arg)
    return ip, acc


def exec(instructions):
    ip, acc, vis_ips, halted = 0, 0, set(), False
    while not halted:
        if ip in vis_ips:
            break  # looped
        if ip == len(instructions):
            halted = True
            break
        vis_ips.add(ip)
        next_ip, next_acc = exec_instruction(instructions[ip], ip, acc)
        ip, acc = next_ip, next_acc
    return halted, acc


def part1(instructions):
    _, acc = exec(instructions)
    return acc


print(part1(I))


def patches(instructions):
    for i, instr in enumerate(instructions):
        op, arg = instr.split(' ')
        if op == 'nop' or op == 'jmp':
            op = ('jmp' if op == 'nop' else 'nop')
            updated_op = f"{op} {arg}"
            cp = instructions[:]
            cp[i] = updated_op
            yield cp


def part2(instructions):
    for patched in patches(instructions):
        halted, acc = exec(patched)
        if halted:
            return acc


print(part2(I))
