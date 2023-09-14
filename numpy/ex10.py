#copy and view
import numpy as np
x=np.array([10,20,30,40])
y=x.copy()
x[0]=100
print(x)
print(y)

a=x.view()
x[0]=200
print(x)
print(a)