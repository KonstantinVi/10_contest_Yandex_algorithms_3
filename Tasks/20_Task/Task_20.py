# ---------open-in-file----------------------
file_1 = open("03.txt", "r")

N = int(file_1.readline().rstrip('\n'))
pyramid_box = list(map(int, file_1.readline().rstrip('\n').split()))

file_1.close()

del file_1


# ---------close-in-file----------------------

#  Пирамидальная сортировка
def sieve(a_mass, n, i):
    max_ind = i
    l = 2 * i + 1  # left element
    r = 2 * i + 2  # right element

    if l < n and a_mass[i] < a_mass[l]:
        max_ind = l
    if r < n and a_mass[max_ind] < a_mass[r]:
        max_ind = r

    if max_ind != i:
        a_mass[i], a_mass[max_ind] = a_mass[max_ind], a_mass[i]
        sieve(a_mass, n, max_ind)


for i in range(N, -1, -1):
    sieve(pyramid_box, N, i)

for i in range(N - 1, 0, -1):
    pyramid_box[i], pyramid_box[0] = pyramid_box[0], pyramid_box[i]
    sieve(pyramid_box, i, 0)

print(*pyramid_box)
