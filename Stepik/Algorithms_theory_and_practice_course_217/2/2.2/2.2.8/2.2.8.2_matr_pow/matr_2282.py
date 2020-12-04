"""This script computes n-th Fibonacci Number mod m"""


def fib_mod(n, m):
    """This function makes fast exponentiation of the given matrix in order to find
    n-th fibonacci number.At the same time it computes fib(n)mod m instead of
    calculating fibonacci numbers itself.There is used fast exponentiation alg"""
    pa, pb, pc, pd = 1, 0, 0, 1
    a, b, c, d = 1, 1, 1, 0

    if n == 0:
        return pb

    if n == 1:
        return b

    while n != 0:

        if n % 2 == 1:
            pat = a * pa + b * pc
            pbt = a * pb + b * pd
            pct = c * pa + d * pc
            pdt = c * pb + d * pd
            pa, pb, pc, pd = pat % m, pbt % m, pct % m, pdt % m
            n -= 1

        at = a * a + b * c
        bt = a * b + b * d
        ct = c * a + d * c
        dt = c * b + d * d
        a, b, c, d = at % m, bt % m, ct % m, dt % m
        n = n // 2

    return pb


def main():
    """Simple main function that takes n,m variables"""
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
