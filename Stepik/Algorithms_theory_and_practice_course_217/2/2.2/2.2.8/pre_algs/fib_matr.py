def find_fib_matr(n):

    pc,pd = (i for i in fast_pow_matr(n))
    rn, rn_minus_1 = 1, 0
    fn = pc * rn + pd * rn_minus_1

    return fn

def fast_pow_matr(n,pa=1,pb=0,pc=0,pd=1):

    a, b, c, d = 1, 1, 1, 0

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
        n=n//2

    pc_pd=[pc,pd]
    return pc_pd

def main():
    n = int(input())
    print(find_fib_matr(n))


if __name__ == "__main__":
    main()
