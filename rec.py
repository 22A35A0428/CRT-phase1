def f(n):
    if n==0:
        return 1
    return n*f(n-1)
a=f(5)
print(f(5))
print(a)