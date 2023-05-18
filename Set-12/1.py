#!/usr/bin/python3

from string import ascii_lowercase

prods = '''E -> E+T | T
T -> a'''

# prods = '''A->B+C
# B->a
# C->b'''

# prods = '''S->A|Bd
# A->a
# B->c'''

prods = prods.splitlines()

d = {}

def leftRecursionElimination(lhs, prod):
    prod[lhs + "'"] = [prod[lhs][0][1:] + lhs + "'", "eps"]
    prod[lhs] = [prod[lhs][1] + lhs + "'"]

for i in prods:
    lhs, rhs = i.split("->")
    d[lhs.strip()] = [i.strip() for i in rhs.split("|")]

temp = d.copy()
for i in temp:
    if i == temp[i][0][0]:
        leftRecursionElimination(i, d)

nonTerminals = set(list("+-/%^" + ascii_lowercase))

def solve(head, prod, res: list):
    for rhs in prod[head]:
        if rhs == "eps":
            res.append("eps")
        elif rhs[0] in nonTerminals:
            res.append(rhs[0])
        else:
            solve(rhs[0], prod, res)

first = {}
for i in d:
    res = []
    solve(i, d, res)
    first[i] = set(res)
    print(f"FIRST({i}) = {set(res)}")
