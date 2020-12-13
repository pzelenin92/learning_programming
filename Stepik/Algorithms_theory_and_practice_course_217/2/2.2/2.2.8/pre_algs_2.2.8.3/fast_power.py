"""Simple algorithm of fast powering"""


def fast_pow(x, n):
    """x multiplies n times"""
    p = 1
    while n != 0:
        if n % 2 == 1:
            p = p * x
            n -= 1
        x = x ** 2
        n = n // 2
    return p


print(fast_pow(3, 5))
