#!/usr/bin/python3

expr = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}

with open("IntermediateCode.txt", "r") as file:
    for i in file.readlines():
        flag = False
        s = i[:len(i)-1]
        t = s.split("=")
        prev = ""
        for char in t[1]:
            prev = prev.strip()
            if expr.get(char, -1)!=-1:
                print(f"LDA {prev}")
                print(f"{expr[char]}", end=" ")
                flag = True
                prev = ""
            else:
                prev += char
        if prev:
            if flag:
                print(prev)
            else:
                print(f"LDA {prev}")
        print(f"STA {t[0]}")
