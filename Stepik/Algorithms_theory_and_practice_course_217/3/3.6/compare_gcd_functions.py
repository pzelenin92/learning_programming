"""There i am comparing 4 algs which find Greatest"""
from time import perf_counter
from matplotlib import pyplot as plt


def gcd1(a, b):
    """Naive iterative version"""
    assert a >= 0 and b >= 0
    for d in reversed(range(1, max(a, b) + 1)):
        if a % d == b % d == 0:
            return d
    return 0


def gcd2(a, b):
    """Iterative Euclidean version"""
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd3(a, b):
    """Recursive version"""
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    if a >= b:
        return gcd3(a % b, b)
    return gcd3(a, b % a)


def gcd4(a, b):
    """Fast Recursive version"""
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)


def timed(f, args, n_iter=100):
    """Calculate the time of function's execution"""
    acc = float('inf')
    for i in range(n_iter):
        t0 = perf_counter()
        f(*args)
        t1 = perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare_delta_const(fs, steps, delta):
    """Plots the execution time for different functions with delta = const and compares them"""
    for f in fs:
        plt.plot(steps, [timed(f, (step, step + delta)) for step in steps], label=f.__name__)
        plt.legend()
        plt.xlabel('Number of steps')
        plt.ylabel('Time')
        plt.title('Comparing execution time')
        plt.text(30, 8e-6, 'diff between a and b == 20 \non every step')
        plt.grid(True)
    plt.show()


def compare_delta_var(f, steps, deltas):
    """Plots the execution time for chosen function with diff deltas and compares them"""
    for delta in deltas:
        plt.plot(steps, [timed(f, (step, step + delta)) for step in steps], label=delta)
        plt.legend()
        plt.grid(True)
    plt.show()


def main():
    """main function"""
    compare_delta_const([gcd1, gcd2, gcd3, gcd4], list(range(100)), 20)


if __name__ == '__main__':
    main()
