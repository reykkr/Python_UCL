import numpy as np

# ex1

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[10,11,12], [13,14,15]])
sum = a + b
print(sum)

# ex2

a = np.array([x for x in range(27)]).reshape(3,3,3)
print(a)

# ex3

a1 = np.array([[1,2,3], [4,5,6]])
a2 = np.array([[7,8,9], [10,11,12]])
stack = np.hstack((a1,a2))

# ex4

a1 = np.array([[1,2], [3,4], [5,6]])
a2 = np.array([[7,8], [9,10], [10,11]])
stack = np.vstack((a1,a2))