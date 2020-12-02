def fast_pow_matr(n):

    pa,pb,pc,pd=1,0,0,1
    a, b, c, d = 1, 1, 1, 0

    if n ==0:
        return pb

    elif n ==1:
        return b

    else:
        while n!=0:

            if n%2 == 1:

                pat = a * pa + b * pc
                pbt = a * pb + b * pd
                pct = c * pa + d * pc
                pdt = c * pb + d * pd
                pa,pb,pc,pd = pat, pbt, pct, pdt
                n-=1

            at = a * a + b * c
            bt = a * b + b * d
            ct = c * a + d * c
            dt = c * b + d * d
            a,b,c,d = at, bt, ct, dt
            n= n // 2

        return pb

def main():
    n = int(input())
    print(fast_pow_matr(n))


if __name__ == "__main__":
    main()
