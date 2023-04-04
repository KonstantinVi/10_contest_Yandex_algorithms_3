# ---------open-in-file----------------------
file_1 = open("10.txt", "r")

N = int(file_1.readline())
'''количество учеников в классе'''
a = int(file_1.readline())
a_mass = []
for i in range(N-1):
    k = int(file_1.readline())
    if a <= k:
        a_mass.append(a)
    if k < a:
        a_mass.append(k)
    a = k
file_1.close()

print(sum(a_mass))
# ---------close-in-file----------------------
