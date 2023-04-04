# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

poland_line = file_1.readline().rstrip('\n').split()

file_1.close()
del file_1
# ---------close-in-file----------------------

STEK_one = []
if len(poland_line) != 0:
    for i in range(len(poland_line)):
        if poland_line[i] not in '+-*':
            STEK_one.append(int(poland_line[i]))
        elif poland_line[i] == '+':
            tmp = STEK_one[-2] + STEK_one[-1]
            STEK_one.pop()
            STEK_one[-1] = tmp
        elif poland_line[i] == '-':
            tmp = STEK_one[-2] - STEK_one[-1]
            STEK_one.pop()
            STEK_one[-1] = tmp
        elif poland_line[i] == '*':
            tmp = STEK_one[-2] * STEK_one[-1]
            STEK_one.pop()
            STEK_one[-1] = tmp
    print(*STEK_one)
else: print(0)