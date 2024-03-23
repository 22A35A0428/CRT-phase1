def me():
    n=int(input("hi"))
    for i in range(2,n):
        if n%i==0:
            f=0
            break
    if f==0:
        print("no")
    else:
        print("not")
me()