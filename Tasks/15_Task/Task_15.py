# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

N_city = int(file_1.readline().rstrip('\n'))
tmp = list(map(int, file_1.readline().split()))

del file_1
# ---------close-in-file----------------------

Lainlandiya_city = []

# создаём двумерный массив | индекс, значение, новый город
for i in range(N_city):
    Lainlandiya_city.append([i, tmp[i], 0])

del tmp
del i

STACK = []

for i in range(N_city):

    # анализ стека новым элементом
    if len(STACK) != 0:

        while len(STACK) != 0 and STACK[-1][1] > Lainlandiya_city[i][1]:
            tmp = STACK[-1][0]
            Lainlandiya_city[tmp][2] = Lainlandiya_city[i][0]
            del STACK[-1]
        else: STACK.append(Lainlandiya_city[i])

    else: STACK.append(Lainlandiya_city[i])

while len(STACK) != 0:
    tmp = STACK[-1][0]
    Lainlandiya_city[tmp][2] = -1
    del STACK[-1]

for i in range(N_city):
    print(Lainlandiya_city[i][2], end=' ')