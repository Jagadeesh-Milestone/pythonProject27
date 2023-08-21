#nested function with arguments:
def d1(a,b):
    print(a+b)
    def d2(c,d):
        return c*d
    print(d2(10,5))
d1(30,40)

