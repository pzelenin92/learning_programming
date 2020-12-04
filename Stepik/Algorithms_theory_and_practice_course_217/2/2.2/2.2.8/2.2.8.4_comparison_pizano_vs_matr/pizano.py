def fib_mod(n, m):
    def period(x):
        a,b,counter=1,1,1
        while a!=0 or b!=1:
            f=(a+b)%x
            a,b=b,f
            counter+=1
        return counter
    a,b=0,1
    element=n%period(m)
    if element != 0 and element != 1:
        for i in range(2,element+1):
            f=(a+b)%m
            a,b=b,f
    else:
        f=element
    return f

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
