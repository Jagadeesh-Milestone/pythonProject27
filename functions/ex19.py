#globals method:
#it is used to access the global variable locally when there is
#same name for both global variable and local variable.
x=100
print('x value before the function:',x)
def d1():
    x=200
    print('x value inside the function:',x)
    print('global x value is:',globals()['x'])
d1()
print('x value after the function:',x)