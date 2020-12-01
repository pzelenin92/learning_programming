
def fast_pow(x,n):
    p=1
    while n!=0:
        if n%2 == 1:
            p=p*x
            n-=1
        x=x**2
        n=n//2
    return p

print(fast_pow(2,13))
