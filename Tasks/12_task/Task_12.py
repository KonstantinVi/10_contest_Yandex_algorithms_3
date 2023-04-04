# ---------open-in-file----------------------
file_1 = open("04.txt", "r")

str_line = file_1.readline().rstrip('\n')
file_1.close()

del file_1
# ---------close-in-file----------------------

# stack_command - список команд
size_str_line = len(str_line)
''' размер списка '''

if str_line != 0:
    stack_box = []
    ''' СТЕК '''

    Flag_char = True

    for i in str_line:
        if i == '(':
            stack_box.append(i)
        elif i == ')':
            if len(stack_box) == 0 or stack_box[-1] != '(':
                Flag_char = False
                break
            stack_box.pop()

        if i == '[':
            stack_box.append(i)
        elif i == ']':
            if len(stack_box) == 0 or stack_box[-1] != '[':
                Flag_char = False
                break
            stack_box.pop()

        if i == '{':
            stack_box.append(i)
        elif i == '}':
            if len(stack_box) == 0 or stack_box[-1] != '{':
                Flag_char = False
                break
            stack_box.pop()
    if len(stack_box) == 0 and Flag_char == True: print('yes', end='')
    else: print('no', end='')