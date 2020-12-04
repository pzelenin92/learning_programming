"""This module computes n-th Fibonacci number mod m"""


def fib_mod(n, m):
    """This funcion takes n-th Fibonacci number and computes n mod m"""

    def period(x):
        """This function finds Pizzano period. It takes number m as input, then finds f(n) mod m
        of the Fibonacci number through f(n)=(f(n-1)+f(n-2))mod m"""
        a, b, counter = 1, 1, 1  # a=1 -> last digit of the 1st fibo number, a=2 -> last digit of the 2nd fibo number
        while a != 0 or b != 1:
            f = (a + b) % x
            a, b = b, f
            counter += 1
        return counter

    a, b = 0, 1
    element = n % period(m)
    # if element != 0 and element != 1:
    if element not in (0, 1):
        for i in range(2, element + 1):
            f = (a + b) % m
            a, b = b, f
    else:
        f = element
    return f


def main():
    """Simple main funcion, takes n,m from keyboard"""
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
