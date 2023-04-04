# ---------open-in-file----------------------
file_1 = open("18.txt", "r")

A_element = list(map(int, file_1.readline().split(':')))
A_s = (((60 * A_element[0]) + A_element[1]) * 60 + A_element[2])

B_element = list(map(int, file_1.readline().split(':')))
B_s = (((60 * B_element[0]) + B_element[1]) * 60 + B_element[2])

C_element = list(map(int, file_1.readline().split(':')))
C_s = (((60 * C_element[0]) + C_element[1]) * 60 + C_element[2])

file_1.close()
del file_1
# ---------close-in-file----------------------

D_s = ((60 * 24) * 60)
'''Суточное время | заготовка'''

if C_s <= A_s: C_s += D_s

average_s = ((C_s - A_s) * 10) / 2
if (average_s % 10) >= 5:
    average_s = int((average_s // 10) + 1)
elif (average_s % 10) == 0:
    average_s = int(average_s // 10)
elif (average_s % 10) < 5 and (average_s % 10) > 0:
    average_s = int((average_s // 10) - 1)

B_s += average_s
'''Серверное время плюс задержка'''

if B_s > D_s:
    B_s = B_s % D_s

B_sec = str(B_s % 60)
if len(B_sec) == 1: B_sec = '0' + B_sec
B_min = str((B_s // 60) % 60)
if len(B_min) == 1: B_min = '0' + B_min
B_hour = str((B_s // 60) // 60)
if len(B_hour) == 1: B_hour = '0' + B_hour

print(B_hour + ':' + B_min + ':' + B_sec, end = '')






