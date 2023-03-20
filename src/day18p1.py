import ply.lex as lex
import ply.yacc as yacc

tokens = (
    "NUMBER",
    "PLUS",
    "TIMES",
    "LPAREN",
    "RPAREN",
)

t_PLUS = r"\+"
t_TIMES = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ignore = " \t\n"


def t_NUMBER(t):
    r"\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Parsing rules

precedence = (("left", "PLUS", "TIMES"),)


def p_statement_expr(t):
    "statement : expression"
    t[0] = t[1]


def p_expression_binop(t):
    """expression : expression PLUS expression
    | expression TIMES expression
    """
    if t[2] == "+":
        t[0] = t[1] + t[3]
    elif t[2] == "*":
        t[0] = t[1] * t[3]


def p_expression_group(t):
    "expression : LPAREN expression RPAREN"
    t[0] = t[2]


def p_expression_number(t):
    "expression : NUMBER"
    t[0] = t[1]


print(sum(yacc.yacc().parse(l) for l in open(0).read().splitlines()))
