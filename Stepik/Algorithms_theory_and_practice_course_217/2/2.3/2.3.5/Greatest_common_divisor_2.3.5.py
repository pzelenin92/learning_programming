"""Iterative Euclidean algorithm"""


def gcd(a, b):
    """Function that finds greatest common divisor"""
    if a > b:
        big_number, remainder = a, b
    else:
        big_number, remainder = b, a
    while remainder > 0:
        big_number, remainder = remainder, big_number % remainder
    return big_number  # we return big_number because remainder from previous iter was assigned to this big_number
    # in the last iter remainder = 0, thus we need to get it from previous iter


def main():
    """input and print func"""
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
