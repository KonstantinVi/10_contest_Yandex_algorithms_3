# ------open-file-----------------------
file_1 = open("14.txt", "r")

# получение количества замен
char_01 = file_1.readline()
char_01 = int(char_01.rstrip('\n'))

# получение строки данных
char_02 = file_1.readline()
char_02 = char_02.rstrip('\n')
file_1.close()
# ------close-file----------------------

char_02 = tuple(char_02)

out_char = 0  # максимум красоты

#abc = 'abcdefijklmnopqrstuvwxyz'
abc = tuple(set(char_02))


for ii in abc:  # выдаёт уникальные символы

    j = char_01  # возможное количество изменений
    k = 0  # правый указатель | статрт с начала списка
    max_char = 0

    for i in range(len(char_02)):  # левый указатель
        if max_char > 0: max_char -= 1  # при перемещении левого указателя вправо
        while k < len(char_02) and (j > 0 or char_02[k] == ii):
            if char_02[k] != ii:
                j -= 1
            k += 1
        max_char = k - i
        out_char = max(out_char, max_char)

        if char_02[i] != ii and j < char_01:
            j += 1

print(out_char)
