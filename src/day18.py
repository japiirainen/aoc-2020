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


# part 1
print(sum(eval_1(tokens) for tokens in I))


def eval_2(expr):
    if isinstance(expr, int):
        return expr
    elif "*" in expr:
        # force multiplication to be evaluated last
        i = expr.index("*")
        return eval_2(expr[:i]) * eval_2(expr[i + 1 :])
    else:
        return sum(eval_2(x) for x in expr if x not in ops)


# part 2
print(sum(eval_2(tokens) for tokens in I))
