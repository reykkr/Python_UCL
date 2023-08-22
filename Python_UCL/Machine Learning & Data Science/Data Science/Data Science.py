import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import sklearn.metrics as met

#ex4

#a
df = pd.read_table("C:/Users/m_a_g/Desktop/FinalExam-EntityLogger1.txt", delimiter="\t",header=12, engine= "python")
df.drop(range(0,12), inplace= True)
df = pd.DataFrame(df)

#b
df.drop(['this.SimTime/1[h]','this.obj'], axis= 1 , inplace= True)

#c
df.rename(columns= {'[Queue1].QueueLength':'Queue1','[Queue2].QueueLength':'Queue2','[Queue3].QueueLength':'Queue3'}, inplace= True)

#d
df.drop_duplicates(inplace= True)
s = df["Queue1"].mode()
df["Queue1"].fillna(s, inplace= True)
df["Queue2"].dropna(inplace= True)
df["Queue1"] = pd.to_numeric(df["Queue1"])
df["Queue2"] = pd.to_numeric(df["Queue2"])
df["Queue3"] = pd.to_numeric(df["Queue3"])

#e
q1 = df["Queue1"].mean()
q2 = df["Queue2"].mean()
q3 = df["Queue3"].mean()
for i in df.index:
    if df.loc[i,"Queue1"] > 70:
        df.loc[i, "Queue1"] = q1
    if df.loc[i,"Queue2"] > 70:
        df.loc[i, "Queue2"] = q2
    if df.loc[i,"Queue3"] > 70:
        df.loc[i, "Queue3"] = q3
df['Queue4'] = np.random.randint(2,25)
print(df)

#g
mea1 = df["Queue1"].mean()
mod1 = df["Queue1"].mode()[0]
std1 = df["Queue1"].std()
print("Queue1 mean, mode and std are: ", mea1, mod1, std1)
mea2 = df["Queue2"].mean()
mod2 = df["Queue2"].mode()[0]
std2 = df["Queue2"].std()
print("Queue2 mean, mode and std are: ", mea2, mod2, std2)
mea3 = df["Queue3"].mean()
mod3 = df["Queue3"].mode()[0]
std3 = df["Queue3"].std()
print("Queue3 mean, mode and std are: ", mea3, mod3, std3)

#h
x = np.percentile(df['Queue1'],90)
print(x)

#i
df.to_csv("C:/Users/m_a_g/Desktop/exam.csv")
plt.scatter(df['Queue1'],df['Queue2'])
#j
plt.grid(ls = '--',lw = 0.5)
# k
plt.xlabel('Queue1')
plt.ylabel('Queue2')
plt.title('exam')
plt.show()

# l
Y1 = df['Queue1']
plt.plot(Y1)
plt.subplot(2,2,1)

Y2 = df['Queue2']
plt.plot(Y2)
plt.subplot(2,2,2)

Y3 = df['Queue3']
plt.plot(Y3)
plt.subplot(2,2,3)

Y4 = df['Queue4']
plt.plot(Y4)
plt.subplot(2,2,4)
plt.show()

# m
Y1 = df['Queue1']
plt.plot(Y1)
plt.subplot(4,1,1)

Y2 = df['Queue2']
plt.plot(Y2)
plt.subplot(4,1,2)

Y3 = df['Queue3']
plt.plot(Y3)
plt.subplot(4,1,3)

Y4 = df['Queue4']
plt.plot(Y4)
plt.subplot(4,1,4)
plt.show()