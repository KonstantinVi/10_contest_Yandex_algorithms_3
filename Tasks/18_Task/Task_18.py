# ---------open-in-file----------------------
file_1 = open("03.txt", "r")

file_2 = file_1.readline()
deque_command = []
''' список команд '''
while file_2 != '':
    deque_command.append(file_2.rstrip('\n').split())
    file_2 = file_1.readline()
file_1.close()

del file_1
del file_2
# ---------close-in-file----------------------

# deque_command - список команд в очереди
size_deque_command = len(deque_command)
''' размер списка команд '''

if size_deque_command != 0:
    queue_box = []
    ''' ОЧЕРЕДЬ '''

    for i in range(size_deque_command):
        if deque_command[i][0] == 'push_front':
            queue_box.insert(0, int(deque_command[i][1]))
            print('ok')

        elif deque_command[i][0] == 'push_back':
            queue_box.append(int(deque_command[i][1]))
            print('ok')

        elif deque_command[i][0] == 'pop_front':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[0])
            del queue_box[0]

        elif deque_command[i][0] == 'pop_back':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[-1])
            del queue_box[-1]

        elif deque_command[i][0] == 'front':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[0])

        elif deque_command[i][0] == 'back':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[-1])

        elif deque_command[i][0] == 'size':
            print(len(queue_box))

        elif deque_command[i][0] == 'clear':
            queue_box = []
            print('ok')

        elif deque_command[i][0] == 'exit':
            print('bye')
            break
