#!/usr/bin/python3

with open("1.py") as file:
    s=file.read()
    d={"Spaces":0, "Characters":0, "Lines":1, "Tabs": 0, "Words": 0, "Special Characters": 0, "Numbers": 0}
    t=s.split()
    d["Words"]=len(t)
    for i in s:
        if ord(i)==9:
            d["Tabs"]+=1
        elif ord(i)==10:
            d["Lines"]+=1
        elif ord(i)==32:
            d["Spaces"]+=1
        elif i.isalpha():
            d["Characters"]+=1
        elif i.isnumeric():
            d["Numbers"]+=1
        else:
            d["Special Characters"]+=1

    for i,j in d.items():
        print(f"{i} : {j}")
