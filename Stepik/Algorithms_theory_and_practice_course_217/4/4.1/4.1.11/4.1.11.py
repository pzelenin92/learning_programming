"""Finding the sum of the natural items which equal the given number"""


def sum_natural_items(n):
    """Finds the sum"""
    items, delta_cur, k = [], n, 0
    if n in (1,2):
        print(1)
        print(n)
    else:
        while delta_cur > k:
            k += 1
            items.append(k)
            delta_prev, delta_cur = delta_cur, delta_cur - k

        items[-1] = delta_prev
        print(len(items))
        for i in items:
            print(i, end=' ')


def main():
    """main function"""
    n = int(input())
    sum_natural_items(n)


if __name__ == '__main__':
    main()
