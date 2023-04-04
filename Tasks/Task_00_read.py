# ---------open-in-file----------------------
file_1 = open("input.txt", "r")

file_2 = file_1.readline()

while file_2 != '':
    file_2 = file_2.rstrip('\n')
    b_mass = file_2.split()
    a_mass.append(''.join(b_mass))
    file_2 = file_1.readline()

file_1.close()

del b_mass
del file_2
# ---------close-in-file----------------------

CODE Programm

# ---------open-out-file---------------------
file_3 = open("output.txt", "w")

for i in range(len(d_list)):  # построчный вывод
    if i != (len(d_list) - 1):
        file_3.write(f'{d_list[i]}\n')
    else:
        file_3.write(f'{d_list[i]}')

file_3.close()
# ---------close-out-file---------------------


# ///\\\\\\/////\\\\\/////\\\\\/////\\\\\\\///////\\\\\///////\\\\\\///////\\\\\\\//////\\


# ----------------------------------------------------- ручной ввод -----------------------

diego_01 = int(input())
diego_02 = sorted(set(map(int, input().split())))

guest_01 = int(input())
guest_02 = tuple(map(int, input().split()))

# -----------------------------------------------------------------------------------------


