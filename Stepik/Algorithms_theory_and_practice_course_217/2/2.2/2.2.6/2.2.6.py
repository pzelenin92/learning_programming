def fib(n):
    # put your code here
    fvl0,fvl1,i=0,1,2
    if n==1:
        fvl=1
    else:
        while i<=n:
            fvl=fvl0+fvl1
            fvl0,fvl1=fvl1,fvl
            i+=1
    return fvl

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
