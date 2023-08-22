import pandas as pd
import numpy as np

# ex1

s = pd.Series([1,5,2,3,7])
lst = []
for i in s:
    lst.append(i)
print(lst)

# ex2

r = np.random.rand(10)*10
s = pd.Series(r)
s1 = s[s<5]
print(s)
print(s1)

# ex3

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])
print(s1 * s2)
print(s1 / s2)
print(s1 + s2)

# ex4

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])
print(s1 == s2)
print(s1>s2)
print(s1<s2)

# ex5

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,10])
print(s1[s1 == s2])
print(s1[s1>s2])
print(s1[s1<s2])

# ex6

d = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
s = pd.Series(d)
print(s)

# ex7

s = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
print("Minimum", s.min())
print("Maximum", s.max())
print("Mean: ", s.mean())
print("Standard deviation: ", s.std())

# ex8

sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print(sr1[sr1.isin(sr2)])

# ex9

sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print(sr1[sr1.n])

# ex10

n = np.random.randint(10 , 20 , size = 150 )
s = pd.Series(n)
print (n)
print (s.value_counts())
