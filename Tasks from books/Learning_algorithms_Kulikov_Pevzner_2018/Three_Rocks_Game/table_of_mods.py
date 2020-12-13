"""There i printed mods of given matrix and trying to find out which mods are leading to
    lost combination. The losing mods are (0, 2) (1, 1) (2, 0) (3, 3)"""

n, m = 10, 10  # given matrix

matr = [[[] for j in range(m + 1)] for i in range(n + 1)]  # construction empty matrix to print

for i in range(n + 1):  # printing empty matrix for visualisation
    print(matr[i])
print()

for i in range(1, n + 1):  # calculating mods and insert to corresponding cell
    for j in range(1, m + 1):
        x = (i + 1) % 4
        y = (j + 1) % 4
        matr[i][j] = [x, y]

# printing matrix with mods
print(end='   ')
for i in range(n + 1):
    print(i, end='       ')
print()
for i in range(n + 1):
    print(i, matr[i])
