# ---------open-in-file----------------------
file_1 = open("01.txt", "r")

N = int(file_1.readline())
'''количество учеников в классе'''
K = int(file_1.readline())
'''количество вариантов задач'''
row = int(file_1.readline())
'''номер ряда Пети'''
place = int(file_1.readline())
'''номер места'''

file_1.close()
del file_1
# ---------close-in-file----------------------


# --------- какая у Пети задача? -------------
if row == 1:
    division_of_the_whole = place
elif row > 1:
    task_before = 2 * row
    division_of_the_whole = (task_before % K)
    if division_of_the_whole == 0: division_of_the_whole = K
    if place == 1:
        division_of_the_whole -= 1
# --------- какая у Пети задача --------------

#print(f'Номер задачи Пети: {division_of_the_whole}')

id_Petya = (2 * (row - 1)) + place
''' Порядковый номер Пети '''
# print(f'Номер Пети: {id_Petya}')
#
# number_of_tables_in_the_classroom = [(N // 2), (N % 2)]
# '''количество парт в классе'''
#
# number_of_tables = [(K // 2), (K % 2)]
# '''считаем сколько парт в задаче'''
#
# print(number_of_tables_in_the_classroom)
# print(number_of_tables)

if id_Petya + K < N:  # идём вверх
    row_V = (id_Petya + K) // 2
    place_V = (id_Petya + K) % 2
    if place_V == 0:
        place_V = 2
    print(row_V, place_V)

elif id_Petya - K > 0:  # идём вниз
    row_V = ((id_Petya - K) // 2) + 1
    place_V = (id_Petya - K) % 2
    if place_V == 0:
        place_V = 2
    print(row_V, place_V)

else: print(-1)