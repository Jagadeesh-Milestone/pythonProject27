#filter:
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(i,'is a even number')
    else:
        print(i,'is a odd number')

def d1(n):
    return n%2==0
x=filter(d1,l)
print(list(x))

y=filter(lambda m:m%2==1,l)
print(tuple(y))

