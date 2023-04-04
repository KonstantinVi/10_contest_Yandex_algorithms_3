# ---------open-in-file----------------------
file_1 = open("08.txt", "r")

N, M = map(int, file_1.readline().split())
a_mass = []
for _ in range(N):
    a_mass.append(list(map(int, file_1.readline().rstrip('\n').split())))

file_1.close()

del file_1
del _
# ---------close-in-file----------------------

dp = [[0] * M for _ in range(N)]
dp[0][0] = a_mass[0][0]

for i in range(1, M): dp[0][i] = dp[0][i - 1] + a_mass[0][i]
for j in range(1, N): dp[j][0] = dp[j - 1][0] + a_mass[j][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = a_mass[i][j] + min(dp[i - 1][j], dp[i][j - 1])

i = N - 1
j = M - 1
print(dp[i][j])

