n=[42,36,28,96,-1,1]
m=[42,36,28,96,-1,1]
for j in range (1,6):
    for i in range(1,6):
        if n[i-1]>n[i]:
            temp=n[i]
            n[i]=n[i-1]
            n[i-1]=temp
print(n)
for j in range (1,6):
    for i in range(1,6):
        if m[i-1]<m[i]:
            temp=m[i]
            m[i]=m[i-1]
            m[i-1]=temp            
# a=n[i]
print(m)
