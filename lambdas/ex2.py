#multiple expressions:
def d1(a,b,c,d):
    print(a+b)
    print(b-c)
    print(c*d)
    print(d/a)
d1(3,4,5,6)

#using lambda:
x=lambda x,y,z,t:((x+y),(y-z),(z*t),(t/x))
print(x(3,4,5,6))