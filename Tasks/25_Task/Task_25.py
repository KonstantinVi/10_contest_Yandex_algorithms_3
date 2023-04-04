# ---------open-in-file----------------------
file_1 = open("01.txt", "r")

n = int(file_1.readline().rstrip('\n'))
a_mass = list(map(int, file_1.readline().split()))
a_mass.sort()

del file_1
# ---------close-in-file----------------------

dp = [0 for i in range(n)]
dp[1] = a_mass[1] - a_mass[0]
if n > 2:
    dp[2] = a_mass[2] - a_mass[0]
    for i in range(3, n):
        dp[i] = min(dp[i - 2], dp[i - 1]) + a_mass[i] - a_mass[i - 1]
print(dp[n - 1])
