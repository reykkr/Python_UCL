import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn.metrics as met

# ex6

# a
n = np.random.normal(6,2,200)
x = n
# b
n1 = np.random.normal(300,40,200)
y = n1/x
# c
plt.scatter(x,y)
# d
train_x = x[:160]
train_y = y[:160]
test_x = x[160:]
test_y = y[160:]

plt.scatter(train_x,train_y,color = 'g')
plt.scatter(test_x,test_y,color = 'r')

regmodel = np.poly1d(np.polyfit(train_x,train_y,4))
print(met.r2_score(train_y,regmodel(train_x)))
regmodel = np.poly1d(np.polyfit(train_x,train_y,4))
print(met.r2_score(test_y,regmodel(test_x)))
x1 = np.linspace(0,6,100)
plt.plot(x1,regmodel(x1))

# e
print(regmodel(4.3))
print(regmodel(8.5))