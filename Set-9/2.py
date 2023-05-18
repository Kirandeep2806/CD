#!/usr/bin/python3

from string import ascii_lowercase
from collections import defaultdict

# prods = '''E -> E+T | T
# T -> a'''

# prods = '''A->B+C
# B->a
# C->b'''

prods = '''S->A|Bd
A->a
B->c'''

prods = prods.splitlines()

d = {}

def leftRecursionElimination(lhs, prod):
    prod[lhs + "'"] = [prod[lhs][0][1:] + lhs + "'", "eps"]
    prod[lhs] = [prod[lhs][1] + lhs + "'"]

# FIRST

for i in prods:
    lhs, rhs = i.split("->")
    d[lhs.strip()] = [i.strip() for i in rhs.split("|")]

temp = d.copy()
for i in temp:
    if i == temp[i][0][0]:
        leftRecursionElimination(i, d)

nonTerminals = set(list("+-/%^" + ascii_lowercase))

def findFirst(head, prod, res: list):
    for rhs in prod[head]:
        if rhs == "eps":
            res.append("eps")
        elif rhs[0] in nonTerminals:
            res.append(rhs[0])
        else:
            findFirst(rhs[0], prod, res)

first = {}
for i in d:
    res = []
    findFirst(i, d, res)
    first[i] = set(res)
    print(f"FIRST({i}) = {set(res)}")


# FOLLOW

start = "A"
# start = "S"

def findFollow(head, d: dict[str, list], res: list):
    for j in d:
        for k in d[j]:
            if head in k:
                if k.find(head) == len(k)-1:
                    res.append(*follow[j])
                else:
                    beta = k[k.index(head) + 1]
                    if beta in nonTerminals:
                        res.append(beta)
                    else:
                        if "eps" not in first[beta]:
                            res.append(first[beta])
                        else:
                            res.append((first[beta] - {"eps"}) | follow[j])

follow = {}

for i in d:
    if i == start:
        print(f"FOLLOW({i}) = {{'$'}}")
        follow[i] = {"$"}
    else:
        res = []
        findFollow(i, d, res)
        follow[i] = set(res)
        print(f"FOLLOW({i}) = {follow[i]}")


print("\n\nLL(1) parsing table : ")

llTable = defaultdict(dict)

for i in d:
    for j in first[i]:
        llTable[i][j] = i + " -> " + j

print(llTable)
