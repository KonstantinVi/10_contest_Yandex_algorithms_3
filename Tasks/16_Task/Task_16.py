# ---------open-in-file----------------------
file_1 = open("03.txt", "r")

file_2 = file_1.readline()
stack_command = []
''' список команд '''
while file_2 != '':
    stack_command.append(file_2.rstrip('\n').split())
    file_2 = file_1.readline()
file_1.close()

del file_1
del file_2
# ---------close-in-file----------------------

# stack_command - список команд
size_stack_command = len(stack_command)
''' размер списка '''

if size_stack_command != 0:
    queue_box = []
    ''' ОЧЕРЕДЬ '''

    for i in range(size_stack_command):
        if stack_command[i][0] == 'push':
            queue_box.append(int(stack_command[i][1]))
            print('ok')

        elif stack_command[i][0] == 'pop':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[0])
            del queue_box[0]

        elif stack_command[i][0] == 'front':
            if len(queue_box) == 0:
                print('error')
                continue
            print(queue_box[0])
        elif stack_command[i][0] == 'size':
            print(len(queue_box))
        elif stack_command[i][0] == 'clear':
            queue_box = []
            print('ok')
        elif stack_command[i][0] == 'exit':
            print('bye')
            break
