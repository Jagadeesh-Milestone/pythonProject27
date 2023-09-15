#labels
import pandas as pd
x=[10,20,30,40]
a=pd.Series(x)
print(a)
print(a[2])
#print(a[10])
#creating own labels
b=pd.Series(x,index=['x','y','z','s'])
print(b)
print(b['x'])
print(b['s'])
print(b['t'])