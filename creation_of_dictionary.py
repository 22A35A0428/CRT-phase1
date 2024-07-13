d={
    11:"me",
    22:"you",
    35:"none"
}
d[29]="narasimha"
d[22]=11
for i in d:
    print(i)
for t in d.values():
    print(t)
for c,e in d.items():
    print(c,e)
d.pop(35)
for c,d in d.items():
    print(c,d)
