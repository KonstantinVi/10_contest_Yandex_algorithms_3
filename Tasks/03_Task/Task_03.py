# ---------open-in-file----------------------
file_1 = open(r"03_Task_Test\10.txt", "r")

diego_01 = int(file_1.readline())  # количество наклеек у Диего
diego_02 = sorted(set(map(int, file_1.readline().split())))  # номера которые есть у Диего

guest_01 = int(file_1.readline())  # количество коллекционеров пришедших к Диего
guest_02 = tuple(map(int, file_1.readline().split()))  # наименьший номер наклейки i-го коллекционера
file_1.close()
del file_1
# ---------close-in-file----------------------

a_mass = []  # вывод значений

for k in guest_02:
    # ---------цикл бинарного поиска---------
    left_ind = -1
    right_ind = len(diego_02)
    while right_ind > left_ind + 1:
        median = (left_ind + right_ind) // 2
        if diego_02[median] >= k:  # k - это искомое число
            right_ind = median
        else:
            left_ind = median
    # ---------цикл бинарного поиска---------> right

    print(right_ind)

