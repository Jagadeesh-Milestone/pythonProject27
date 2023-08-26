#map:
l=[10,20,30,40]
for i in l:
    print(i*2)

#using map:
def d1(n):
    return n*5
m=map(d1,l)
print(list(m))

#using lambda:
x=map(lambda m:m*10,l)
print(tuple(x))
