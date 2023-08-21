#return a function:
def d1():
    def d2(a,b):
        return a+b
    return d2(10,30)
d=d1()
print(d)