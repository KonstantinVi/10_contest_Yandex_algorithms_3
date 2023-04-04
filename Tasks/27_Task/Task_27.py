# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

N, M = map(int, file_1.readline().split())
a_mass = [[0 for _ in range(M + 1)]]
for _ in range(N + 1):
    a = list(map(int, file_1.readline().rstrip('\n').split()))
    a = [0] + a
    a_mass.append(a)

file_1.close()

del file_1
del _
del a
del a_mass[-1]
# ---------close-in-file----------------------

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1] = a_mass[1][1]

for j in range(2, M + 1): dp[1][j] = dp[1][j-1] + a_mass[1][j]
for i in range(2, N + 1): dp[i][1] = dp[i-1][1] + a_mass[i][1]

for i in range(2, N + 1):
    for j in range(2, M + 1):
        if dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + a_mass[i][j]
        else:
            dp[i][j] = dp[i][j-1] + a_mass[i][j]

i = N
j = M
turtle_way = []
while i > 0 and j > 0:
    if i == 1 and j == 1: break
    if dp[i - 1][j] > dp[i][j - 1] and i - 1 != 0:
        turtle_way.append('D')
        i -= 1
    elif dp[i][j - 1] >= dp[i - 1][j] and j - 1 != 0:
        turtle_way.append('R')
        j -= 1
    elif dp[i - 1][j] == dp[i][j - 1] and i - 1 != 0:
        turtle_way.append('D')
        i -= 1
    elif dp[i][j - 1] == dp[i - 1][j] and j - 1 != 0:
        turtle_way.append('R')
        j -= 1

print(dp[N][M])
print(*turtle_way[::-1], sep='')