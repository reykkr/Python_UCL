matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for column in row:
        print(column, end = " ")

for row in range(len(matrix)):
    total = 0
    for col in range(len(matrix[0])):
        total = total + matrix[row][col]
    print(total)


for col in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total = total + matrix[row][col]
    print(total)