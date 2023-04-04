# ---------open-in-file----------------------
file_1 = open("08.txt", "r")

string_line = file_1.readline().rstrip('\n')

file_1.close()
del file_1
# ---------close-in-file----------------------

#print(string_line)

abc_dict = {}
'''словарь букв алфавита'''
for i in range(len(string_line)):
    if (string_line[i] not in abc_dict) and (string_line[i] in 'abcdefghijklmnopqrstuvwxyz'):
        abc_dict[string_line[i]] = 0

    j = i + 1
    k = len(string_line) - i
    full_amount = j * k

    abc_dict[string_line[i]] += full_amount


for i in sorted(abc_dict):
    print(f'{i}: {abc_dict[i]}')
