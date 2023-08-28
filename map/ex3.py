#finding length of strings in a list:
l=['apple','banana','mango','cherry']
print(len(l))

for i in l:
    print(len(i))

def d1(n):
    return len(n)
x=map(d1,l)
print(list(x))

y=map(lambda m:len(m),l)
print(tuple(y))
