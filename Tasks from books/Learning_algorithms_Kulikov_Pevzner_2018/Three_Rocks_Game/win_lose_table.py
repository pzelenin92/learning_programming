"""There i draw matrix with Win-Lose cells"""

n, m = 10, 11  # given matrix

matr = [['x' for j in range(m + 1)] for i in range(n + 1)]  # construction matrix with 'x' elements

for i in range(n + 1):  # printing praparatory matrix
    print(matr[i])
print()

# start filling the cells of the matrix
matr[0][0] = 'L'  # (0,0) element

for i in range(1, n + 1):  # filling border elements when i==0 or j ==0
    if i % 4 == 0:
        matr[i][0] = 'L'
    else:
        matr[i][0] = 'W'
for j in range(1, m + 1):
    if j % 4 == 0:
        matr[0][j] = 'L'
    else:
        matr[0][j] = 'W'

dict_mods = {0: 2, 1: 1, 2: 0, 3: 3}  # mods which leads to lost combination. i=key, j=value

for i in range(n + 1):  # filling remaining cells of the matrix
    for j in range(m + 1):
        if matr[i][j] == 'x':
            x = (i + 1) % 4
            y = (j + 1) % 4
            if dict_mods[x] == y:
                matr[i][j] = 'L'
            else:
                matr[i][j] = 'W'

for i in range(n + 1):  # printing resulting matrix
    print(matr[i])
