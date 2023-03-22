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


# def play_rec(d1, d2):
#     pass


# part 2
# print(score([*play_rec(*(map(deque, I)))]))
