matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
def multi(list1,list2):
        result = []
        for i in range(len(matrix1)):
            result.append([])
            for j in range(len(matrix2[0])):
                result[i].append(0)
                for k in range(0, len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result
print(multi(matrix1,matrix2))

print(multi(matrix1,matrix2))
import numpy as np
print(np.dot(matrix1,matrix2))

def find_divisors(n):
  divisors = []
  for i in range(1, n):
    if n % i == 0:
      divisors.append(i)
  return divisors


n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
n_divisors = find_divisors(n)
m_divisors = find_divisors(m)
n_sum = sum(n_divisors)
m_sum = sum(m_divisors)
if n_sum == m_sum:
    print(True)
else:
    print(False)