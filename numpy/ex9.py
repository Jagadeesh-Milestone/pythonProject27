#data types in numpy
#string
#int
#float
#boolean
#complex

import numpy as np
x=np.array([10,20,40])
print(x.dtype)

y=np.array(['apple','banana','pineapple'])
print(y.dtype)

z=np.array([10.2,11.4,12.7])
newarray=z.astype('i')
print(newarray)
print(newarray.dtype)

b=np.array([10,20,0,2,0,3,0])
c=b.astype(bool)
print(c)
print(c.dtype)
