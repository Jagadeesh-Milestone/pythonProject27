#print/return/yield:
def d1(a,b):
    print(a,b)
d1(10,20)

def d2(x,y):
    return x,y
print(d2(20,30))

def d3(c,d):
    yield c,d
    yield c+d
d=d3(40,50)
print(next(d))
print(next(d))