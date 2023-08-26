#default arguments:
def d1(a,b=10):
    print(a+b)
d1(20)
d1(30,40)

#using lambda:
x=lambda x,y=30:x+y
print(x(20))
print(x(100,200))