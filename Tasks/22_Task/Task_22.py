# ---------open-in-file----------------------
file_1 = open("06.txt", "r")
N, k = map(int, file_1.readline().rstrip('\n').split())
file_1.close()
del file_1
# ---------close-in-file----------------------

dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    for j in range(1, k+1):
        if i-j >= 1:
            dp[i] += dp[i-j]

print(dp[N])



