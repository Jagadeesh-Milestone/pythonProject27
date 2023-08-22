#variables:
#python has three types of variables:
#global variables(public)
#local variables (private)
#protected variables:
#global variables:
#once we declare a variable globally we can use it anywhere in the program
x=100
print('x value before the function:',x)
def d1():
    print('x value inside the function:',x)
d1()
print('x value after the function :',x)