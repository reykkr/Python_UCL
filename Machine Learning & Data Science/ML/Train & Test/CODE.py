import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn.metrics as met

x = np.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])
y = np.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4,4.4,5.2])
#ex7
train_x = x[:8]
train_y = y[:8]
test_x = x[8:]
test_y = y[8:]
plt.scatter(train_x,train_y, color = 'g')
plt.scatter(test_x,test_y, color = 'r')
regmodel = np.poly1d(np.polyfit(train_x,train_y,1))
print(met.r2_score((train_y,regmodel(train_x))))
regmodel = np.poly1d(np.polyfit(train_x,train_y,4))
print(met.r2_score((test_y,regmodel(test_x))))
print(regmodel(5.3))
x1 = np.linspace(0,6,100)
plt.plot(x1, regmodel(x1))
plt.show()
