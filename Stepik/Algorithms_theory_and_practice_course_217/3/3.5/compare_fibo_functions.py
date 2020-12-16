"""There i am comparing 3 algs which finds Fibonacci Numbers"""
from time import perf_counter
from matplotlib import pyplot as plt


def fib1(n):
    """Recursive fibo"""
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib2(nn):
    """Recursive fibo + Getting from cache founded Fibo number"""
    cache = {}

    def fibin(n):
        assert n >= 0
        if n not in cache:
            cache[n] = n if n <= 1 else fibin(n - 1) + fibin(n - 2)
        return cache[n]

    return fibin(nn)


def fib3(n):
    """Iterative algo"""
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def timed(f, *args, n_iter=100):
    """Calculate the time of function's execution"""
    acc = float('inf')
    for i in range(n_iter):
        t0 = perf_counter()
        f(*args)
        t1 = perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare_timed(fs, args):
    """Plots the execution time for chosen fibo-functions and compares it"""
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


def main():
    """main function"""
    compare_timed([fib1, fib2, fib3], list(range(10)))


if __name__ == '__main__':
    main()
