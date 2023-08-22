import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn.metrics as met

# ex5
x = np.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])
y = np.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4,4.4,5.2])
# a
plt.scatter(x,y)
# b
slope, intercept, r, p, std_err = stats.linregress(x,y)
print(r)
y1 = []
for i in range(len(x)):
    y1.append(slope * x[i] + intercept)
plt.plot(x,y1)
# c
train_x = x[:8]
train_y = y[:8]
test_x = x[8:]
test_y = y[8:]
regmodel = np.poly1d(np.polyfit(train_x,train_y,4))
print(regmodel(8.2))
# d
plt.plot(regmodel(8.2), ms = 10, mec = 'r', mfc = 'r')
plt.show()