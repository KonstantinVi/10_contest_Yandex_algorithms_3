# ---------open-in-file----------------------
file_1 = open("14.txt", "r")

number_wagons = int(file_1.readline())
''' количество вагонов '''
train_line = file_1.readline().rstrip('\n').split()
train_line = train_line[::-1]
''' поезд '''

file_1.close()
del file_1
# ---------close-in-file----------------------

MEMORY_STACK = []
''' тупик '''

left_path = []
counter_input = number_wagons
''' счётчик вхождений в стек '''
counter_output = number_wagons
''' счётчик выхождений из стека '''
counter_baza = counter_input + counter_output
while counter_input > 0 or counter_output > 0:

    if len(train_line) > 0:
        MEMORY_STACK.append(train_line[-1])  # добавление в стек нового вагона
        counter_input -= 1
        train_line.pop()

    if len(left_path) == 0 and MEMORY_STACK[-1] == '1':  # если путь 2 пуст, то добавляем только 1 вагон
        left_path.append(MEMORY_STACK[-1])
        counter_output -= 1
        MEMORY_STACK.pop()
        if len(train_line) == 0 and len(MEMORY_STACK) == 0:
            print('YES', end='')
            break

    while len(left_path) > 0 and len(MEMORY_STACK) != 0 and (int(left_path[-1]) + 1) == int(MEMORY_STACK[-1]):  # если путь 2 не свободен, то добавляем следующий эелемент по порядку
        left_path.append(MEMORY_STACK[-1])
        counter_output -= 1
        MEMORY_STACK.pop()
        if len(train_line) == 0 and len(MEMORY_STACK) == 0:
            print('YES', end='')
            break

    counter_baza -= 1
    if counter_baza <= 0:
        print('NO', end='')
        break
