import re
import ast


def tokenize(expr):
    return ast.literal_eval(re.sub(r"([*+])", r",'\1',", expr))


I = [tokenize(expr) for expr in open(0).read().splitlines()]

ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}


def eval_1(expr):
    if isinstance(expr, int):
        return expr
    else:
        a, op, b, *rest = expr
        x = ops[op](eval_1(a), eval_1(b))
        return x if not rest else eval_1((x, *rest))


print(sum(eval_1(tokens) for tokens in I))
