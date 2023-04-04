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

#print(*a_mass, sep='\n')
#print('\n'.join(map(str, a_mass)))

# ---------open-out-file---------------------
#file_3 = open("output.txt", "w")
#for i in range(len(a_mass)):  # построчный вывод
#    if i != (len(a_mass) - 1):
#        file_3.write(f'{a_mass[i]}\n')
#    else:
#        file_3.write(f'{a_mass[i]}')
#file_3.close()
# ---------close-out-file---------------------
