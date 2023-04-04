# ---------open-in-file----------------------
file_1 = open("08.txt", "r")
n = int(file_1.readline().rstrip('\n'))
file_1.close()
del file_1
# ---------close-in-file----------------------

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 2
if len(dp) > 2:
    dp[2] = 4

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(dp[n])

