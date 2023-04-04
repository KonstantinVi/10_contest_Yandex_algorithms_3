# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

N, M, Q = map(int, file_1.readline().split())

big_mass = []
''' big matrix number'''
for i in range(N):
    a = list(map(int, file_1.readline().split()))
    big_mass.append(a)

request_mass = []
''' coordinates: Y1, X1, Y2, X2 '''
for i in range(Q):
    a = list(map(int, file_1.readline().split()))
    request_mass.append(a)

file_1.close()
del i
del a
del file_1
# ---------close-in-file----------------------
# x - vertical
# y - horizontal

if N != 0 and M != 0:

    for i in range(N):
        if i == 0:
            for j in range(1, M):
                big_mass[i][j] += big_mass[i][j-1]
        elif i != 0:
            for j in range(1, M):
                big_mass[i][j] += big_mass[i][j - 1]
                big_mass[i][j-1] += big_mass[i-1][j-1]
            big_mass[i][-1] += big_mass[i - 1][-1]

    # request_mass - запросы Y1, X1, Y2, X2
    for i in range(Q):

        x1 = request_mass[i][0] - 1
        y1 = request_mass[i][1] - 1
        x2 = request_mass[i][2] - 1
        y2 = request_mass[i][3] - 1

        if x1 == 0 and y1 == 0:  # x1 = 0 and y1 = 0
            CHAR_ONE = big_mass[x2][y2]
            print(CHAR_ONE)

        elif y1 == 0:  # y1 = 0
            one_cube = big_mass[x2][y2]
            one_mines = big_mass[x1-1][y2]
            CHAR_ONE = one_cube - one_mines
            print(CHAR_ONE)

        elif x1 == 0:  # x1 = 0
            one_cube = big_mass[x2][y2]
            one_mines = big_mass[x2][y1-1]
            CHAR_ONE = one_cube - one_mines
            print(CHAR_ONE)

        else:
            one_cube = big_mass[x2][y2]
            one_mines_one = big_mass[x1 - 1][y2]
            one_mines_two = big_mass[x2][y1 - 1]
            one_mines_tree = big_mass[x1 - 1][y1 - 1]
            CHAR_ONE = one_cube - (one_mines_one + one_mines_two) + one_mines_tree
            print(CHAR_ONE)

else: print(0)

