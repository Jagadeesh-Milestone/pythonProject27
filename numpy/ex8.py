#accessing elements
import numpy as np
x=np.array([10,20,30,40])
print(x[0])
print(x[-1])

y=np.array([[10,20,30],[40,50,60]])
print(y[0,0])
print(y[1,1])
print(y[0,1])

z=np.array([[[10,20],[30,40]],[[50,60],[70,80]],[[90,100],[110,120]]])
print(z[0,0,0])
print(z[1,1,1])
print(z[2,1,1])
