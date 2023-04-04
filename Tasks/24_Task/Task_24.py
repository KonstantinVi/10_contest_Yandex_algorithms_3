# ---------open-in-file----------------------
file_1 = open("01.txt", "r")

N = int(file_1.readline().rstrip('\n'))
sec_mass = []
for _ in range(N):
    sec_mass.append(list(map(int, file_1.readline().rstrip('\n').split())))

file_1.close()

del file_1
del _
# ---------close-in-file----------------------

dp = [0] * (N + 1)

dp[1] = (sec_mass[0][0])

for i in range(2, N + 1):
    if i == 2:
        dp[i] = min(dp[i - 1] + sec_mass[i - 1][0],
                    dp[i - 2] + sec_mass[i - 2][1])

    elif i >= 3:
        dp[i] = min(dp[i - 1] + sec_mass[i - 1][0],
                    dp[i - 2] + sec_mass[i - 2][1],
                    dp[i - 3] + sec_mass[i - 3][2])

print(dp[N])

