# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

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
    stack_box = []
    ''' СТЕК '''

    for i in range(size_stack_command):
        if stack_command[i][0] == 'push':
            stack_box.append(int(stack_command[i][1]))
            print('ok')
        elif stack_command[i][0] == 'pop':
            if len(stack_box) == 0:
                print('error')
                continue
            print(stack_box[-1])
            stack_box.pop()
        elif stack_command[i][0] == 'back':
            if len(stack_box) == 0:
                print('error')
                continue
            print(stack_box[-1])
        elif stack_command[i][0] == 'size':
            print(len(stack_box))
        elif stack_command[i][0] == 'clear':
            stack_box = []
            print('ok')
        elif stack_command[i][0] == 'exit':
            print('bye')
            break
