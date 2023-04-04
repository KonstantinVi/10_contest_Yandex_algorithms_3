# ---------open-in-file----------------------
file_1 = open("02.txt", "r")

M = int(file_1.readline())
m_word = list(map(int, file_1.readline().rstrip('\n').split()))
N = int(file_1.readline())
n_word = list(map(int, file_1.readline().rstrip('\n').split()))

file_1.close()

del file_1
# ---------close-in-file----------------------

# поиск совпадений подпоследовательности
dp = [[0] * (M + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif n_word[i - 1] == m_word[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# поиск состава подпоследовательности
i = N
j = M
end_position = dp[N][M]
subsequence = [''] * (end_position + 1)
subsequence[end_position] = ''
while i > 0 and j > 0:
    if n_word[i - 1] == m_word[j - 1]:
        subsequence[end_position - 1] = str(n_word[i - 1])
        i -= 1
        j -= 1
        end_position -= 1
    elif dp[i - 1][j] > dp[i][j - 1]: i -= 1
    else: j -= 1

print(*subsequence, sep=' ')
