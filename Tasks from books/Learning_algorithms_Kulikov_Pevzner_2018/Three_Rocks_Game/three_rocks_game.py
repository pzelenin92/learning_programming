"""There is simple algo of Three Rocks Game. You Win or Lose based on win_or_lose_table(n,m)"""


def three_rocks(n, m):
    """Finds solution (win or lose) based on quantity of stones in the left and right"""
    dict_mods = {0: 2, 1: 1, 2: 0, 3: 3}  # mods which leads to lost combination
    # boundary solution
    if n == 0 and m == 0:
        ans = 'L'
    elif n == 0:
        if m % 4 == 0:
            ans = 'L'
        else:
            ans = 'W'
    elif m == 0:
        if n % 4 == 0:
            ans = 'L'
        else:
            ans = 'W'
    # inbound solution
    x = (n + 1) % 4
    y = (m + 1) % 4
    if dict_mods[x] == y:
        ans = 'L'
    else:
        ans = 'W'

    return ans


def main():
    """Takes input"""
    # n,m = (int(i) for i in input().split())
    n, m = map(int, input().split())
    print(three_rocks(n, m))


if __name__ == "__main__":
    main()
