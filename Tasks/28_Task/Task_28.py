# ---------open-in-file----------------------
file_1 = open("02.txt", "r")

N, M = map(int, file_1.readline().split())

file_1.close()

del file_1
# ---------close-in-file----------------------

horse_path = [[0] * M for _ in range(N)]

horse_path[0][0] = 1

for i in range(N):
    for j in range(M):
        if i > 1 and j > 0:
            horse_path[i][j] += horse_path[i - 2][j - 1]
        if i > 0 and j > 1:
            horse_path[i][j] += horse_path[i - 1][j - 2]

i = N - 1
j = M - 1
print(horse_path[i][j])
