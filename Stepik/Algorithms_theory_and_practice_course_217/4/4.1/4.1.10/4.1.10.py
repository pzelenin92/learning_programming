"""This script solves the problem of continuous rucksack with greedy algorithm"""


def max_rucksack_cap(capacity, items):
    """function that puts optimal quantity of items in order to maximize its overall price"""

    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    maxprice = 0

    for item in items:
        if item[1] < capacity:
            maxprice += item[0]
            capacity -= item[1]
        else:
            maxprice += (item[0] / item[1]) * capacity
            break

    print(format(maxprice, '.3f'))


def main():
    """main function"""
    n, capacity = map(int, input().split())
    items = []
    while n > 0:
        input_item = [int(i) for i in input().split()]
        if 0 not in input_item:
            items.append(input_item)
        n -= 1

    max_rucksack_cap(capacity, items)


if __name__ == '__main__':
    main()
