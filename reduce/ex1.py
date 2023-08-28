#reduce:
from functools import reduce
l=[10,20,30,40,50]
print(l)

def d1(a,b):
    return a+b
x=reduce(d1,l)
print(x)

y=reduce(lambda m,n:m+n,l)
print(y)
