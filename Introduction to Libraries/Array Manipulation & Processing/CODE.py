import numpy as np

a = np.array([(1,1.0,'1',True),(2,2.0,'2',False),(3,3.0,'3',True)],
             dtype=[("entity",'int16'),("numeric", 'float16'), ("chain", 'S6'), ("boolean", 'b')])
a.dtype.name = ("ENTITY", "NUMERIC", "CHAIN", "BOOLEAN")
print(a["ENTITY"])

a = np.arange(9).reshape(3,3)
print(a)
np.save("firstnp" , a)
b = np.load('firstnp.npy')
print(b)

data = np.genfromtxt("test.csv",delimiter=",",dtype="int16","float16","S6")
print(test)

print(data,)

print(a[a<0.5])

for i in a:
    for j in i:
        print(j)

def ezsqrt(array):
    return array ** 0.5
print(np.apply_along_axis(ezsqrt, axis=0,arr=a))
print(np.apply_along_axis(ezsqrt, axis=1,arr=a))