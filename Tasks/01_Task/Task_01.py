file_1 = open("input.txt", "r")

a_mass = []
c_dict = {}
d_list = []
# -------------------------------------
file_2 = file_1.readline()
while file_2 != '':
    file_2 = file_2.rstrip('\n')
    b_mass = file_2.split()
    a_mass.append(''.join(b_mass))
    file_2 = file_1.readline()
file_1.close()
del b_mass
del file_2
# -------------------------------------
a = ''.join(a_mass)
del a_mass
b_tuple = sorted(tuple(set(a)))
for i in a:
    if i not in c_dict:
        c_dict[i] = 0
    c_dict[i] += 1
del a
# -------------------------------------
d_list.append(''.join(b_tuple))
for i in range(max(c_dict.values())):
    w_str = ''
    for j in b_tuple:
        if c_dict[j] > 0:
            w_str += '#'
            c_dict[j] = c_dict[j] - 1
        elif c_dict[j] == 0:
            w_str += ' '
    d_list.append(w_str)
del b_tuple
del c_dict
del i
del j
del w_str

d_list = d_list[::-1]
#
# print(*d_list, sep='\n')

file_3 = open("output.txt", "w")
for i in range(len(d_list)):
    if i != (len(d_list) - 1):
        file_3.write(f'{d_list[i]}\n')
    else:
        file_3.write(f'{d_list[i]}')
file_3.close()
