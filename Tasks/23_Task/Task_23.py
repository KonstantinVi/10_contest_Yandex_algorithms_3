# ---------open-in-file----------------------
file_1 = open("02.txt", "r")
n = int(file_1.readline().rstrip('\n'))
file_1.close()
del file_1
# ---------close-in-file----------------------

dp = [0] * (n + 1)
a_mass = [0] * (n + 1)

for i in range(2, n + 1):
    # плюс единица
    dp[i] = dp[i - 1] + 1
    a_mass[i] = i - 1

    # умножить число X на 2
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        a_mass[i] = i // 2

    # умножить число X на 3
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        a_mass[i] = i // 3

k = [n]
m = n
while m != 1:
    k.append(a_mass[m])
    m = a_mass[m]

print(dp[n])
print(*k[::-1])
