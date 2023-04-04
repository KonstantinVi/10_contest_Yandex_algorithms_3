# ---------open-in-file----------------------
file_1 = open("01.txt", "r")

M = int(file_1.readline())
''' количество секторов '''
N = int(file_1.readline())
''' количество разделов на диске '''
if N != 0:
    a_mass = []
    one_element = sorted(map(int, file_1.readline().split())) + [True]
    '''массив (минимальная точка, максимальная точка, True / False)'''
    a_mass.append(one_element)
    for i in range(0, N - 1):
        one_element = sorted(map(int, file_1.readline().split())) + [True]

        # -------------------- элементы ---------------------------
        # a - a_mass[j][0]
        # b - a_mass[j][1]

        # c - one_element[0]
        # d - one_element[1]

        # Flag -  - one_element[2]
        # -------------------- элементы ---------------------------

        for j in range(len(a_mass)):
            # c > b and d > b
            # c < a and d < a
            if (one_element[0] > a_mass[j][1]) and (one_element[1] > a_mass[j][1]):
                pass
            elif (one_element[0] < a_mass[j][0]) and (one_element[1] < a_mass[j][0]):
                pass
            else:
                a_mass[j][2] = False
        a_mass.append(one_element)

    counter_one = 0
    for i in range(len(a_mass)):
        if a_mass[i][2] == True:
            counter_one += 1

    print(counter_one)

else:
    print(0)
file_1.close()
del file_1
# ---------close-in-file----------------------



