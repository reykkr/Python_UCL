matrix = []
num_rows = eval(input("Enter nb of rows: "))
num_cols = eval(input("Enter nb of columns: "))
for row in range(num_rows):
    matrix.append([])
    for column in range(num_cols):
        value = eval(input("Enter values: "))
        matrix[row].append(value)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

# another way

# for row in matrix:
#     print(row)

# another way

# for row in matrix:
#     for column in row:
#         print(column, end=" ")
#     print()