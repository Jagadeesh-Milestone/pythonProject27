
def d1(func):
    def d2(a):
        return func(a*a)
    return d2
def d3(a):
    return a
d=d1(d3)
print(d(5))
