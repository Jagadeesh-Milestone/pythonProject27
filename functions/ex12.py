#we can use the arguments of outer function inside inner function:
def d1(x,y):
    print(x+y)
    def d2():
        return x*y
    print(d2())
d1(10,5)
#we cant use the arguments of inner function in outer function:
def d3():
    print(c+d)
    def d4(c,d):
        print(c*d)
    d4(10,5)
d3()