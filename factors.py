n=47
b=n
a=0
while n>0:
    a=a+n%10
    n=n//10
print(a)
if b%a==0:
    print("divisable")
else:
    print("not")