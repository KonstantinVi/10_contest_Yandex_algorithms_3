# ---------open-in-file----------------------
file_1 = open("02.txt", "r")

N = int(file_1.readline().rstrip('\n'))

file_2 = file_1.readline()
in_command = []
''' список команд '''
while file_2 != '':
    in_command.append(file_2.rstrip('\n').split())
    file_2 = file_1.readline()
file_1.close()

del file_1
del file_2
# ---------close-in-file----------------------

in_command = in_command[::-1]

if len(in_command) != 0:
    heap_box = []
    ''' create КУЧА '''

    while len(in_command) != 0:
        if in_command[-1][0] == '0':  # insert | добавление
            heap_box.append(int(in_command[-1][1]))

            if len(heap_box) > 1:
                i = len(heap_box) - 1
                j = (i - 1) // 2

                while heap_box[i] > heap_box[j] and i != 0:
                    heap_box[i], heap_box[j] = heap_box[j], heap_box[i]
                    i = j
                    j = (i - 1) // 2


        elif in_command[-1][0] == '1':  # extract | удаление
            print(heap_box[0])
            heap_box[0], heap_box[-1] = heap_box[-1], heap_box[0]
            del heap_box[-1]

            i = 0
            n = len(heap_box)
            while True:
                max_ind = i
                j = 2 * i + 1  # левый ребёнок
                k = 2 * i + 2  # правй ребёнок

                if j < n and heap_box[i] < heap_box[j]:
                    max_ind = j
                if k < n and heap_box[max_ind] < heap_box[k]:
                    max_ind = k

                if max_ind != i:
                    heap_box[i], heap_box[max_ind] = heap_box[max_ind], heap_box[i]

                if max_ind == i: break

                i = max_ind


        del in_command[-1]
