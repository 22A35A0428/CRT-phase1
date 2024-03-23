n=[42,36,28,96,-1,1]
m=n.copy()
for j in range (6,0,-1):
    for i in range(1,j):
        if n[i-1]>n[i]:
            temp=n[i]
            n[i]=n[i-1]
            n[i-1]=temp
print(n)
for j in range (6,0,-1):
    for i in range(1,j):
        if m[i-1]<m[i]:
            temp=m[i]
            m[i]=m[i-1]
            m[i-1]=temp            
print(m)