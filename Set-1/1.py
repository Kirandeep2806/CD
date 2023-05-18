#!/usr/bin/python3

import re

expr=input()

alphabets=r'[a-zA-Z_]+'
specialSymbols=r'[^a-zA-Z0-9.]'
numbers=r'[0-9.]+'

a=[]
s=[]
n=[]

val={"*":"Multiplications","^":"Exponent","%":"Modulo Division","+":"Addition","-":"Subtraction","=":"Equality","/":"Division"," ":"Space", ";": "Semi-colon"}

tknum=1

for i in re.finditer(alphabets, expr):
    a.append([i.start(0),i.group(),f"<id,{tknum}>", "Identifier"])
    tknum+=1

for i in re.finditer(specialSymbols, expr):
    s.append([i.start(0),i.group(),f"<{i.group()}>",val[i.group()]])

for i in re.finditer(numbers, expr):
    txt="Number"
    if "." in i.group():
        txt="Floating "+txt
    else:
        txt="Decimal "+txt
    n.append([i.start(0),i.group(),i.group(), txt])

res=sorted(a+s+n, key=lambda x:x[0])
del a,s,n
for i in res:
    i.pop(0)

print("Lexems\tToken\tPattern")
print("-"*30)
for i in res:
    print(f"{i[0]}\t{i[1]}\t{i[2]}")
