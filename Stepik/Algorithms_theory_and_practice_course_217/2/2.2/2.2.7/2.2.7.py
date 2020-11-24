def fib_digit(n):
    a0,a1,i=0,1,2
    if n==1:
        a2=1
    else:
        while i<=n:
            a2=(a0+a1)%10
            a0,a1=a1,a2
            i+=1
    return a2


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
