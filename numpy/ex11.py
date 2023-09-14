#array shape
import  numpy as np

x=np.array([[10,20,30],[40,50,60]])
print(x)
print(x.shape)

y=np.array([10,20,30],ndmin=10)
print(y)
print(y.shape)

#reshape
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(4,3)
print(b)

c=a.reshape(2,3,2)
print(c)