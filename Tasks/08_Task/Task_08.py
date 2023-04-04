# ---------open-in-file----------------------
file_1 = open("01.txt", "r")

N = int(file_1.readline())
coordinates_square = []

coordinates = list(map(int, file_1.readline().split()))
coordinates_square = [coordinates[0], coordinates[1], coordinates[0], coordinates[1]]

for i in range(N-1):
    coordinates = list(map(int, file_1.readline().split()))
    coordinates_square[0] = min(coordinates[0], coordinates_square[0])
    coordinates_square[1] = min(coordinates[1], coordinates_square[1])
    coordinates_square[2] = max(coordinates[0], coordinates_square[2])
    coordinates_square[3] = max(coordinates[1], coordinates_square[3])

file_1.close()
del file_1
# ---------close-in-file----------------------

print(*coordinates_square, end='')