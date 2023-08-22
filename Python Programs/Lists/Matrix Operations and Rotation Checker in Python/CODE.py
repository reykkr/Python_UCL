matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,4],[2,3,5],[3,4,6]]
n = eval(input("Choose your options: \n"
                "1 add matrices \n"
                "2 multiply matrices \n"
                "3 check if rotated \n"
                "4 exit \n"))
while n != 4:
    if n == 1:
        result = []
        for i in range(len(matrix1)):
            result.append([])
            for j in range(len(matrix2[i])):
                    result[i].append(matrix1[i][j] + matrix2[i][j])
        print(result)
    elif n == 2:
        result = []
        for i in range(len(matrix1)):
            result.append([])
            for j in range(len(matrix2[0])):
                result[i].append(0)
                for k in range(0, len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print(result)
    elif n == 3:
        def rotate(matrix1, matrix2):
            for i in range(len(matrix1)):
                for j in range(len(matrix1[i])):
                    if matrix1[i][j] != matrix2[j][i]:
                        return False
            return True
        print(rotate(matrix1,matrix2))
    n = eval(input("Choose your options: \n"
               "1 add matrices \n"
               "2 multiply matrices \n"
               "3 check if rotated \n"
               "4 exit \n"))