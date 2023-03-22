from collections import deque
import numpy as np


def parse(input):
    out = []
    for player in input:
        _, ns = player.split(":\n")
        out.append([int(x) for x in ns.splitlines()])
    return tuple(map(tuple, out))


I = parse(open(0).read().split("\n\n"))


def play(d1, d2):
    d1, d2 = d1.copy(), d2.copy()
    while d1 and d2:
        top1 = d1.popleft()
        top2 = d2.popleft()
        W = 1 if top1 > top2 else 2
        T = d1 if W == 1 else d2
        E = [top1, top2] if W == 1 else [top2, top1]
        T.extend(E)
    return d1 or d2


def score(winning_deck):
    return np.dot(winning_deck, range(len(winning_deck), 0, -1))


# part 1
print(score([*play(*(map(deque, I)))]))


def seen(d1, d2, P):
    H = tuple(map(tuple, (d1, d2)))
    if H in P:
        return True
    P.add(H)
    return False


def play_rec(deals):
    deals = tuple(map(deque, deals))
    P = set()
    while all(deals):
        if seen(*deals, P):
            return (deals[0], ())
        topcards = tuple(map(deque.popleft, deals))
        if all(len(deals[p]) >= topcards[p] for p in (0, 1)):
            deals2 = [tuple(deals[p])[: topcards[p]] for p in (0, 1)]
            result = play_rec(deals2)
            winner = 0 if result[0] else 1
        else:
            winner = 0 if topcards[0] > topcards[1] else 1
        deals[winner].extend([topcards[winner], topcards[1 - winner]])
    return deals


# part 2
d1, d2 = play_rec(I)
print(score(*[d1 or d2]))
